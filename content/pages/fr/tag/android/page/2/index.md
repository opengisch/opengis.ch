---
title: "Android – Page 2 – OPENGIS.ch"
date: "2011-08-14T01:19:47+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
source: "www.opengis.ch/fr/tag/android/page/2/index.html"
---

## [GSoC 2011 weekly report #11](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html> "GSoC 2011 weekly report #11")
This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no[ Read more](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>) 2020-04-29
## [GSoC 2011 weekly report #10](<../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html> "GSoC 2011 weekly report #10")
This week I finally managed to get a test Qt application packaged as an apk file. The application uses the native Proj lib to do some projections conversions. Basically it does the same as what qgis will do just with much more dependencies. The key problem was that necessitas wipes[ Read more](<../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>) 2020-04-29
## [GSoC 2011 weekly report #9](<../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html> "GSoC 2011 weekly report #9")
This week I managed to cross compile qgis and started working on packaging it. See the previous post for more details.
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html>) 2020-04-29
## [QGIS cross compiles using android NDK](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html> "QGIS cross compiles using android NDK")
Finally I managed to cross compile qgis using a NDK r5c standalone toolchain. Currently the scripts to produce the binaries require the necessitas qt source to be present on the host since QtUiTools need to be compiled as well. This should be only until QtUitools is included in necessitas (maybe[ Read more](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>) 2020-04-29
## [GSoC 2011 weekly report #8](<../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html> "GSoC 2011 weekly report #8")
This week I fought against libiconv and spatialite that did not want to properly crosscompile. Due to time pressure I decided to temporarly work on it and moved on compiling qgis. I get to the linking part of the process where I get many errors. I m now looking into[ Read more](<../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>) 2020-04-29
## [GSoC 2011 weekly report #7](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html> "GSoC 2011 weekly report #7")
This week I was at a mountaineering course so I could only work in the evening/nights. despite of the lack of time I made some nice progresses, I got qgis to configure properly (for some reasons it still needs to run twice) and to start compile. while compiling I run[ Read more](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>) 2020-04-29
## [GSoC 2011 weekly report #6](<../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html> "GSoC 2011 weekly report #6")
This week I started cross compiling qgis and encountered some problems that I could’t solve yet but I’m working on it. UPDATE: I just managed to have QGIS to properly configure, by using -DQT_QTUITOOLS_INCLUDE_DIR=/usr/include/qt4/QtUiTools since it appears that necessitas has no QtUiTools yet. I’ll look into it. UPPDATE2:or maybe not…[ Read more](<../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>) 2020-04-29
## [GSoC 2011 weekly report #5](<../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html> "GSoC 2011 weekly report #5")
This week I re-factored the install script to make it cleverer, compiled expat library, fixed the last problem that was blocking GDAL from installing and compiled QWT library using necessitas. As well I started and started looking on compiling qgis and how to add external libs to a necessitas package.[ Read more](<../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html>) 2020-04-29
## [GSoC 2011 weekly report #4](<../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html> "GSoC 2011 weekly report #4")
This week i finally got PROJ, GEOS and GDAL to compile and install. I updated all the instller scripts to use the NDK stand alone toolchain, using Android.mk files turned out to be more a hassle than useful. Furthermore using the standalone NDK toolchain the compire process can be totally[ Read more](<../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>) 2020-04-29
## [GSoC 2011 weekly report #3](<../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html> "GSoC 2011 weekly report #3")
This week, I worked on trying to get Android.mk files working, it looks like using the Android Toolchain standalone (I found in the docs how to use it cleanly) was more fruity, I started working on cross compiling GDAL and it looks not too bad. Using makefiles got me to[ Read more](<../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>) 2020-04-29
## Pagination des publications
[Précédent](<../../index.html>) [1](<../../index.html>) 2 [3](<../3/index.html>) [Suivant](<../3/index.html>)
