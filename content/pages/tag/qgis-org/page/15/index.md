---
title: "qgis.org – Page 15 – OPENGIS.ch"
date: "2012-02-01T00:52:30+01:00"
lastmod: "2020-04-29T18:55:48+02:00"
source: "www.opengis.ch/tag/qgis-org/page/15/index.html"
---

## [QGIS gets Compass support](<../../../../2012/02/01/qgis-gets-compass-support/index.html> "QGIS gets Compass support")
After implementing GPS support for QGIS on Android I’ve implemented a plugin that reads the internal compass readings and shows the value in a small dock widget. All theese new features are available in the master-alpha4 version and the nightly. Hope you enjoy
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2012/02/01/qgis-gets-compass-support/index.html>) 2020-04-29
[](<../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html> "QGIS on Android gets GPS support")
## [QGIS on Android gets GPS support](<../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html> "QGIS on Android gets GPS support")
Lately I’ve been working on adding native GPS support to QGIS on Android, here is a short video showing how it works. A big thanks goes to the municipality of Schoten in Belgium which sponsored the development. This functionality is included in the latest nightly builds as of yesterday. GPS[ Read more](<../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html>) 2020-04-29
## [QGIS on ANDROID talk at the Università degli Studi di Urbino](<../../../../2011/12/14/qgis-on-android-talk-at-the-universita-degli-studi-di-urbino/index.html> "QGIS on ANDROID talk at the Università degli Studi di Urbino")
Yesterday, thanks to Prof. Mauro De Donatis who invited me, I held a 2h talk at the Università degli Studi di Urbino about QGIS and QGIS on Android. The talk was attended by around 50 students and staff from Computer science, Geology and Ambient sciences. I liked finally holding my[ Read more](<../../../../2011/12/14/qgis-on-android-talk-at-the-universita-degli-studi-di-urbino/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/12/14/qgis-on-android-talk-at-the-universita-degli-studi-di-urbino/index.html>) 2020-04-29
## [Creating non-versioned shared libraries for android](<../../../../2011/11/23/creating-non-versioned-shared-libraries-for-android/index.html> "Creating non-versioned shared libraries for android")
While porting QGIS to android using necessitas I encountered the problem of versioned libs. Android does not support versioned libs and it is not going to. In the first vesions I used rpl -R -e libqgis_core.so.1.9.90 “libqgis_core.sox00x00x00x00x00x00x00” $APK_LIBS_DIR and similar hacks to remove the version from the libs. But it was[ Read more](<../../../../2011/11/23/creating-non-versioned-shared-libraries-for-android/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/11/23/creating-non-versioned-shared-libraries-for-android/index.html>) 2020-04-29
## [Sharing internet connection](<../../../../2011/10/01/sharing-internet-connection/index.html> "Sharing internet connection")
Today, for some bizarre reasons only my android phone was connecting to a WiFi. So I decided to use it as a tethered modem. The problem was that my friend Bruno could not use the net either, so since networkmanager ad-hoc networks were not working and it is our day off climbing we decided to keep our fingers trained on the keyboard. [(more…)](<../../../../2011/10/01/sharing-internet-connection/index.html#more-322>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/10/01/sharing-internet-connection/index.html>) 2020-04-29
## [GSoC 2011 final report](<../../../../2011/08/24/gsoc-2011-final-report/index.html> "GSoC 2011 final report")
So, it is over, after 3 months working on QGIS for android as a Google Summer of code project it is now time to wrap up what I did and didn’t do. First of all a QGIS android app exists now and it has many features including: – reading/writing projects[ Read more](<../../../../2011/08/24/gsoc-2011-final-report/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/08/24/gsoc-2011-final-report/index.html>) 2020-04-29
## [QGIS Android works!](<../../../../2011/08/21/qgis-android-works-2/index.html> "QGIS Android works!")
Just a quick screenshot to show that qgis on android is now a working reality. Tomorrow I’ll make a video and so on. The major missing thing now is reading shp files ad maybe spatialite… maybe tomorrow. Now it’s sunday 😉 Ciao test it now:
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/08/21/qgis-android-works-2/index.html>) 2020-04-29
## [QGIS Android the first test map](<../../../../2011/08/20/qgis-android-the-first-test-map/index.html> "QGIS Android the first test map")
Today I loaded the first data into qgis and although the mapcanvas stays black, in the map composer the data is shown. Here some screenshots.
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/08/20/qgis-android-the-first-test-map/index.html>) 2020-04-29
## [GSoC 2011 weekly report #12](<../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html> "GSoC 2011 weekly report #12")
See my last posts. In short I managed to get qgis packaged as an apk and to properly run with only one major problem. The map canvas is always black. I ll investigate this till Tuesday. Cheers
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html>) 2020-04-29
## [QGIS data providers and map canvas](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html> "QGIS data providers and map canvas")
After finishing with the gui(see previous post) i started testing the data providers.reading and writing shp files always ends in an app crash. Loading rasters, wms and gpx seems to work but the mapcanvas is never drawn. I have to investigate why. But probably it has to do with the[ Read more](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>) 2021-06-06
## Posts pagination
[Previous](<../14/index.html>) [1](<../../index.html>) … [14](<../14/index.html>) 15 [16](<../16/index.html>) … [19](<../19/index.html>) [Next](<../16/index.html>)
