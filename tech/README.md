# Technical overview of the whale project

* Objective 1: Create an interactive citizen science game to build training datasets
* Objective 2: Use training datasets to create a presence/absence humpback detector
* Objective 3: Generalize 1 and 2 for use in other research tasks
* Objective 4: Build a viable outreach program around this material
* Objective 5: Expand data access to the marine science community towards getting papers written

# Cyber Resources

## OrcaNav is available only on the UW network

* [OrcaNav interface](http://orca.ooirsn.uw.edu)
  * See Rob for U/P
  * Images of spectrograms are pre-built at different time scales; giving some nice zoom in / out
  * To scroll through time be sure to Stop playback
  * Number of hydrophones = 6; data are intermittently available over days/months/years
  * Use this interface to select site qualifiers i.e. switch between hydrophones
    * 80 meter site on LJ01D
    * 500 meter side on LJ01C (Endurance array)
    * (Verify this:) Anchor point (sea floor) of the Oregon slope base shallow profiler; code is LJ01A
    * 200 meter platform Oregon Slope Base shallow profiler PC01A
    * (Verify this:) Anchor point (sea floor) of the Axial shallow profiler; code is LJ03A
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


<img src="https://github.com/whaledr/whalebooks/tech/master/orcanav_passing_boat_spectrogram.png" alt="spectrogram" width="500"/>


## Other signal sources
[Is this useful?](oceanobservatories.org/community-tools) leads to the notebooks we have shared so far
    * [Sperm whale site](https://dosits.org/galleries/audio-gallery/marine-mammals/toothed-whales/sperm-whale/?vimeography_gallery=30&vimeography_video=227089578)
    * [Another](https://ocr.org/sounds/sperm-whale/) with good 'creak' examples interspersed between single clicks
- Bering strait (Erica)
- HARP, Seabass, Mobysound, Raven (Cornell), OOI, OrcaSound: To do: Look these up... useful?


## Games
* [Megaptera = megaptera.swipesforscience.org](http://megaptera.swipesforscience.org)
* [Whaledr](https://whale-dr.firebaseapp.com/#/play) (not currently maintained)
* [Bering Sea hydrophone game](http://arcticwhaledr.swipesforscience.org) (not currently maintained)
  * A3150919_08_1970_01_01T00_00_45_767212Z is a truly excellent low-frequency humpback call


## Persons
- Kerri: Signal processing
  - Seger, Kerri D., Mahdi H. Al-Badrawi, others. "An Empirical Mode Decomposition-based detection and classification approach for marine mammal vocal signals." The Journal of the Acoustical Society of America 144, no. 6 (2018): 3181-3190.
    - This is thematically related to the Hilbert-Huang transform
- Shima: Ambient noise characterization
  - Of interest: Removing ADCP pings  
- Rob
  - eScience; coordination work
- Christian contributed ships (AIS) notebook
- William Wilcock
- Rose Wade: Low-frequency mysticete calls that register on seafloor seismometers


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

## Links and references (see below for status and planning)



## Status / Plans (modified Feb 13 2019)

### Megaptera Release Planning

#### Schedule
- March 20: Rob to create an email distro with focus persons called out for a community heads-up
- March 20: Rob to ping RCC for interest
- March 20: Rob to have new training sequence installed below
- March 20: Rob to refactor the stuff at the top and bottom of this README into this section
- April 1 start of term: EE to have 40 students interested in learning about marine mammals...
- April 10: Request for EE plan/schedule for BATL project
  - Formalize { data resources > training data pipeline } 
- April 20: Pre-release to students and colleagues for comment
- May 30: Wide release with OOI RCO CAVA announcement

#### Connections with the community

- Contact POGO; Erica: 'They are doing ML tutorials for low frequency whale calls'
- Rob to interview Shima on the topic of 'cloud success on the Azure platform' 
- Shima's challenge idea: Something along the lines of a kaggle competition
- Connect with OrcaNav
- Connect with the Google Team, Scott V, William W, other science teams
- Seattle Aq? PSC? UW SoO (with UWT, Queens College)? 

#### Megaptera App (including tasks for Shrey to consider)
- Color scale dictionary options
  - Generate six spectrograms for different circumstances (see the links below on Training for examples)
  - For each generate greyscale, existing color scale, 'bone' and three other options to consider
  - The resulting 36 images will inform how the app gets rebuilt
- Revise spectrogram generator
  - Frequency range 0.01 kHz to 8.0 kHz (coordinate with Shiv)
  - Duration 10 seconds
  - Square as is now the case; group to validate whether this is still human-parseable
  - Three tic marks on each access with labels: 0 4 8 vertical left; 0 5 10 horizontal top
- Landing
  - Fun!
  - Promote accessibility of marine data science
  - Promote awareness and usability of RCO
- Training
  - Rob's new training sequence needed <---- here ---->
  - Follow up Shima to Michelle on cartoons
  - Need a comprehensive 'Whale / Fail / Flail' sequence with play-on-click audio
  - Metadata: Location, time of year, humpback expected residency patterns
- Play
  - Revised spectrogram per above
  - Oops button
  - Go To Chat toggle would be super nice
  - Can we work from base greyscale png to projecting a User-chosen color scheme in the browser?

### Broadband Hydrophone: Storm and Wind Noise
- Shima's study
- SOFAR approaches the surface towards Oregon and to the North (Arctic)
- Sound gets trapped and propagates
- Shiv has started the work on simple SNR characterization: Reducing processing time
  - Related: Can sample occasionally rather than comprehensively


### Please re-factor the following into the above material

#### EE work

- Erica E. driving a bioacoustic workflow project
  - Hydrophone archive > decomposition > spectrograms > training data > CNN transfer learning > classifier > whale data
    - Sub-topic: From Raven-Light to Python, the transfer of frequency domain finesse for isolating low frequencies, etcetera
    - Sub-topic: Dual spectrograms blowing up 0-100Hz
  - From Erica's experience we aspire to produce a short course for oceanography students
  - Shima points out: Register tools and teaching materials on the OOI website
  - Potential to share at ASA (Kentucky: May, San Diego: September)  
  - Potential to share at OceanHackWeek-2 (late August)

#### Research

- Kerri S.: Signal processing reference
  - Seger, Kerri D., Mahdi H. Al-Badrawi, others. "An Empirical Mode Decomposition-based detection and classification approach for marine mammal vocal signals." The Journal of the Acoustical Society of America 144, no. 6 (2018): 3181-3190.
  - Thematically related to the Hilbert-Huang transform
- Shima A.: Ambient noise characterization including removing ADCP pings  
- Rob F.: Has OrcaNav in-hand courtesy Mike H.; and working on resource writeup (here)
  - OOI operates six broadband hydrophones
- Christian has contributed ships (AIS) notebook
- Stay in touch with William Wilcock and Rose Wade
- Conceptual decomposition
  - Sources: OOI x 6, Orca stations, HARP, Bering Strait
  - Baleen (mysticetes), odontocetes, species break-down by frequency characteristics
  - Audience objectives: Outreach, teaching, research, operational


#### Funding
* Valentina S., Shima A., Erica E., Scott V. (OrcaSound): Southern Resident KW study proposal in eval
  * 'Otherwise': Some other path forward (hackathons etc)
* Generally: Scientists driving proposals based on this technical substrate
* ONR is interested in density estimation
