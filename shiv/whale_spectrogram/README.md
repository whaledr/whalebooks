# Whaledr spectrogram generation

## Contents


- [Introduction](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#introduction)
- [Pay Serious Attention](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#pay_serious_attention)
- [Overviews: Low-res and Medium-res walk-throughs](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#overviews)
- [High-res walkthrough](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#walkthrough)
- [Using **Screen**](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#screen)
- [Creating an AMI](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#create_an_ami)
- [Re-using an AMI](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#re-use_an_ami)
- [Data Manifest](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#data_manifest)
- [Whaledr Post-processing](https://github.com/whaledr/whalebooks/blob/master/shiv/whale_spectrogram/README.md#post-processing)



## Introduction

We are working with broadband hydrophones in the Ocean Observing Initiative **Regional Cabled Array**. These hydrophones
record surface noise from storms, ship passage, seismic signal, and marine mammal vocalizations, particularly whales. 
We are very interested in sharing this data and for this reason we need to do some preliminary data processing. 
Specifically this set of instructions walks through *loading* one day's worth of broadband hydrophone data to AWS S3 object 
storage by means of an AWS EC2 instance, a virtual machine (computer) on the public cloud.  

Both sound files and corresponding spectrogram images (png) are generated and stored. The source data are in seismic
`.mseed` format. Before going into the walkthrough we provide both low- and medium-resolution descriptions of the 
process. After the walkthrough we also describe using the Linux `screen` utility and using Amazon Machine Images (AMIs)
to speed up the task.

### Hydrophones

In the OOI Regional Cabled Observatory program we are familiar with six broadband hydrophones capable of recording
ambient acoustics at 40khz (and higher) sampling rates. These are the microphones that pick up humpback whale calls; 
as well as sounds made by other sorts of whales, boat engine noise, mechanical sounds (moorings rattling for example), 
and surface wind/wave action noise. 


Hydrophone data is archived at a 
['raw data' ftp server](https://rawdata.oceanobservatories.org/files/).
Here we find a large number (> 130) of sub-folders corresponding to different locations or resources of 
the Ocean Observing Initiative program. We are concerned with only six of these, all located off the coast of Oregon state.
For example the **Coastal Endurance - OR (Oregon) Offshore Cabled Benthic Experiment Package** corresponds to folder `CE04OSBP`. 
Below is the key information for these six hydrophones: The site name followed by a link to the site webpage; and then
the qualifiers needed to point at the raw data files. These qualifiers are appended to the base URL `https://rawdata.oceanobservatories.org/files/`. They are placed in the Python data loader script to 
access data from a particular site and date.


- Oregon Shelf Benthic Cabled Experiment Package, 80 meters depth
([web page](https://oceanobservatories.org/site/ce02shbp/))
  - data qualifiers: /CE02SHBP/, LJ01D/, 11-HYDBBA106/, 2015/,  09/, 03/
- Endurance Offshore (distal continental shelf), 500 meters depth
([web page](https://oceanobservatories.org/site/ce04osbp/))
  - data qualifiers: CE04OSBP/, LJ01C/, 11-HYDBBA105/, 2015/, 09/, 03/
- Oregon Slope Base sea floor, 2900 meters depth
([web page](https://oceanobservatories.org/site/rs01slbs/))
  - data qualifiers: RS01SLBS/, LJ01A/, 09-HYDBBA102/, 2015/, 09/, 03/ 
- Oregon Slope Base shallow profiler mooring, 200 meters depth
([web page](https://oceanobservatories.org/site/rs01sbps/))
  - data qualifiers: RS01SBPS/, PC01A/, 08-HYDBBA103/, 2015/, 09/, 03/
- Axial Base Seafloor; 2600 meters 
([web page](https://oceanobservatories.org/site/rs03axbs/))
  - data at RS03AXBS/, LJ03A/, 09-HYDBBA302/, 2015/, 09/, 03/ 
- Axial Base shallow profiler mooring, 200 meters depth (offline as of summer 2018) 
([web page](https://oceanobservatories.org/site/rs03axps/))
  - data at RS03AXPS/, PC03A/, 08-HYDBBA303/, 2015/, 09/, 03/


### Good megaptera days / sites


- 2018-11-15T06:07:47Z    80meter
- 2018-12-10T12:50:45Z    80meter
- 2018-12-28T09:23:24Z    80meter
- 2019-01-12T03:10:31Z    500meter   <--- very nice day
  - re-tiled on April 25 2019 0-8khz and 10 seconds. Site code is LJ01C
- 2019-01-07T14:55:27Z    500meter   
- 2019-01-14T11:39:34Z    500meter   <--- 
  - currently in progress April 26 2019, 0 -- 8 khz, 10 seconds, site code LJ01C
- 2018-12-28T03:17:33Z    SlopeBase

## Pay Serious Attention

Ok this is important! This section is what you must read right now, and I really mean it. Why? 
Because ***this is the stuff you forgot after two weeks spent doing other things***.
Read through this to remind yourself...

- This walk-through is really thorough so you are in good shape
  - but it can always be improved
- `conda activate whaledr` is an absolutely essential for the Python script to run
  - if you run `screen` you issue `conda activate whaledr` *therein*
    - Remember this walkthrough has useful notes on using `screen`
  - if you reconstitute an AMI that *should* work but doesn't: Why is that? I'll give you a sec...
    - Answer: Did you say `conda activate whaledr`? 
- access keys
  - keep them out of git repo directories; avoid wasting tens thousand dollars and days of your time
  - keep keys in `creds.json` in your root directory; contents look like this with ***double*** quotes: 
  
```
{ "key_id": "APIIJDHGUFK8TZKHCDIZ", "key_access" : "uUilebaksX9AaEa2WZYUCnXaZIUc87EgazsHdw45" }
```

  - use an S3 Browser (or something) to look in on your S3 bucket situation
    - your access keys can be tested out in the process; perhaps you need to generate new ones
    - you can clobber old datasets in preparation for generating new versions

## Overviews

### Low-resolution walkthrough

- Start an EC2 instance on AWS running Ubuntu
- Configure a Python environment, processing code and AWS credentials
- From a `screen` shell start the processing task; and wait for that to complete
- Modify this README to reflect the current state of the output dataset: What's done?
- Proceed to configure the app and so on (not covered here)

### Medium-resolution walkthrough


Read this to get a fairly complete picture of all the steps. They are repeated once more in
more detail in the following section.


- Get an AWS account including user key pair credentials.
- Log in to the AWS console and start a fairly powerful machine -- say one with 12 cores
  - We strongly urge you to use an Ubuntu (not an AWS Linux) image for this Virtual Machine
  - Note that cores and vCPUs are not the same. Generally one core is equivalent to two vCPUs
  - Be sure to own or generate the ssh key file `xxx.pem` so you can `ssh` or `sftp` to this instance
- Install a `bash` shell on your own computer if needed; and run it
  - log in to the EC2 instance
  - Per details below: Install Miniconda and then install and activate the `whaledr` Python environment
    - On this same EC2 instance clone this repository (`whalebooks`) and install dependencies
      - This is done using the `requirements.txt` file found in the data loader Python script directory
    - Issue `conda activate whaledr` to make the functional environment active
  
That's a good start. We now turn the corner to processing details. Your goal is to convert five-minute-duration
seismic format `xxx.mseed` files into 10-second clips accompanied by spectrograms in an S3 bucket where the 
broadband hydrophone source and date are captured in the directory-like structure of S3 object storage. Here we go.


- Configure a JSON credentials file in your home directory
  - This file includes both public and private keys and resides outside of any github repo folders
  - It can be configured on your own computer and transferred to the EC2 instance
    - For example using `sftp -i xxx.pem ubuntu@12.34.56.78`
- On the EC2 instance: Start a `screen` session 
  - Thus you can leave the job running even if you are disconnected from the EC2
  - Simply type `screen` on the command line
    - You are then *in* the screen shell; leave using `ctrl + a + ctrl + d`
    - You find a running screen session using `screen -ls`
    - This returns `There is a screen on: 5981.pts-0.ip-172-31-18-10   (Detached)`
  - You reconnect to this session using `screen 5981.pts-0.ip-172-31-18.10`
- Within `screen` issue `conda activate whaledr`
- Edit the `whaledr_data_push_parallel.py` to reflect your data and EC2 instance size
- Run the script: `python whaledr_data_push_parallel.py`
- Note the data you process in this `README.md` file (or somewhere stable)
  - Your note should accurately reflect the metadata needed to re-create the results
    - Date of the data
    - Location of the hydrophone including location code
    - Frequency range (e.g. 0-8khz displayed in the images)
    - Time range (e.g. each sound clip is 10 seconds)



## Walkthrough

This walk-through will make much more sense in relation to the previous section. I encourage you
to read that first before proceeding.


The script `whaledr_data_push_parallel.py` 
selects one *day* of broadband hydrophone data resident on an OOI RCA Engineering 
[Server](https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/)
and pushes this as short sound clips in `.wav` format to AWS S3 object storage. 
Each clip is also represented by a spectrogram image file in `.jpg` format.
This walkthrough covers running this script on an AWS EC2 instance (Virtual Machine) running Ubuntu Linux.


On AWS a **c5.4xlarge** EC2 instance processes a single day of broadband hydrophone
data in five hours. The source data are seismic format `.mseed` files spanning 5 minutes. 
The output files are `.png` images and `.wav` sound files spanning a few seconds (as of
April 2019: 10 seconds). Hence each `.mseed` file produces 6 x 5 x 2 = 60 output files.
There are 720 files required to span an hour; or 17,280 files per day if the source record is 
uninterrupted.


### Environment setup part 1

- Start an AWS EC2 instance running Ubuntu Linux
  - Be sure to store the access key file (`xxxx.pem`) on your local machine outside of any and all GitHub repo folders
- Log in and run the following commands individually (i.e. not as a block; some are interactive)
  - It is safe to respond `yes` to all prompts


```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda create -n whaledr python=3.6
conda activate whaledr
```

You should now be operating in the *whaledr* Python environment. However if you use the `screen` command 
(see below) you will have to re-run `conda activate whaledr` inside the screen shell.


### Environment setup part 2

Run each of the following commands in sequence, again waiting for the previous command to finish. 


```
git clone https://github.com/whaledr/whalebooks.git
cd whalebooks/shiv/whale_spectogram/ 
pip install -r requirements.txt
```

This provides you with the necessary package *within* your `whaledr` Python environment. That is: 
Doing the package install with `whaledr` activated makes those packages *stick* to the `whaledr`
environment. 


### Credential setup

Install a credential file for AWS S3 access.
This can be done using the following Python script; or by directly editing the file `creds.json` in your
home directory. 


***WARNING: If you manage to place your credentials file in a GitHub repo; and if those credentials find 
their way onto the GitHub website: With 100% certainty they will be found by a bot in minutes and used to 
mine bitcoin at your expense. Over the next two hours this will run you 15,000 US dollars. The only way to
fix the situation -- should it happen -- is to immediately Delete your access keys on the AWS console and
shut down all of the offending instances. If you think that deleting keys from GitHub is sufficient you 
will be surprised (as GitHub is about version control) that the bots will find the keys in a previous
version of your repo and proceed as above. You must delete the access keys at AWS so that they are no longer
usable. Generating new keys (that you keep out of GitHub) is easy and just takes a couple of minutes.***


flag left off here April 26 2019

Credential builder script follows; follow these steps from the home directory of your Ubuntu EC2 instance.

- Copy this code to a Python console without saving it to a file
- Ensure the Python console is not saving a ```.history``` file that records your changes (see warning above)
  - If your credentials end up inside a GitHub repo they can be found (by a bot) and used
    - ...costing you a lot of money; see warning above
- Place the public and private key strings in the script
- Run the script just once...
  - ...then delete this code from the console so that the key information is gone
- It is in fact saved in your home directory; so again do not make this part of a repository
  - `ls` from your home directory should show the file `creds.json`
- Once you are done processing hydrophone data: Delete the `creds.json` file


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

### Configure the data processing script

Edit the Python script `python whaledr_data_push_parallel.py` making two changes 

- The following line contains year, month and day strings at the extreme right: 

```
mainurl = 'https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/2017/10/09/'
``` 

Modify the date in this string to reflect the desired day to process.

- The following line of the script contains the number `12` which reflect the number of **cores** (not vCPUs) 
on the EC2 instance. Modify this if necessary to match the number of cores on the instance you are using.
- Example: The c5n.xlarge EC2 instance has 4 vCPUs and therefore 2 cores. `12` becomes `2` in the following:

```
        pool = Pool(12)                         # Create a multiprocessing Pool
```

**Note** that the script writes to an S3 bucket named `himatdata/whaledr_renamed`. 
Make sure your script is writing to the S3 location you intend.


### Run the script


Since the script will require a number of hours to run it is simplest to start it as a background job. 
This can be done for example using `nohup` but we suggest using the Linux `screen` utility. This is 
described in the **Medium Resolution** walkthrough found at the top of this page. 

- From the command line (inside `screen` if desired) issue `python whaledr_data_push_parallel.py`

### Job time

For a single day of data it takes ~5 hours wall clock time on a c5.4xlarge EC2 instance. This does
multiprocessing over all 12 available CPUs. Run time may vary based on data availability. A full day 
of data with no source dropouts will produce 30GB of **.wav** + **.png** files, a total of 34,560 files; 
this being 24 hours x 60 minutes x 12 5-second intervals per minute x 2 file types.


## Screen

- Start a Linux `screen` session so that you can leave the subsequent processing job running
  - You invoke this by simply typing `screen` on the command line
  - You are then *in* the screen shell; you leave using `ctrl + a + ctrl + d`
  - You find a running screen session using `screen -ls`
    - This returns `There is a screen on: 5981.pts-0.ip-172-31-18-10   (Detached)`
  - You reconnect to this session using `screen 5981.pts-0.ip-172-31-18.10`
  
## Create an AMI
## Re-use an AMI
## Data manifest

- whaledr bucket
  - megaptera folder
    - 500 meter Endurance array hydrophone
      - January 12 2019
    - Oregon slope base hydrophone
      - October 6 2017

- himatdata bucket
  - whaledr_renamed folder
    - Oregon slope base hydrophone
      - 2017 October 03, 04, 05
      - 2017 October 07 (partial), 08, 09, 10, 11, 12, 13, 17


## Post-processing

### Sync for the whaledr app

Once data is uploaded to the S3 bucket run `sync` to make the files available to the firebase application
(`whaledr`, `megaptera` etcetera).  You must be an **admin** on the firebase application account to do this. 
The synch is done through the firebase web console for the application. 


* Go to the admin page
* Click on **Preview** and wait for the file list to begin populating the text box
* Click **Refresh Sample List** button
* To verify something is happening: Notice the *You have N items currently* change the value of N


