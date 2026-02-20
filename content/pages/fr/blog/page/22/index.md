---
title: "Blog – Page 22 – OPENGIS.ch"
date: "2011-07-05T10:35:07+02:00"
lastmod: "2020-04-29T18:56:25+02:00"
source: "www.opengis.ch/fr/blog/page/22/index.html"
---

## [GSoC 2011 weekly report #5](<../../../2011/07/05/gsoc-2011-weekly-report-5/index.html> "GSoC 2011 weekly report #5")
This week I re-factored the install script to make it cleverer, compiled expat library, fixed the last problem that was blocking GDAL from installing and compiled QWT library using necessitas. As well I started and started looking on compiling qgis and how to add external libs to a necessitas package. This week I’ll be mainly looking into how to compile QGIS to have it running on Android.
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/07/05/gsoc-2011-weekly-report-5/index.html>) 2020-04-29
## [GSoC 2011 weekly report #4](<../../../2011/06/24/gsoc-2011-weekly-report-4/index.html> "GSoC 2011 weekly report #4")
This week i finally got PROJ, GEOS and GDAL to compile and install. I updated all the instller scripts to use the NDK stand alone toolchain, using Android.mk files turned out to be more a hassle than useful. Furthermore using the standalone NDK toolchain the compire process can be totally scripted and thus integrated in bigger build systems. I started working on QWT as well and I plan to finish it next week. next week[ Read more](<../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/06/24/gsoc-2011-weekly-report-4/index.html>) 2020-04-29
## [GSoC 2011 weekly report #3](<../../../2011/06/18/gsoc-2011-weekly-report-3/index.html> "GSoC 2011 weekly report #3")
This week, I worked on trying to get Android.mk files working, it looks like using the Android Toolchain standalone (I found in the docs how to use it cleanly) was more fruity, I started working on cross compiling GDAL and it looks not too bad. Using makefiles got me to more compile mistakes than anything else. Next week I’ll discuss with Marco what we should do (use android.mk or not). The plan for next week[ Read more](<../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/06/18/gsoc-2011-weekly-report-3/index.html>) 2020-04-29
## [GSoC 2011 weekly report #2](<../../../2011/06/10/gsoc-2011-weekly-report-2/index.html> "GSoC 2011 weekly report #2")
This week I managed to crosscompile PROJ 4.7.0 and created installer scripts for it and for GEOS, which gets to the linking step. but then stops due to the absence of STL in android. diggig into the problem I discovered (I’m almost ashamed) that the NDK docs explains how to deal with that problem (big RTFD to myself). So now I’m carefully reading the NDK docs and started experimenting with ndk_build script. Next week I[ Read more](<../../../2011/06/10/gsoc-2011-weekly-report-2/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/06/10/gsoc-2011-weekly-report-2/index.html>) 2020-04-29
## [GSoC 2011 weekly report #1](<../../../2011/06/07/gsoc-2011-weekly-report-1/index.html> "GSoC 2011 weekly report #1")
all, this week i leaped more int the cross compile realm. Geos almost done and started with proj4. I updated my necessitas infrastructure to necessitas v 0.2 and we decide to target android 3.0 which is optimized for tablets. I havent updated the wiki yet since i’ve been (and still am) mainly offline at the moment. On the dev list of Qgis tere have been interesting discussions about the needs of qgis mobile. Pity they[ Read more](<../../../2011/06/07/gsoc-2011-weekly-report-1/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/06/07/gsoc-2011-weekly-report-1/index.html>) 2020-04-29
## [GSoC 2011 weekly report #0](<../../../2011/05/28/gsoc-2011-weekly-report-0/index.html> "GSoC 2011 weekly report #0")
so the first (almost) week Is over. In this week I couldn’t do much since yesterday I finally graduated. Any how I managed to squeeze into the week some work (together with stuff I had done the previous week).I finished setting up everything and I got a first Qt test application running on android. furthermore I started looking into which libraries need to be ported.I created a Wiki page [0] wiki page and a github[ Read more](<../../../2011/05/28/gsoc-2011-weekly-report-0/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/05/28/gsoc-2011-weekly-report-0/index.html>) 2021-05-07
## [QGis Globe runs on a GeoWall using ubuntu natty](<../../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html> "QGis Globe runs on a GeoWall using ubuntu natty")
  
After a day of work in the [GeoWall](<https://en.wikipedia.org/wiki/GeoWall>) lab at the [GIScience Center](<https://www.geo.uzh.ch/en/units/giscience-giva/>) of the Zurich University, I got QGis Globe to work in [QuadBuffer stereo](<https://en.wikipedia.org/wiki/Quad_buffering>) mode with [polarization glasses](<https://en.wikipedia.org/wiki/Polarized_3D_glasses>). [(suite…)](<../../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html#more-204>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html>) 2020-04-29
## [QGIS Globe runs in Trunk](<../../../2011/05/13/qgis-globe-runs-in-trunk/index.html> "QGIS Globe runs in Trunk")
Thanks to Marco Hugentobler’s idea of using Mutex, QGIS Globe now runs in Trunk, i just created a dev branch at https://github.com/mbernasocchi/Quantum-GIS/tree/mutex-globe and updated the installer script at https://www.opengis.ch/2010/12/01/qgis-globe-plugin-installer-script/ (I haven’t tried it yet but it should work) Cheers Marco
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/05/13/qgis-globe-runs-in-trunk/index.html>) 2020-04-29
## [Thats it!?](<../../../2011/04/29/thats-it/index.html> "Thats it!?")
wow, what a long night, but finally I finished my masterr thesis… 🙂 and now a free wknd!!!!
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/04/29/thats-it/index.html>) 2020-04-29
## [GSoC 2011 – I'm in](<../../../2011/04/25/gsoc-2011-im-in/index.html> "GSoC 2011 – I'm in")
Guess what appeared inmy inbox at 20.59 today!? Dear Marco, Congratulations! Your proposal « QGIS Mobile » as submitted to « OSGeo – Open Source Geospatial Foundation » has been accepted for Google Summer of Code 2011. Over the next few days, we will add you to the private Google Summer of Code Student Discussion List. Over the next few weeks, we will send instructions to this list regarding turn in proof of enrollment, tax forms, etc. Now that[ Read more](<../../../2011/04/25/gsoc-2011-im-in/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../2011/04/25/gsoc-2011-im-in/index.html>) 2020-04-29
## Pagination des publications
[Précédent](<../21/index.html>) [1](<../../index.html>) … [21](<../21/index.html>) 22 [23](<../23/index.html>) [24](<../24/index.html>) [Suivant](<../23/index.html>)
