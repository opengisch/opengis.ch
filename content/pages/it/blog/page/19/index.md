---
title: "Blog – Pagina 19 – OPENGIS.ch"
date: "2011-10-01T03:39:43+02:00"
lastmod: "2020-04-29T16:06:56+02:00"
source: "www.opengis.ch/it/blog/page/19/index.html"
---

## [Sharing internet connection](<../../../2011/10/01/sharing-internet-connection/index.html> "Sharing internet connection")
Today, for some bizarre reasons only my android phone was connecting to a WiFi. So I decided to use it as a tethered modem. The problem was that my friend Bruno could not use the net either, so since networkmanager ad-hoc networks were not working and it is our day off climbing we decided to keep our fingers trained on the keyboard. [(altro…)](<../../../2011/10/01/sharing-internet-connection/index.html#more-322>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/10/01/sharing-internet-connection/index.html>) 2020-04-29
## [GSoC 2011 final report](<../../../2011/08/24/gsoc-2011-final-report/index.html> "GSoC 2011 final report")
So, it is over, after 3 months working on QGIS for android as a Google Summer of code project it is now time to wrap up what I did and didn’t do. First of all a QGIS android app exists now and it has many features including: – reading/writing projects – raster support – spatialite support – wms support – (apparent – untested) wfs and postgress support – partial shape files support (string attributes still[ Read more](<../../../2011/08/24/gsoc-2011-final-report/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/24/gsoc-2011-final-report/index.html>) 2020-04-29
## [QGIS Android works!](<../../../2011/08/21/qgis-android-works-2/index.html> "QGIS Android works!")
Just a quick screenshot to show that qgis on android is now a working reality. Tomorrow I’ll make a video and so on. The major missing thing now is reading shp files ad maybe spatialite… maybe tomorrow. Now it’s sunday 😉 Ciao test it now:
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/21/qgis-android-works-2/index.html>) 2020-04-29
## [QGIS Android the first test map](<../../../2011/08/20/qgis-android-the-first-test-map/index.html> "QGIS Android the first test map")
Today I loaded the first data into qgis and although the mapcanvas stays black, in the map composer the data is shown. Here some screenshots.
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/20/qgis-android-the-first-test-map/index.html>) 2020-04-29
## [GSoC 2011 weekly report #12](<../../../2011/08/20/gsoc-2011-weekly-report-12/index.html> "GSoC 2011 weekly report #12")
See my last posts. In short I managed to get qgis packaged as an apk and to properly run with only one major problem. The map canvas is always black. I ll investigate this till Tuesday. Cheers
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/20/gsoc-2011-weekly-report-12/index.html>) 2020-04-29
## [QGIS data providers and map canvas](<../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html> "QGIS data providers and map canvas")
After finishing with the gui(see previous post) i started testing the data providers.reading and writing shp files always ends in an app crash. Loading rasters, wms and gpx seems to work but the mapcanvas is never drawn. I have to investigate why. But probably it has to do with the draw used in qgis. The properties are there and get updated, but the canvasstays black. The same happens with decorations plugins like north arrow and[ Read more](<../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>) 2021-06-06
## [QGIS on android has complete gui and supports translations](<../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html> "QGIS on android has complete gui and supports translations")
Hi I just managed to create an apk with al the resources needed by qgis. On the first runrun the application extracts this file to the proper location a thus the gui is now complete. This means as well that translations and crs databases now work properly. The gui works nice beside some small glitches. It is usefull to go under settings->general->icon size and set it to 32. The only inconvenient at the moment is[ Read more](<../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html>) 2020-04-29
## [QGIS on Android has a proper GUI](<../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html> "QGIS on Android has a proper GUI")
Today I managed to get QGIS to load all the icons, providers and plugins. The GUI looks very good and quick, it is easy to use with the finger, beside the small arrows hiding multiple icons. Furthermore I discovered that customization works so that we could pre configure qgis to show bigger icons (as in Settings->Options->Icon size 32) and a subset of tool bars, all in all is cool how good it runs. To be[ Read more](<../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>) 2020-04-29
## [QGIS on Android](<../../../2011/08/17/qgis-on-android/index.html> "QGIS on Android")
Hi all, it is a pleasure to announce that I finally got Quantum GIS to start on an android (3.2) tablet (Asus transformer). I tested as well on a Samsung Galaxy phone with cyanogen mod 7 RC1 and it works a well (with the obvious screen size limitations). Qgis still doesnt load many elements, but the gui is there and the rest should be only minor issues. I’ll post more as soon as i make[ Read more](<../../../2011/08/17/qgis-on-android/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/17/qgis-on-android/index.html>) 2020-04-29
## [GSoC 2011 weekly report #11](<../../../2011/08/14/gsoc-2011-weekly-report-11/index.html> "GSoC 2011 weekly report #11")
This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no message or anything. This week I’ll investigate this problem and hopefully get it all to run, this part was definitively tougher than planed.
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>) 2020-04-29
## Paginazione degli articoli
[Precedenti](<../18/index.html>) [1](<../../index.html>) … [18](<../18/index.html>) 19 [20](<../20/index.html>) … [23](<../23/index.html>) [Successivi](<../20/index.html>)
