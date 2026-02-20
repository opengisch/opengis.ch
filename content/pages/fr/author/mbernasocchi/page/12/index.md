---
title: "Marco Bernasocchi – Page 12 – OPENGIS.ch"
date: "2011-07-24T17:08:00+02:00"
lastmod: "2020-04-29T18:57:34+02:00"
source: "www.opengis.ch/fr/author/mbernasocchi/page/12/index.html"
---

## [GSoC 2011 weekly report #8](<../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html> "GSoC 2011 weekly report #8")
This week I fought against libiconv and spatialite that did not want to properly crosscompile. Due to time pressure I decided to temporarly work on it and moved on compiling qgis. I get to the linking part of the process where I get many errors. I m now looking into[ Read more](<../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>) 2020-04-29
## [GSoC 2011 weekly report #7](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html> "GSoC 2011 weekly report #7")
This week I was at a mountaineering course so I could only work in the evening/nights. despite of the lack of time I made some nice progresses, I got qgis to configure properly (for some reasons it still needs to run twice) and to start compile. while compiling I run[ Read more](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/07/17/gsoc-2011-weekly-report-7/index.html>) 2020-04-29
## [GSoC 2011 weekly report #6](<../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html> "GSoC 2011 weekly report #6")
This week I started cross compiling qgis and encountered some problems that I could’t solve yet but I’m working on it. UPDATE: I just managed to have QGIS to properly configure, by using -DQT_QTUITOOLS_INCLUDE_DIR=/usr/include/qt4/QtUiTools since it appears that necessitas has no QtUiTools yet. I’ll look into it. UPPDATE2:or maybe not…[ Read more](<../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/07/10/gsoc-2011-weekly-report-6/index.html>) 2020-04-29
## [Globe is in QGIS Trunk](<../../../../2011/07/06/globe-is-in-qgis-trunk/index.html> "Globe is in QGIS Trunk")
Last night Pirmin committed our Globe plugin to the QGIS trunk. this means that getting the needed dependencies (see below), building QGIS with -DWITH_GLOBE=ON and activating the plugin its all it takes to get a super globe running on QGIS. Dependencies: sudo apt-get install osgearth osgearth-dev openscenegraph (should be enough)[ Read more](<../../../../2011/07/06/globe-is-in-qgis-trunk/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/07/06/globe-is-in-qgis-trunk/index.html>) 2020-04-29
## [GSoC 2011 weekly report #5](<../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html> "GSoC 2011 weekly report #5")
This week I re-factored the install script to make it cleverer, compiled expat library, fixed the last problem that was blocking GDAL from installing and compiled QWT library using necessitas. As well I started and started looking on compiling qgis and how to add external libs to a necessitas package.[ Read more](<../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/07/05/gsoc-2011-weekly-report-5/index.html>) 2020-04-29
## [GSoC 2011 weekly report #4](<../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html> "GSoC 2011 weekly report #4")
This week i finally got PROJ, GEOS and GDAL to compile and install. I updated all the instller scripts to use the NDK stand alone toolchain, using Android.mk files turned out to be more a hassle than useful. Furthermore using the standalone NDK toolchain the compire process can be totally[ Read more](<../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>) 2020-04-29
## [GSoC 2011 weekly report #3](<../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html> "GSoC 2011 weekly report #3")
This week, I worked on trying to get Android.mk files working, it looks like using the Android Toolchain standalone (I found in the docs how to use it cleanly) was more fruity, I started working on cross compiling GDAL and it looks not too bad. Using makefiles got me to[ Read more](<../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>) 2020-04-29
## [GSoC 2011 weekly report #2](<../../../../2011/06/10/gsoc-2011-weekly-report-2/index.html> "GSoC 2011 weekly report #2")
This week I managed to crosscompile PROJ 4.7.0 and created installer scripts for it and for GEOS, which gets to the linking step. but then stops due to the absence of STL in android. diggig into the problem I discovered (I’m almost ashamed) that the NDK docs explains how to[ Read more](<../../../../2011/06/10/gsoc-2011-weekly-report-2/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/06/10/gsoc-2011-weekly-report-2/index.html>) 2020-04-29
## [GSoC 2011 weekly report #1](<../../../../2011/06/07/gsoc-2011-weekly-report-1/index.html> "GSoC 2011 weekly report #1")
all, this week i leaped more int the cross compile realm. Geos almost done and started with proj4. I updated my necessitas infrastructure to necessitas v 0.2 and we decide to target android 3.0 which is optimized for tablets. I havent updated the wiki yet since i’ve been (and still[ Read more](<../../../../2011/06/07/gsoc-2011-weekly-report-1/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/06/07/gsoc-2011-weekly-report-1/index.html>) 2020-04-29
## [GSoC 2011 weekly report #0](<../../../../2011/05/28/gsoc-2011-weekly-report-0/index.html> "GSoC 2011 weekly report #0")
so the first (almost) week Is over. In this week I couldn’t do much since yesterday I finally graduated. Any how I managed to squeeze into the week some work (together with stuff I had done the previous week).I finished setting up everything and I got a first Qt test[ Read more](<../../../../2011/05/28/gsoc-2011-weekly-report-0/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/05/28/gsoc-2011-weekly-report-0/index.html>) 2021-05-07
## Pagination des publications
[Précédent](<../11/index.html>) [1](<../../index.html>) … [11](<../11/index.html>) 12 [13](<../13/index.html>) [14](<../14/index.html>) [Suivant](<../13/index.html>)
