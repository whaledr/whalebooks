# Whaledr Spectogram generation.

This repo consists of file whaledr_data_push_parallel.py which grabs data from [OOI](https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/) website and upload 5 sec Spectogram and respective sound file to s3 bucket.

## Environment setup
Run the following set of commands to setup the environment before running the script. These commands would setup the necessary conda environment and get the `whaledr_data_push_parallel.py` script alongside the `requirements.txt` file.

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

## Usage

Before executing the `whaledr_data_push_parallel.py` initial setup requires setting up requisite credential file for AWS S3.

Provide one time `key_id` and `key_access` to be stored in the `home` folder as `creds.json` which will be used by `data_fetch.py`.
```
import json
import os
from os.path import expanduser
home = expanduser("~")
# store one time credentials in the home directory
creds = {'key_id' : '',
         'key_access' : ''}
with open(os.path.join(home,'creds.json'), 'a') as cred:
    json.dump(creds, cred)
```

Post setting up credentials next steps involves defining the day of data to upload to S3: Ex. For pushing 10/09/2017 set: `mainurl = 'https://rawdata.oceanobservatories.org/files/CE02SHBP/LJ01D/11-HYDBBA106/2017/10/09/'` 

Note: Current S3 bucket is configured as `Himatdata/whaledr_renamed` which can be changed accordingly.

Run script: `python whaledr_data_push_parallel.py`
      
## Sync for the whaledr app

Once data is uploaded to S3 bucket, sync has to be initiated for the files to be available in the whaledr app.

## Runtime

For a single day of data it takes ~5 hours on a c5.4x large machine multiprocessed over 12 CPU's. The runtime may vary based on days with ideal day containing ~30GB of file size( both wav and spectogram) with ~30000 files.

