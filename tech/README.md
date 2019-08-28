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
