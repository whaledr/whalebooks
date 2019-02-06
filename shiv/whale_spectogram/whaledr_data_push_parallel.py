from obspy import read
from obspy.core import UTCDateTime
import numpy as np
from matplotlib import mlab
from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
import math as M
import requests
from lxml import html
import os
import boto3
from multiprocessing import Pool
from os.path import expanduser
import json
import gc
import time
import logging
logging.basicConfig(filename='whaledr_data_upload.log', level=logging.INFO)


def load_creds():
    """
        Utility function to read s3 credential file for
        data upload to s3 bucket.
    """
    home = expanduser("~")
    with open(os.path.join(home, 'creds.json')) as creds_file:
        creds_data = json.load(creds_file)
    return creds_data


def get_data_url_list(mainurl):
    """
        Utility function to create a list of mseed URL
        for a day from OOI website
    """
    mainurlpage = requests.get(mainurl)
    webpage = html.fromstring(mainurlpage.content)
    suburl = webpage.xpath('//a/@href')

    FileNum = len(suburl)

    data_url_list = []
    for filename in suburl[6:FileNum]:
        if filename.endswith('.mseed'):
            data_url_list.append(str(mainurl + filename[2:]))
    return data_url_list


def _nearest_pow_2(x):
    """
        Utility function to calculate nearest power.
    """
    a = M.pow(2, M.ceil(np.log2(x)))
    b = M.pow(2, M.floor(np.log2(x)))
    if abs(a - x) < abs(b - x):
        return a
    else:
        return b


def Save2Wav(sound, filename, samp_rate):
    """
        Utility function to save data data as wav file.
    """
    sound = sound.copy()
    sound.normalize()
    sound.data = (sound.data * (2**31-1)).astype('int32')
    sound.write(filename[:-8] + '.wav', format='WAV', framerate=samp_rate)


def data_push(data_url):
    """
        Utility function to upload spectogram and wav file from
        OOI website to s3.
    """
    creds_data = load_creds()
    client = boto3.client('s3', aws_access_key_id=creds_data['key_id'],
            aws_secret_access_key=creds_data['key_access'])
    try:
        hydrophone_name = data_url.split('/')[5]
        url_date = data_url.split('--')[1][4:14].replace('-','_')
        # Read from url
        stream = read(data_url)
        samp_rate = stream[0].stats.sampling_rate
        t_start = stream[0].stats.starttime
        t_end = stream[0].stats.endtime
        duration = t_end-t_start

        # Ping Detections
        duration_check = int(duration) - 1
        if duration_check > 0:
            logging.info('Executing Url: %s', data_url)
            pingtimes = np.zeros(duration_check)
            for stratpoint in range(duration_check):
                pingindex = np.argmax(stream[0].data[int(stratpoint * samp_rate):int((stratpoint + 1) * samp_rate)])
                pingtimes[stratpoint] = (t_start + stratpoint + pingindex * stream[0].stats.delta)
            # Filter Data+Plot Spectrogram+Save Image and Audio
            step_size = 5  # for calculating the rms pressure and ploting the spectrogtam
            wlen = 0.056  # bin size in sec
            nfft = int(_nearest_pow_2(wlen * samp_rate))  # number of fft points of each bin
            per_lap = 0.995      # percentage of overlap
            nlap = int(nfft * float(per_lap))   # number of overlapped samples
            timestep = 5  # save results every 5 seceonds (no overlap)

            for i in range(0, len(pingtimes), timestep):
                st = stream.slice(UTCDateTime(pingtimes[i]), UTCDateTime(pingtimes[i]) + step_size)
                trace = st[0].copy()
                # Plot Spectrogram
                npts = len(st[0])
                end = npts / samp_rate
                # using mlab to create the array of spectrogram
                specgram, freq, time = mlab.specgram(trace.data/1e-6, NFFT=nfft, Fs=samp_rate, noverlap=nlap, pad_to=None)
                specgram = 10 * np.log10(specgram[1:, :])
                specgram = np.flipud(specgram)
                freq = freq[1:] / 1e3  # Convert Frequency to kHz
                halfbin_time = (time[1] - time[0]) / 2.0
                halfbin_freq = (freq[1] - freq[0]) / 2.0
                freq = np.concatenate((freq, [freq[-1] + 2 * halfbin_freq]))
                time = np.concatenate((time, [time[-1] + 2 * halfbin_time]))
                # colormap setting
                vmin = 0.50  # default should be 0 to start from the min number of the spectrgram
                vmax = 0.95  # default should be 1 to end at the max number of the spectrgram
                _range = float(specgram.max() - specgram.min())
                vmin = specgram.min() + vmin * _range
                vmax = specgram.min() + vmax * _range

                # Save spectrogram
                fig = plt.figure(frameon=False, figsize=(8, 8))
                ax = plt.Axes(fig, [0., 0., 1., 1.])
                ax.set_axis_off()
                fig.add_axes(ax)
                dpi = fig.get_dpi()
                fig.set_size_inches(512/float(dpi), 512/float(dpi))
                ax.axis('tight')
                ax.set_xlim(0, end)
                ax.set_ylim(0, 11)
                ax.grid(False)
                ax.set_xlabel('Time [s]')
                ax.set_ylabel('Frequency [kHz]')
                filename = st[0].stats.network+'_'+st[0].stats.station+'_'+st[0].stats.location+'_'+st[0].stats.channel+'_'+str(UTCDateTime(pingtimes[i])).replace("-", "_").replace(
        ":", "_")
                plt.savefig(filename[:-8] + '.jpg')
                client.upload_file(filename[:-8] + '.jpg', 'himatdata', 'whaledr_renamed/{}/{}/'.format(hydrophone_name, url_date) +filename[:-8] + '.jpg')
                os.remove(filename[:-8] + '.jpg')
                plt.cla()
                plt.clf()
                plt.close('all')

                # save audio
                Save2Wav(st[0], filename, samp_rate)
                client.upload_file(filename[:-8] + '.wav', 'himatdata', 'whaledr_renamed/{}/{}/'.format(hydrophone_name, url_date) + filename[:-8] + '.wav')
                os.remove(filename[:-8] + '.wav')
                # delete large objects to release memory.
                del trace, st[0]
                gc.collect()
        else:
            logging.info("Skipped Url: %s", data_url)
    # check for unwanted URL format.
    except TypeError:
        logging.info('Url with type error: %s', data_url)


if __name__ == '__main__':
    start_time = time.time()
    # provide the URL for the day to extract data for.
    mainurl = 'https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/2017/10/09/'
    url_list = get_data_url_list(mainurl)
    try:
        pool = Pool(12)                         # Create a multiprocessing Pool
        pool.map(data_push, url_list)  # process data_inputs iterable with pool
    finally:
        pool.close()
        pool.join()
    logging.info("--- %s seconds ---" % (time.time() - start_time))
