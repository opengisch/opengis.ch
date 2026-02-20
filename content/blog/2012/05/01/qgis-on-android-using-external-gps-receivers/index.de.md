---
title: 'QGIS on Android using external GPS receivers – OPENGIS.ch'
date: 2012-05-01
slug: "qgis-on-android-using-external-gps-receivers"
url: "/de/2012/05/01/qgis-on-android-using-external-gps-receivers/"
source: "www.opengis.ch/de/2012/05/01/qgis-on-android-using-external-gps-receivers/index.html"
---
Thanks to [FORNAT AG](<https://www.fornat.ch/>) which sponsored me I could spend some time looking for solutions to make QGIS on android working with an external GPS receiver that sends NMEA strings.  
It all boils down to the following:
  - via bluetooth works
  - via USB not yet (as soon as I get more sponsoring or time I’ll look more into it since I’ve some ideas).


To use an external bluetooth GPS you have to follow six easy steps:
  1. Turn of internal gps
  2. enable allow mock locations in settings>developer options
  3. install [Bluetooth GPS app](<https://play.google.com/store/apps/details?id=googoo.android.btgps>) (there are others as well but I had some problems, this was the best for me)
  4. Pair the tablet and the gps receiver
  5. start Bluetooth GPS select enable mock locations provider and hit connect (here you can see if the connection works by checking the coords you see or even by looking on a google map)
  6. start QGIS, enable the GPS panel (view> panels > gps) and hit connect. that’s it


The only caveat is that you can’t check satellites and signal strength directly from within QGIS since the GPS data is relayed over the mock locations provider.  
but for the rest it works as expected, now it would be cool if somehow it would be possible to connect a magic usb-to-bluetooth converter to our beloved usb only gps units…  
ciao  

### _Related_
