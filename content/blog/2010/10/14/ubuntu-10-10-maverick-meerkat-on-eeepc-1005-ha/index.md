---
title: 'Ubuntu 10.10 maverick meerkat on eeepc 1005 HA – OPENGIS.ch'
date: 2010-10-14
slug: "ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha"
url: "/2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/"
source: "www.opengis.ch/2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/index.html"
---
WOW, today I realized that Ubuntu 10.10 maverick meerkat was out and that I missed it by couple of days… bad me!!! (btw you have to select “normal updates” instead of “long term release” in your update manager’s settings).  
After the update my little eeepc lookt great, and everything worked out of the box without installing a tray control (including wifi, webcam, sound, hotkeys, performance modes, ecc)!!! Great Job guys and the new unity theme is great and optimizes much better the use of vertical screen estate. The only little issue is the two buttons to disable the touchpad (Fn+f3 and the little silver button on the top left) do not work, although they are recognized by the system and give an error about being unable to enable touchpad (ensure xorg.conf is configured properly). A quick workaround is to create a script that enables/disables ONLY (see comment #3) the tapping on the touchpad and to bind it to the silver button using system>keyboard shortcuts, you’ll still get the warning but it does the job.  
`#!/bin/sh  
# toggle synaptic touchpad tap on/off  
# get current state  
SYNSTATE=$(synclient -l | grep TapButton1 | awk '{ print $3 }')  
# change to other state  
if [ $SYNSTATE = 0 ]; then  
synclient TapButton1=1  
elif [ $SYNSTATE = 1 ]; then  
synclient TapButton1=0  
else  
echo "Couldn't get touchpad status from synclient"  
exit 1  
fi  
exit 0  
`  
Updating now my hp 2510 with touch screen and excited to see utouch in action…  
UPDATE: The system got slower when launching applications (just the launch phase, then they run well)… we’ll see 
### _Related_
