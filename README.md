# Whalebooks 🐬🐳🐋🌊🐟🐠🐡


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

- Megaptera is in transition to public release; with many moving parts
  - Address current usability feedback 
    - Train what *is* but also what *is not*
  - Clean up spectrogram presentation
  - Formalize { data resources > training data pipeline } 
  - Connect with OrcaNav
  - Connect with the Google Team, Scott V, William W, other science teams
- Seattle Aq? PSC? UW SoO (with UWT, Queens College)? 

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

