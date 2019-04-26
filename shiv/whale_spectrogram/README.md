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

- 80 meter site on LJ01D
- Endurance 500 meter site LJ01C
- Oregon Slope Base profiler, seafloor, about 2900 meters LJ01A
- 200 meter *platform* for the Oregon Slope Base Shallow Profiler PC01A
- Axial Base seafloor for profiler LJ03A
- Axial shallow profiler 200 meter platform (offline since last summer) PC03A

### Good megaptera days / sites

- 2018-11-15T06:07:47Z    80meter
- 2018-12-10T12:50:45Z    80meter
- 2018-12-28T09:23:24Z    80meter
- 2019-01-12T03:10:31Z    500meter   <--- very nice day
- 2019-01-07T14:55:27Z    500meter
- 2019-01-14T11:39:34Z    500meter
- 2018-12-28T03:17:33Z    SlopeBase

## Pay Serious Attention

This section is really ***stuff you will forget after two weeks doing other things*** so please look through it 
quickly to remind yourself!!

- `conda activate whaledr` is an absolutely necessary command when you log in so the Python script runs
  - also if you run `screen`! (and this walkthrough has some useful notes on using `screen`)
  - also if you reconstitute an AMI!
- access keys
  - keep them out of git repo directories; avoid wasting tens thousand dollars and days of your time
  - keep them in `creds.json` in your root directory; where they look like this with ***double*** quotes: 
  
```
{ "key_id": "APIIJDHGUFK8TZKHCDIZ", "key_access" : "uUilebaksX9AaEa2WZYUCnXaZIUc87EgazsHdw45" }
```

## Overviews

### Low-resolution walkthrough

- Start an EC2 instance on AWS running Ubuntu
- Configure a Python environment, processing code and AWS credentials
- From a `screen` shell start the processing task; and wait for that to complete
- Note the data contribution in this README
- Post-process for app

### Medium-resolution walkthrough

Read this to get a fairly complete picture of all the steps. They are repeated once more in
more detail in the following section.


- Get an AWS account including user key pair credentials.
- Log in to the AWS console and start a fairly powerful machine -- say one with 12 cores.
  - We strongly urge you to use an Ubuntu (not an AWS Linux) image for this Virtual Machine
  - Note that cores and vCPUs are not the same. Generally one core is equivalent to two vCPUs.
  - Be sure to capture the Key file (file extension `.pem`) in order to `ssh` to this instance.
- Install a `bash` shell on your own computer if one is not present
- Use the bash shell to log in to the EC2 instance
- Follow the directions below to install Miniconda and activate the `whaledr` Python environment


You now have a good start on this project. We now turn the corner to the processing details.


- On this same EC2 instance clone this repository (`whalebooks`) and install the dependencies
  - This is done using the `requirements.txt` file found in this repo
- Configure a JSON credentials file in your home directory
  - This file includes both public and private keys and resides outside of any github repo folders
- Start a Linux `screen` session so that you can leave the subsequent processing job running
  - You invoke this by simply typing `screen` on the command line
  - You are then *in* the screen shell; you leave using `ctrl + a + ctrl + d`
  - You find a running screen session using `screen -ls`
    - This returns `There is a screen on: 5981.pts-0.ip-172-31-18-10   (Detached)`
  - You reconnect to this session using `screen 5981.pts-0.ip-172-31-18.10`
- Edit the Python script `python whaledr_data_push_parallel.py` to reflect your data and EC2 instance size
- Be sure to enter the day you are processing in the README.md notes of this repository

## Walkthrough

The script `whaledr_data_push_parallel.py` 
selects one *day* of broadband hydrophone data resident on an OOI RCA Engineering 
[Server](https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/)
and pushes this in five-second pieces to an AWS S3 bucket (object storage on the public cloud). 
Each five-second clip is represented by both an audio file and a spectrogram image file.
This walkthrough covers all the steps needed to run this script on a Linux machine; 
in fact an AWS EC2 instance (Virtual Machine) running Ubuntu Linux.


On AWS the baseline **c5.4xlarge** EC2 instance processes a single day of broadband hydrophone
data in five hours. The source data are 'seismic format' **.mseed** files spanning 5 minutes. 
The output files are **.png** images and **.wav** sound files spanning 5 seconds; hence each
**.mseed** file produces 12 x 5 x 2 = 120 output files.

Setup parts 1 and 2 accomplish the following...

* Install and update-to-latest a small version of Anaconda called 'Miniconda'
* Create and activate a Python environment called *whaledr*
* Clone this `whalebooks` repository and run pip install using `requirements.txt`
  * This installs the proper versions of the necessary Python packages


### Environment setup part 1

- Start an AWS EC2 instance running Ubuntu Linux
  - Be sure to store the access key file (`xxxx.pem`) on your local machine away from all GitHub repo folders
- Once the machine has started: Log in and run the following commands
  - Do not run them as a block; rather run each command only after the prior one has finished running
  - Some commands require you to confirm a sub-action. It is safe to respond `yes` to all the prompts.


```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda create -n whaledr python=3.6
conda activate whaledr
```

You should now be operating in the *whaledr* Python environment 


### Environment setup part 2

Run each of the following commands in sequence, again waiting for the previous command to finish. 


```
git clone https://github.com/whaledr/whalebooks.git
cd whalebooks/shiv/whale_spectogram/ 
pip install -r requirements.txt
```

The above script summarized: 


### Credential setup

Before you can run ```whaledr_data_push_parallel.py``` you must install a credential file for AWS S3 access.
This can be done using the following Python script; or by directly editing the file `creds.json` in your
home directory. 


***WARNING: If you manage to place your credentials file in a GitHub repo; and if those credentials find 
their way onto the GitHub website: With near 100% certainty they will be found very quickly (by a bot) and used to 
mine bitcoin at your expense. Typical cost to you over two hours will be 15,000 USD. The only way to
fix this -- should it happen -- is to immediately Delete your access keys on the AWS console. Deleting 
them from GitHub will not work as GitHub will keep the old credentials as part of version control. Delete
the keys and then generate new keys and start over.***


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


