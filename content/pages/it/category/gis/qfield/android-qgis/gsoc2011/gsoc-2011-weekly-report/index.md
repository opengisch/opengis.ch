---
title: "GSoC 2011 weekly report – OPENGIS.ch"
date: "2011-08-24T03:06:22+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
source: "www.opengis.ch/it/category/gis/qfield/android-qgis/gsoc2011/gsoc-2011-weekly-report/index.html"
---

## [GSoC 2011 final report](<../../../../../../2011/08/24/gsoc-2011-final-report/index.html> "GSoC 2011 final report")
So, it is over, after 3 months working on QGIS for android as a Google Summer of code project it is now time to wrap up what I did and didn’t do. First of all a QGIS android app exists now and it has many features including: – reading/writing projects[ Read more](<../../../../../../2011/08/24/gsoc-2011-final-report/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../../../2011/08/24/gsoc-2011-final-report/index.html>) 2020-04-29
## [GSoC 2011 weekly report #12](<../../../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html> "GSoC 2011 weekly report #12")
See my last posts. In short I managed to get qgis packaged as an apk and to properly run with only one major problem. The map canvas is always black. I ll investigate this till Tuesday. Cheers
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../../../2011/08/20/gsoc-2011-weekly-report-12/index.html>) 2020-04-29
## [GSoC 2011 weekly report #11](<../../../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html> "GSoC 2011 weekly report #11")
This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no[ Read more](<../../../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../../../2011/08/14/gsoc-2011-weekly-report-11/index.html>) 2020-04-29
## [GSoC 2011 weekly report #10](<../../../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html> "GSoC 2011 weekly report #10")
This week I finally managed to get a test Qt application packaged as an apk file. The application uses the native Proj lib to do some projections conversions. Basically it does the same as what qgis will do just with much more dependencies. The key problem was that necessitas wipes[ Read more](<../../../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>) 2020-04-29
## [GSoC 2011 weekly report #9](<../../../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html> "GSoC 2011 weekly report #9")
This week I managed to cross compile qgis and started working on packaging it. See the previous post for more details.
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html>) 2020-04-29
## [GSoC 2011 weekly report #8](<../../../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html> "GSoC 2011 weekly report #8")
This week I fought against libiconv and spatialite that did not want to properly crosscompile. Due to time pressure I decided to temporarly work on it and moved on compiling qgis. I get to the linking part of the process where I get many errors. I m now looking into[ Read more](<../../../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>) 2020-04-29
## [GSoC 2011 weekly report #6](<../../../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html> "GSoC 2011 weekly report #6")
This week I started cross compiling qgis and encountered some problems that I could’t solve yet but I’m working on it. UPDATE: I just managed to have QGIS to properly configure, by using -DQT_QTUITOOLS_INCLUDE_DIR=/usr/include/qt4/QtUiTools since it appears that necessitas has no QtUiTools yet. I’ll look into it. UPPDATE2:or maybe not…[ Read more](<../../../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>) 2020-04-29
## [GSoC 2011 weekly report #5](<../../../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html> "GSoC 2011 weekly report #5")
This week I re-factored the install script to make it cleverer, compiled expat library, fixed the last problem that was blocking GDAL from installing and compiled QWT library using necessitas. As well I started and started looking on compiling qgis and how to add external libs to a necessitas package.[ Read more](<../../../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html>) 2020-04-29
## [GSoC 2011 weekly report #4](<../../../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html> "GSoC 2011 weekly report #4")
This week i finally got PROJ, GEOS and GDAL to compile and install. I updated all the instller scripts to use the NDK stand alone toolchain, using Android.mk files turned out to be more a hassle than useful. Furthermore using the standalone NDK toolchain the compire process can be totally[ Read more](<../../../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>) 2020-04-29
## [GSoC 2011 weekly report #3](<../../../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html> "GSoC 2011 weekly report #3")
This week, I worked on trying to get Android.mk files working, it looks like using the Android Toolchain standalone (I found in the docs how to use it cleanly) was more fruity, I started working on cross compiling GDAL and it looks not too bad. Using makefiles got me to[ Read more](<../../../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>)
By [**Marco Bernasocchi**](<../../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>) 2020-04-29
## Paginazione degli articoli
1 [2](<page/2/index.html>) [Successivi](<page/2/index.html>)
