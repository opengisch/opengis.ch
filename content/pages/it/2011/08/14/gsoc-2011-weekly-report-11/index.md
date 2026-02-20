---
title: "GSoC 2011 weekly report #11 – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2011-08-14T01:19:47+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
categories:
  - "Android QGIS"
  - "GSoC 2011"
  - "GSoC 2011 weekly report"
  - "QGIS"
tags:
  - "Android"
  - "Android NDK"
  - "Android Qt"
  - "qgis.org"
source: "www.opengis.ch/it/2011/08/14/gsoc-2011-weekly-report-11/index.html"
---

This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no message or anything. This week I’ll investigate this problem and hopefully get it all to run, this part was definitively tougher than planed.
### _Related_
