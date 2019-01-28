# Whaledr Spectrogram generation

This repo consists of whaledr_data_push_parallel.py which grabs data from an [OOI Regional Cabled Array server](https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/) and uploads 5 second 
spectrogram image + sound clip files to AWS S3 object storage.


Everything we describe here happens on a Linux machine; and if the idea is to do these operations from the 
cloud we can suggest a baseline c5.4xlarge AWS EC2 instance processes a single day of broadband hydrophone
data in a about five hours. The Python code will be operating on 'seismic format' **.mseed** files and 
producing **.png** images and **.wav** sound files.


## Environment setup

Run the following from a Linux command prompt to set up the environment before running the script. 
These commands set up the necessary conda environment and get the `whaledr_data_push_parallel.py` 
script alongside the `requirements.txt` file.

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda create -n whaledr python=3.6
conda activate whaledr

git clone https://github.com/whaledr/whalebooks.git
cd whalebooks/shiv/whale_spectogram/ 
pip install -r requirements.txt
```

The above script summarized: 

* Install a small version of Anaconda called 'Miniconda'
* Update it to latest
* Create and activate a Python environment called *whaledr*
* Clone this repository and run pip install using ```requirements.txt```
  * This installs the proper versions of the necessary Python packages

## Usage

Before executing the ```whaledr_data_push_parallel.py``` script: Install a requisite credential file for AWS S3 access.

Provide one time `key_id` and `key_access` to be stored in the `home` folder as `creds.json` which will be used by `data_fetch.py`

* Copy this code to a Python console; don't save it to a file
* Make sure that the Python console is not saving a ```.history``` file that records these contents
  * If your credentials end up inside a GitHub repo they can be found (by a bot) and used, costing you a lot of money
* Install the appropriate keys in the script and run it just once...
* ...and then delete this code from the console so that the key information is gone
* It is in fact saved in your home directory; so again do not make this part of a repository
* Once you are done with your data processing: It is a good idea to disable this authentication key

```
import json
import os
from os.path import expanduser

home = expanduser("~")
# store one time credentials in the home directory
creds = {'key_id' : '', # provide key_id
         'key_access' : '' # provide key_access
         } 
with open(os.path.join(home,'creds.json'), 'a') as cred:
    json.dump(creds, cred)
```

Post setting up credentials next steps involves defining the day of data to upload to S3: Ex. For pushing 10/09/2017 set: 

```
mainurl = 'https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/2017/10/09/'
``` 

Note: Current S3 bucket is configured as `himatdata/whaledr_renamed` which can be changed accordingly.

Run script: `python whaledr_data_push_parallel.py`
      
## Sync for the whaledr app

Once data is uploaded to S3 bucket, sync has to be initiated for the files to be available in the whaledr app.
You must be an **admin** on the firebase app account. The synch is done through the firebase web console 
for the app. 

* Go to the admin page
* Click on **Preview** and wait for the file list to begin populating the text box
* Click **Refresh Sample List** button
* To verify something is happening: Notice the *You have N items currently* change the value of N


## Runtime


For a single day of data it takes ~5 hours on a c5.4xlarge EC2 instance: multiprocessed over 12 CPU's. 
The run time may vary based on data availability. A full day of data with no source dropouts will produce
30GB of **.wav** + **.png** files, a total of 30,000 files.

