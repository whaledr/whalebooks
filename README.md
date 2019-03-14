# Whalebooks


This repository supports an ad hoc research group from UW, APL, and affiliates: Concerning submarine acoustic
data from broadband hydrophones; and with a particular emphasis on cetology, the study of whales. 


## Links and references (see below for status and planning)

* [Whaledr](https://whale-dr.firebaseapp.com/#/play) is the first version of our whale identification game
  * Data: [Regional Cabled Array](https://interactiveoceans.washington.edu/story/The_Regional_Cabled_Array)
* The [Bering Sea hydrophone game](http://arcticwhaledr.swipesforscience.org) is currently available
  * A3150919_08_1970_01_01T00_00_45_767212Z is a truly excellent low-frequency humpback call
* The [Megaptera game](http://megaptera.swipesforscience.org/#/) specific to Humpbacks
* Seabass? 
* Mobysound?
* HARP? (Hildebrand, Scripps)
* Raven from Cornell?
* OOI?
* OrcaSound?

## Status / Plans (modified Feb 13 2019)

### Outreach

- Megaptera is working again; let's  plan the release
  - Metadata: Location, time of year, humpback expected residency patterns (info in the filename for example)
    - Translational element: Rob to talk to RCC
    - Follow up with Shima on Michelle for cartoons
  - Goal: Promote the awareness and usability of RCO
  - Figures
    - Greyscale as a save format; so how to give color options (or live with a single color scale choice): Zero latency is key
    - Label axes: Cutoff at 16khz
    - Five seconds, not more than 10
      - Tic marks and numbers 0 5 10 and 0 8 16 but not a grid
    - Square images and standardization
  - Training: Rebuild the training sequence (Rob)
  - Experts
    - Kerri can contact some experts
    - Michelle Fournet
    - Kate Stafford
    - Alison Stimper
    - Rebecca Dunlop
    - And so on: Get a listing of these folks from Shima
    - Israel group: Global working group for Humpback whale social sounds. Gozzman
    - Melinda Rekdahl
    - Jessica Chen
  - Address current usability feedback 
    - Train what *is* but also what *is not*
  - Clean up spectrogram presentation
  - Formalize { data resources > training data pipeline } 
  - Connect with OrcaNav
  - Connect with the Google Team, Scott V, William W, other science teams
- Seattle Aq? PSC? UW SoO (with UWT, Queens College)? 


### Broadband Hydrophone: Storm and Wind Noise
- Shima's study
- SOFAR approaches the surface towards Oregon and to the North (Arctic)
- Sound gets trapped and propagates
- Shiv has started the work on simple SNR characterization: Reducing processing time
  - Related: Can sample occasionally rather than comprehensively




### Training

- Erica E. driving a bioacoustic workflow project
  - Hydrophone archive > decomposition > spectrograms > training data > CNN transfer learning > classifier > whale data
    - Sub-topic: From Raven-Light to Python, the transfer of frequency domain finesse for isolating low frequencies, etcetera
    - Sub-topic: Dual spectrograms blowing up 0-100Hz
  - From Erica's experience we aspire to produce a short course for oceanography students
  - Shima points out: Register tools and teaching materials on the OOI website
  - Potential to share at ASA (Kentucky: May, San Diego: September)  
  - Potential to share at OceanHackWeek-2 (late August)

### Research

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


### Funding
* Valentina S., Shima A., Erica E., Scott V. (OrcaSound): Southern Resident KW study proposal in eval
  * 'Otherwise': Some other path forward (hackathons etc)
* Generally: Scientists driving proposals based on this technical substrate
* ONR is interested in density estimation

