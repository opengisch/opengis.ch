---
title: "QGIS cross compiles using android NDK – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2011-07-28T19:23:41+02:00"
lastmod: "2020-04-29T18:57:34+02:00"
categories:
  - "Android QGIS"
  - "GSoC 2011"
  - "QGIS"
tags:
  - "Android"
  - "Android NDK"
  - "Android Qt"
  - "qgis.org"
source: "www.opengis.ch/fr/2011/07/28/qgis-cross-compiles-using-android-ndk/index.html"
---

Finally I managed to cross compile qgis using a NDK r5c standalone toolchain. Currently the scripts to produce the binaries require the necessitas qt source to be present on the host since QtUiTools need to be compiled as well. This should be only until QtUitools is included in necessitas (maybe in the next release).  
For the moment only the basic library (gdal, geos, qwt, expat, gsl, sqlite and proj) are ported but they allow already a lot. The next lib (on which i already spent some time) is spatialite with its (problematic) dependency iconv.  
More important than spatialite is to actually bundle the binaries in an apk and to be able to run it on android.  
This is all new terrain for me but i m confident that if i mastered cmake i can master necessitas and the likes… 😉 I started looking at it today and plan working on it tomorrow.  
Once I get qgis on android or maybe when i ll be fed of fighting necessitas i ll implement the vertical scrollbars in the dialogs that still need it. And then Gps is still on the plan.  
So thats it for the good news of this week 🙂
### _Related_
