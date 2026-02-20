---
title: "qgis.org – Page 16 – OPENGIS.ch"
date: "2011-08-20T09:11:41+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
source: "www.opengis.ch/fr/tag/qgis-org-fr/page/16/index.html"
---

## [GSoC 2011 weekly report #12](<../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html> "GSoC 2011 weekly report #12")
See my last posts. In short I managed to get qgis packaged as an apk and to properly run with only one major problem. The map canvas is always black. I ll investigate this till Tuesday. Cheers
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html>) 2020-04-29
## [QGIS data providers and map canvas](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html> "QGIS data providers and map canvas")
After finishing with the gui(see previous post) i started testing the data providers.reading and writing shp files always ends in an app crash. Loading rasters, wms and gpx seems to work but the mapcanvas is never drawn. I have to investigate why. But probably it has to do with the[ Read more](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/19/qgis-data-providers-and-map-canvas/index.html>) 2021-06-06
## [QGIS on android has complete gui and supports translations](<../../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html> "QGIS on android has complete gui and supports translations")
Hi I just managed to create an apk with al the resources needed by qgis. On the first runrun the application extracts this file to the proper location a thus the gui is now complete. This means as well that translations and crs databases now work properly. The gui works[ Read more](<../../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/index.html>) 2020-04-29
## [QGIS on Android has a proper GUI](<../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html> "QGIS on Android has a proper GUI")
Today I managed to get QGIS to load all the icons, providers and plugins. The GUI looks very good and quick, it is easy to use with the finger, beside the small arrows hiding multiple icons. Furthermore I discovered that customization works so that we could pre configure qgis to[ Read more](<../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>) 2020-04-29
## [QGIS on Android](<../../../../2011/08/17/qgis-on-android/index.html> "QGIS on Android")
Hi all, it is a pleasure to announce that I finally got Quantum GIS to start on an android (3.2) tablet (Asus transformer). I tested as well on a Samsung Galaxy phone with cyanogen mod 7 RC1 and it works a well (with the obvious screen size limitations). Qgis still[ Read more](<../../../../2011/08/17/qgis-on-android/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/17/qgis-on-android/index.html>) 2020-04-29
## [GSoC 2011 weekly report #11](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html> "GSoC 2011 weekly report #11")
This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no[ Read more](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>) 2020-04-29
## [GSoC 2011 weekly report #10](<../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html> "GSoC 2011 weekly report #10")
This week I finally managed to get a test Qt application packaged as an apk file. The application uses the native Proj lib to do some projections conversions. Basically it does the same as what qgis will do just with much more dependencies. The key problem was that necessitas wipes[ Read more](<../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>) 2020-04-29
## [QGIS Globe runs on Win](<../../../../2011/08/02/qgis-globe-runs-on-win/index.html> "QGIS Globe runs on Win")
I just set up a win xp virtual box (remember to enable 3D acceleration) and to test out globe on windows. here what I did: Get OSGeo4W installer and run it Choose advanced install Select qgis-dev, osgearth-bin, osg-bin from the desktop packages Select osgeart-dev, osg-dev from libs Run Open Qgis,[ Read more](<../../../../2011/08/02/qgis-globe-runs-on-win/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/02/qgis-globe-runs-on-win/index.html>) 2020-04-29
## [GSoC 2011 weekly report #9](<../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html> "GSoC 2011 weekly report #9")
This week I managed to cross compile qgis and started working on packaging it. See the previous post for more details.
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html>) 2020-04-29
## [QGIS cross compiles using android NDK](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html> "QGIS cross compiles using android NDK")
Finally I managed to cross compile qgis using a NDK r5c standalone toolchain. Currently the scripts to produce the binaries require the necessitas qt source to be present on the host since QtUiTools need to be compiled as well. This should be only until QtUitools is included in necessitas (maybe[ Read more](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>) 2020-04-29
## Pagination des publications
[Précédent](<../15/index.html>) [1](<../../index.html>) … [15](<../15/index.html>) 16 [17](<../17/index.html>) … [19](<../19/index.html>) [Suivant](<../17/index.html>)
