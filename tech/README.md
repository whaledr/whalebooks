# Technical overview of the whale project


Just getting started? Coming back and need a review of the moving parts? This is the place to start.


## Objectives


* Create an interactive citizen science game to build training datasets
* Use training datasets to create a presence/absence humpback detector
* Generalize 1 and 2 for use in other research tasks
* Build a viable outreach program around this material
* Expand data access to the marine science community towards getting papers written


## Actions for you to take


* Familiarize yourself with the ***cetus*** repo here under whaledr
  * Particularly this [important README](https://github.com/whaledr/whalebooks/tree/master/shiv/whale_spectrogram)
* Combine cetus with this repo (whalebooks) to make one coherent workflow
* 10 Issues in this repo: Review / resolve / refactor / refurbish


## Workflow of the core project


### Touching on data, code, technology resources


* Data are pulled in from hydrophones along the RCA cables
* Data are stored in five-minute sound files on an APL/UW engineering server
  * These data can be played back using the APL "OrcaNav" application (from within the UW network only)
* Good candidate days (with plenty of humpback calls) are selected towards the workflow that follows
  * Only one or two days are required since a single day will produce 8640 10-second sound bites
  
I interrupt this review with a precis of some May 2019 correspondence:

> Shiv to consolidate into ***cetus*** repo: spectrogram generator, building classifier, running the classifier against newly generated spectrograms and creating a mapping file on s3 which firebase can use to reflect P(whale). This can be used by Anisha's app to sample based on probability. This code exists across whaledr so I will centralize them in cetus.  

> Rob to build "been away 4 months... need refresher course on what we are doing!!!" 

> Shiv: README addresses side issues (keys on github, EC2 memory issue) by reference.

> Shiv: There is a working cron job setup on travis that accesses S3 and generates a README which has information about the files there, updated every week. See https://github.com/whaledr/cetus/tree/master/data

> Action: Rob to test data preprocessor. Work from the README https://github.com/whaledr/cetus/tree/master/data-preprocessing

> Shiv: Future: Set up automated prediction pipeline using travis to create a lookup file based on the model for each of the spectrogram files sitting on S3 and also for any potential files we'll be generating in future.

* These data are pulled from this server (see *sourcechopper* folder code) and cut into 10-second file pairs
  * Each file pair is a spectrogram image plus an audio file
    * These are written into an S3 subsubsubfolder
    * Account number, access keys needed
    * S3 bucket = whaledr
    * subsubsubfolder = megaptera/LJ01C/2019_01_12 which is project/hydrophone/date of course
      * January 12 2019 on this hydrophone has many good whale calls
      * I suspect the images are not squared up yet
* The chopped files are staged for use in the game
* Game play involves matching an audio file to an image and evaluating "whale / fail"
* The results are tallied to eventually produce a training dataset
* The transfer learning process operates on the training data to produce a model
  * This is what Shiv's ***batl*** repo is for; it stands for Bio-Acoustic Transfer Learning
* The model is used to evaluate much larger blocks of hydrophone data (years x 6 hydrophones, etcetera)
* The results are presented in "presence / absence" ribbon format
  * The ribbon can be expanded / contracted to change the granularity


### OrcaNav and broadband hydrophone data

- SOFAR approaches the surface towards Oregon and to the North (Arctic)
  - Sound gets trapped and propagates
  - Shiv did some work on simple SNR characterization to cut processing time
    - Related idea: Sample occasionally rather than comprehensively
* [OrcaNav interface](http://orca.ooirsn.uw.edu)
  * See Rob for U/P
  * Images of spectrograms are pre-built at different time scales; giving some nice zoom in / out
  * To scroll through time be sure to Stop playback
  * Number of hydrophones = 6; data are intermittently available over days/months/years
  * Use this interface to select site qualifiers i.e. switch between hydrophones
    * 80 meter site on LJ01D
    * 500 meter side on LJ01C (Endurance array)
    * (Verify this:) Anchor point (sea floor) of the Oregon slope base shallow profiler; code is LJ01A, 2900m
    * 200 meter platform Oregon Slope Base shallow profiler PC01A
    * (Verify this:) Anchor point (sea floor) of the Axial shallow profiler; code is LJ03A; 2100m
    * 200 meter platform Axial shallow profiler (Off line since last summer ) PC03A
    * Finding whale calls: Scan for "quiet" ocean noise days, then zoom in looking for typical signals
    * Whale days:
      * http://orca.ooirsn.uw.edu/?date=2018-11-15T06:07:47Z&zoom=sec&site=80meter
      * http://orca.ooirsn.uw.edu/?date=2018-12-10T12:50:45Z&zoom=sec&site=80meter
      * http://orca.ooirsn.uw.edu/?date=2018-12-28T09:23:24Z&zoom=sec&site=80meter
      * http://orca.ooirsn.uw.edu/?date=2019-01-12T03:10:31Z&zoom=sec&site=500meter   <--- very nice day
      * http://orca.ooirsn.uw.edu/?date=2019-01-07T14:55:27Z&zoom=sec&site=500meter
      * http://orca.ooirsn.uw.edu/?date=2019-01-14T11:39:34Z&zoom=sec&site=500meter
      * http://orca.ooirsn.uw.edu/?date=2018-12-28T03:17:33Z&zoom=sec&site=SlopeBase

Here is the spectral signal of a passing boat cut from OrcaNav...


<img src="https://github.com/whaledr/whalebooks/blob/master/orcanav_passing_boat_spectrum.png" alt="boat spectrum" width="500"/>


### Other signal sources

- Broken link: oceanobservatories.org/community-tools was shared notebooks
- [Sperm whale site](https://dosits.org/galleries/audio-gallery/marine-mammals/toothed-whales/sperm-whale/?vimeography_gallery=30&vimeography_video=227089578)
- [...and another](https://ocr.org/sounds/sperm-whale/) with good 'creak' examples interspersed between single clicks
- Bering strait (Erica)
- HARP, Seabass, Mobysound, Raven (Cornell), OOI, OrcaSound: To do: Look these up... useful?


## Game links

* [Megaptera = megaptera.swipesforscience.org](http://megaptera.swipesforscience.org)
* [Whaledr](https://whale-dr.firebaseapp.com/#/play) (not currently maintained)
* [Bering Sea hydrophone game](http://arcticwhaledr.swipesforscience.org) (not currently maintained)
  * A3150919_08_1970_01_01T00_00_45_767212Z is a truly excellent low-frequency humpback call


## Persons
- Sarah
- Daria
- Matt
  - Strong interest in the ML
- Shima: Ambient noise characterization
  - Of interest: Removing ADCP pings  
  - currently calibrating hydrophone data
  - EPO: Worked with highschool students
- Shiv
  - Available!
- Erica
  - bioacoustic transfer learning (BATL) workflow
    - Hydrophone archive > decomposition > spectrograms > training data > CNN transfer learning > classifier > whale data
      - Sub-topic: From Raven-Light to Python, the transfer of frequency domain finesse for isolating low frequencies, etcetera
      - Sub-topic: Dual spectrograms blowing up 0-100Hz
  - Aspire to produce a short course for oceanography students
  - Imperative: Register tools and teaching materials on the OOI website
  - Potential to share at ASA
- Michelle: Illustrations, videos
- Kerri: Signal processing
  - Seger, Kerri D., Mahdi H. Al-Badrawi, others. "An Empirical Mode Decomposition-based detection and classification approach for marine mammal vocal signals." The Journal of the Acoustical Society of America 144, no. 6 (2018): 3181-3190. (Thematically ~ H-H Transform)
- Rob
  - eScience; coordination work
- Christian contributed ships (AIS) notebook
- William: Seismics
- Rose Wade
  - Low-frequency mysticete calls that register on seafloor seismometers


## Conceptual project components
- Species break-down by call types and frequency characteristics
- Audience objectives: Outreach, teaching, research, operational
- Sound sources
  - ambient boat noise, waves, wind, rain, marine life particularly mammals, fish, plankton
- Odontocetes are toothed whales: porpoises, dolphins, orcas, sperm whales
- Mysticetes are baleen whales (grey, blue, right, sei, fin, and humpback whales to name a few)
- [We would like to share with you the experience of hearing a humpback whale 'singing' in the Pacific](http://megaptera.swipesforscience.org)


<img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Humpback_whale_NOAA.jpg" alt="humpback" width="500"/>


- How does this game connect to whale research? Awareness is a good thing! Further: We wish to train a computer to recognize humpback calls automatically. This requires thousands of positive and negative results. You help us build this training dataset.
  - Each round of the game has two pieces: A sound clip and a picture of that sound.


<img src="https://github.com/whaledr/whalebooks/blob/master/megaptera_spectrogram.png" alt="spectrogram" width="500"/>

## Other open action items

- Create an email distro
- Install new training sequence
- Review and formalize the continuation plan for BATL { data resources > training data pipeline } 
- Per Erica check in on POGO doing ML tutorials for low frequency whale calls
- Erica suggests she provide 10-15 minute .wav files with calls > S3 as resource
- Shima to contribute a perspective on Azure
- Shima to comment on a potential kaggle competition
- Connect with the Google Team, Scott V, William W, other interested parties
- Outreach connections: Seattle Aq? PSC? UW SoO, Queens College? 
- Megaptera improvements, needed pieces
  - Color scheme x spectrogram formation idea
    - Perhaps six spectrograms with different parameters
    - For each perhaps six images (greyscale, 'bone', ...)
    - Resulting 36 images as a type of customization
  - Revise spectrogram generator
    - Frequency range 0.01 kHz to 8.0 kHz (coordinate with Shiv)
    - Duration 10 seconds
    - Square aspect (no black rectangle at base)
    - Three tic marks on each access with labels: 0 4 8 vertical left; 0 5 10 horizontal top
  - Landing page
    - Exude fun, promote accessibility of marine data science, awareness and usability of RCA
- Training
  - Tutorial: Reqs to Michelle
  - Revisit 'Whale / Flail / Fail'
  - Metadata: Location, time of year, humpback expected residency patterns
- Play
  - Oops button
  - Go To Chat toggle would be super nice
