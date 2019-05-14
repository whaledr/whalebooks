
# Whalebooks

This repo supports citizen science contributions to automatic whale call identification. The most carefully built
of these three is called **Megaptera** as it is concerned entirely with Humpback whale (Megaptera novaeangliae) vocalization.


## Megaptera

Oceanographers maintain underwater microphones called *hydrophones* that record audio signals from within the ocean.
These include noise from boats, the sounds that waves make together with the sounds of wind and rain, and the sounds
made by sea creatures; particularly whales. Of these there are two broad categories: Toothed whales (porpoises, dolphins,
orcas, sperm whales) and baleen whales (grey, blue, sei, fin, and humpbacks to name a few). We would like to share with 
you the experience of hearing a humpback whale 'singing' in the Pacific ocean by means of a game. Simply go to 
[this link](http://megaptera.swipesforscience.com) and click on ***Play Now***. To get more involved you can Sign Up.
The game will track how many rounds you play on our leaderboard.


How does this affect whale research? Excellent question! We would like to train a computer to recognize humpback calls; 
but to do so requires thousands of examples (both *Yes* and *No*) for the training to work. This -- by the way -- is an
example of the relatively new field of machine learning in data science, a sub-discipline of artificial intelligence. 
As you play the game you will notice that each round has two matched components: A sound clip and a picture of that sound.
Here is an example of that picture...


<img src="https://github.com/whaledr/whalebooks/blob/master/megaptera_spectrogram.png" alt="drawing" width="500"/>







This repository supports an ad hoc research group from UW, APL, and affiliates: Concerning submarine acoustic
data from broadband hydrophones; and with a particular emphasis on cetology, the study of whales
[.](https://github.com/robfatland/ops)


## Links and references (see below for status and planning)

* [Whaledr](https://whale-dr.firebaseapp.com/#/play) is the first version of our whale identification game
  * Data: [Regional Cabled Array](https://interactiveoceans.washington.edu/story/The_Regional_Cabled_Array)
  * OOI is [here](oceanobservatories.org/communit-tools) leads to the notebooks we have shared so far
* The [Bering Sea hydrophone game](http://arcticwhaledr.swipesforscience.org) is currently available
  * A3150919_08_1970_01_01T00_00_45_767212Z is a truly excellent low-frequency humpback call
* The [Megaptera game](http://megaptera.swipesforscience.org/#/) specific to Humpbacks
  * Disambiguation issues: potential mechanical noise and sperm whale echolocation signals 
    * [Sperm whale site](https://dosits.org/galleries/audio-gallery/marine-mammals/toothed-whales/sperm-whale/?vimeography_gallery=30&vimeography_video=227089578)
    * [Another](https://ocr.org/sounds/sperm-whale/) with good 'creak' examples interspersed between single clicks
* Seabass? 
* Mobysound?
* HARP? (Hildebrand, Scripps)
* Raven from Cornell?
* OOI?
* OrcaSound?

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

