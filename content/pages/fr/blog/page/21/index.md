---
title: "Blog – Page 21 – OPENGIS.ch"
date: "2011-08-17T01:38:17+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
source: "www.opengis.ch/fr/blog/page/21/index.html"
---

## [QGIS on Android](<../../../2011/08/17/qgis-on-android/index.html> "QGIS on Android")
Hi all, it is a pleasure to announce that I finally got Quantum GIS to start on an android (3.2) tablet (Asus transformer). I tested as well on a Samsung Galaxy phone with cyanogen mod 7 RC1 and it works a well (with the obvious screen size limitations). Qgis still doesnt load many elements, but the gui is there and the rest should be only minor issues. I’ll post more as soon as i make[ Read more](<../../../2011/08/17/qgis-on-android/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../2011/08/17/qgis-on-android/index.html>) 2020-04-29
## [GSoC 2011 weekly report #11](<../../../2011/08/14/gsoc-2011-weekly-report-11/index.html> "GSoC 2011 weekly report #11")
This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no message or anything. This week I’ll investigate this problem and hopefully get it all to run, this part was definitively tougher than planed.
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>) 2020-04-29
## [GSoC 2011 weekly report #10](<../../../2011/08/09/gsoc-2011-weekly-report-10/index.html> "GSoC 2011 weekly report #10")
This week I finally managed to get a test Qt application packaged as an apk file. The application uses the native Proj lib to do some projections conversions. Basically it does the same as what qgis will do just with much more dependencies. The key problem was that necessitas wipes the libs directory when it generates a project and the native libs never get pushed to the device (bug report). As well, when they get[ Read more](<../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>) 2020-04-29
## [QGIS Globe runs on Win](<../../../2011/08/02/qgis-globe-runs-on-win/index.html> "QGIS Globe runs on Win")
I just set up a win xp virtual box (remember to enable 3D acceleration) and to test out globe on windows. here what I did: Get OSGeo4W installer and run it Choose advanced install Select qgis-dev, osgearth-bin, osg-bin from the desktop packages Select osgeart-dev, osg-dev from libs Run Open Qgis, activate the globe plugin in plugin manager, click on the globe button and post here your success stories 😉
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../2011/08/02/qgis-globe-runs-on-win/index.html>) 2020-04-29
## [GSoC 2011 weekly report #9](<../../../2011/07/29/gsoc-2011-weekly-report-9/index.html> "GSoC 2011 weekly report #9")
This week I managed to cross compile qgis and started working on packaging it. See the previous post for more details.
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../2011/07/29/gsoc-2011-weekly-report-9/index.html>) 2020-04-29
## [QGIS cross compiles using android NDK](<../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html> "QGIS cross compiles using android NDK")
Finally I managed to cross compile qgis using a NDK r5c standalone toolchain. Currently the scripts to produce the binaries require the necessitas qt source to be present on the host since QtUiTools need to be compiled as well. This should be only until QtUitools is included in necessitas (maybe in the next release). For the moment only the basic library (gdal, geos, qwt, expat, gsl, sqlite and proj) are ported but they allow already[ Read more](<../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>) 2020-04-29
## [GSoC 2011 weekly report #8](<../../../2011/07/24/gsoc-2011-weekly-report-8/index.html> "GSoC 2011 weekly report #8")
This week I fought against libiconv and spatialite that did not want to properly crosscompile. Due to time pressure I decided to temporarly work on it and moved on compiling qgis. I get to the linking part of the process where I get many errors. I m now looking into them. Furthermore I refactored the scripts to be more solid and I did a major wiki update (added errors, added how to, cleanup,…). I m[ Read more](<../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>) 2020-04-29
## [GSoC 2011 weekly report #7](<../../../2011/07/17/gsoc-2011-weekly-report-7/index.html> "GSoC 2011 weekly report #7")
This week I was at a mountaineering course so I could only work in the evening/nights. despite of the lack of time I made some nice progresses, I got qgis to configure properly (for some reasons it still needs to run twice) and to start compile. while compiling I run into the problem that qreal are typedef to float when compiling from arm, so I patched qglobal.h to remove the float typedef and set it[ Read more](<../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>) 2020-04-29
## [GSoC 2011 weekly report #6](<../../../2011/07/10/gsoc-2011-weekly-report-6/index.html> "GSoC 2011 weekly report #6")
This week I started cross compiling qgis and encountered some problems that I could’t solve yet but I’m working on it. UPDATE: I just managed to have QGIS to properly configure, by using -DQT_QTUITOOLS_INCLUDE_DIR=/usr/include/qt4/QtUiTools since it appears that necessitas has no QtUiTools yet. I’ll look into it. UPPDATE2:or maybe not… got more errors now 🙁 As well I met with my mentor and we discussed the next steps needted after qgis compiles. We decided which[ Read more](<../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>) 2020-04-29
## [Globe is in QGIS Trunk](<../../../2011/07/06/globe-is-in-qgis-trunk/index.html> "Globe is in QGIS Trunk")
Last night Pirmin committed our Globe plugin to the QGIS trunk. this means that getting the needed dependencies (see below), building QGIS with -DWITH_GLOBE=ON and activating the plugin its all it takes to get a super globe running on QGIS. Dependencies: sudo apt-get install osgearth osgearth-dev openscenegraph (should be enough) WARNING: it appears if you don’t install osgearth-dev, then the plugin will compile fine but will not be available for activation in the plugin list.[ Read more](<../../../2011/07/06/globe-is-in-qgis-trunk/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/07/06/globe-is-in-qgis-trunk/index.html>) 2020-04-29
## Pagination des publications
[Précédent](<../20/index.html>) [1](<../../index.html>) … [20](<../20/index.html>) 21 [22](<../22/index.html>) … [24](<../24/index.html>) [Suivant](<../22/index.html>)
