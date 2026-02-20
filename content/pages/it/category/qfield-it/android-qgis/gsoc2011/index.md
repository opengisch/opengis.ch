---
title: "GSoC 2011 – OPENGIS.ch"
date: "2011-08-21T12:03:15+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
source: "www.opengis.ch/it/category/qfield-it/android-qgis/gsoc2011/index.html"
---

## [QGIS Android works!](<../../../../2011/08/21/qgis-android-works-2/index.html> "QGIS Android works!")
Just a quick screenshot to show that qgis on android is now a working reality. Tomorrow I’ll make a video and so on. The major missing thing now is reading shp files ad maybe spatialite… maybe tomorrow. Now it’s sunday 😉 Ciao test it now:
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/21/qgis-android-works-2/index.html>) 2020-04-29
## [QGIS Android the first test map](<../../../../2011/08/20/qgis-android-the-first-test-map/index.html> "QGIS Android the first test map")
Today I loaded the first data into qgis and although the mapcanvas stays black, in the map composer the data is shown. Here some screenshots.
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/20/qgis-android-the-first-test-map/index.html>) 2020-04-29
## [GSoC 2011 weekly report #12](<../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html> "GSoC 2011 weekly report #12")
See my last posts. In short I managed to get qgis packaged as an apk and to properly run with only one major problem. The map canvas is always black. I ll investigate this till Tuesday. Cheers
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html>) 2020-04-29
## [QGIS data providers and map canvas](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html> "QGIS data providers and map canvas")
After finishing with the gui(see previous post) i started testing the data providers.reading and writing shp files always ends in an app crash. Loading rasters, wms and gpx seems to work but the mapcanvas is never drawn. I have to investigate why. But probably it has to do with the[ Read more](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>) 2021-06-06
## [QGIS on android has complete gui and supports translations](<../../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html> "QGIS on android has complete gui and supports translations")
Hi I just managed to create an apk with al the resources needed by qgis. On the first runrun the application extracts this file to the proper location a thus the gui is now complete. This means as well that translations and crs databases now work properly. The gui works[ Read more](<../../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html>) 2020-04-29
## [QGIS on Android has a proper GUI](<../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html> "QGIS on Android has a proper GUI")
Today I managed to get QGIS to load all the icons, providers and plugins. The GUI looks very good and quick, it is easy to use with the finger, beside the small arrows hiding multiple icons. Furthermore I discovered that customization works so that we could pre configure qgis to[ Read more](<../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>) 2020-04-29
## [QGIS on Android](<../../../../2011/08/17/qgis-on-android/index.html> "QGIS on Android")
Hi all, it is a pleasure to announce that I finally got Quantum GIS to start on an android (3.2) tablet (Asus transformer). I tested as well on a Samsung Galaxy phone with cyanogen mod 7 RC1 and it works a well (with the obvious screen size limitations). Qgis still[ Read more](<../../../../2011/08/17/qgis-on-android/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/17/qgis-on-android/index.html>) 2020-04-29
## [GSoC 2011 weekly report #11](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html> "GSoC 2011 weekly report #11")
This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no[ Read more](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>) 2020-04-29
## [QGIS cross compiles using android NDK](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html> "QGIS cross compiles using android NDK")
Finally I managed to cross compile qgis using a NDK r5c standalone toolchain. Currently the scripts to produce the binaries require the necessitas qt source to be present on the host since QtUiTools need to be compiled as well. This should be only until QtUitools is included in necessitas (maybe[ Read more](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>) 2020-04-29
## [GSoC 2011 weekly report #7](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html> "GSoC 2011 weekly report #7")
This week I was at a mountaineering course so I could only work in the evening/nights. despite of the lack of time I made some nice progresses, I got qgis to configure properly (for some reasons it still needs to run twice) and to start compile. while compiling I run[ Read more](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>) 2020-04-29
## Paginazione degli articoli
1 [2](<page/2/index.html>) [Successivi](<page/2/index.html>)
