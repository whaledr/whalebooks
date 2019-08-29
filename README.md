
# Whalebooks


## Folders


* tech: technical notes on the project
* training: Links to good samples (I think from January 12 or so, 2019) for training Megaptera players
* sourcechopper: Gets 5-minute files from the engineering server and cuts them into 10-second { image + sound } pairs
* notebooks: Python notebooks that may suffer from some version overlap; see also the whaledr *cetus* repo
* ais: AIS ship locations close to hydrophones; i.e. register acoustic engine signatures
* data: A few sound files by way of examples


## Overview


This repo supports citizen science contributions to automatic whale call identification. **Megaptera** is the
current (2019) focus, concerned with Humpback whale (**Megaptera novaeangliae**) 
vocalization[.](https://github.com/robfatland/ops) To get started on the technical components of the project
please open the [***tech*** folder](https://github.com/whaledr/whalebooks/tree/master/tech). 
The balance of this page is towards outreach.


## Background for the Giant-wing project

In February 2018 a group of thirty oceanographers gathered at the University of Washington to learn more
about a gigantic ongoing undersea experiment called the Regional Cabled Observatory.
This observatory has taken two decades to build on the floor of
the eastern Pacific ocean. It spans 300 miles from the coast of Oregon out to an active volcano called Axial 
and its job is looks at, listens to, and sense the state of the ocean, sending data back via the internet to 
the scientists' computers for analysis. The UW meeting (called a "hack week") ran for five days 
with lots of brainstorming and sharing of ideas. The underlying questions on the scientists' minds were
"What is this data trying to tell us?" and "How can we share this with more scientists and with students?" 
The array of sensors in the RCO can get a bit overwhelming: Seismic tremors from the volcano, 
streaming video of black smokers (super-hot volcanic vents), measurements of temperature and 
ocean currents, nutrient levels that supply primary production in the upper ocean, a steady watch on
the migrations of grazing plankton... and undersea microphones (*hydrophones*) that record the sounds within the ocean.


These sounds include boat noise, the sounds that waves make together with the sounds of wind and rain, and the sounds
made by sea creatures; particularly whales. Concerning whales there are two broad categories: Toothed whales (porpoises, dolphins,
orcas, sperm whales) and baleen whales (grey, blue, right, sei, fin, and humpback whales to name a few). We would like to share with 
you the experience of hearing a humpback whale 'singing' in the Pacific ocean by means of a game. Simply go to 
[this link](http://megaptera.swipesforscience.org) and click on ***Play Now***.
The game is cooperative; but it *will* track how many rounds you play on the leaderboard.


<img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Humpback_whale_NOAA.jpg" alt="humpback" width="500"/>


How does this game connect to whale research? First we feel that awareness is a good thing for everyone concerned.
Second we can train a computer to recognize humpback calls automatically but to do so requires thousands of examples 
(both *Yes* and *No*). By playing the game you contribute to this training dataset. This by the way is machine learning, 
a sub-discipline of artificial intelligence. 


As you play the game you will notice that each round has two matched pieces: A sound clip and a picture of that sound.
Here is an example picture...


<img src="https://github.com/whaledr/whalebooks/blob/master/megaptera_spectrogram.png" alt="spectrogram" width="500"/>


To help you make sense of this we have included a mini-tutorial in the game website. 
Notice that the left-to-right direction of the plot is 10 seconds; so it represents time. 
The sound clip is ten seconds long. The bottom-to-top direction is frequency where lines
and squiggles are noises. 


Notice in the image that there are two sets of narrow vertical lines, in the upper and lower halves. The upper
streaks are from a research sonar. The lower streaks are from creaking of the underwater structure. Everything
else is humpback vocalizations. 


The Regional Cabled Observatory maintains several such microphones off the coast of Oregon. 


