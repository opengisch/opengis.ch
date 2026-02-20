---
title: "GSoC 2011 weekly report #2 – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2011-06-10T15:39:10+02:00"
lastmod: "2020-04-29T18:56:25+02:00"
categories:
  - "Android QGIS"
  - "GSoC 2011 weekly report"
tags:
  - "Android"
  - "Android NDK"
  - "Android Qt"
  - "qgis.org"
source: "www.opengis.ch/it/2011/06/10/gsoc-2011-weekly-report-2/index.html"
---

This week I managed to crosscompile PROJ 4.7.0 and created installer scripts for it and for GEOS, which gets to the linking step. but then stops due to the absence of STL in android. diggig into the problem I discovered (I’m almost ashamed) that the NDK docs explains how to deal with that problem (big RTFD to myself). So now I’m carefully reading the NDK docs and started experimenting with ndk_build script.  
Next week I want to create ndk make files for this two libs and start on working on the next ones. I’m finally starting to understand the whole picture.
### _Related_
