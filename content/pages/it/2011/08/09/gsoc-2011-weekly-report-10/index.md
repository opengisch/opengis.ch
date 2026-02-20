---
title: "GSoC 2011 weekly report #10 – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2011-08-09T03:07:17+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
categories:
  - "Android QGIS"
  - "GSoC 2011 weekly report"
  - "QGIS"
tags:
  - "Android"
  - "Android NDK"
  - "Android Qt"
  - "qgis.org"
source: "www.opengis.ch/it/2011/08/09/gsoc-2011-weekly-report-10/index.html"
---

This week I finally managed to get a test Qt application packaged as an apk file. The application uses the native Proj lib to do some projections conversions. Basically it does the same as what qgis will do just with much more dependencies.  
The key problem was that necessitas wipes the libs directory when it generates a project and the native libs never get pushed to the device ([bug report](<https://sourceforge.net/p/necessitas/tickets/57/>)). As well, when they get pushed, for example by using the ant Task, then there was a versioning problem. Android does not support ([and won’t in the future either](<https://comments.gmane.org/gmane.comp.handhelds.android.ndk/11819>)) versioned libs, so I had to find a way around it. I came up with two solutions, the first is a custom java method in the QtActivity class that creates symlinks or copies the libraries on runtime and loads them accordingly. the other involves editing the SONAME of each lib and padding the versioning with 0 using the rpl program (rpl -R -e libexpat.so.1 “libexpat.sox00x00” $INSTALL_DIR/lib). I dont know yet which approach to keep, but they both work properly.  
I updated all the scripts to be cleaner and I’m working now on creating the libqgisapp.so once I have this all the app should be hopefully ready.  
As well, I tried the full over th air deployement of the test app on a real device and it all works, just click on the link to the [APK arm-V5](<https://github.com/downloads/mbernasocchi/qgis-android/Qgis-debug-arm-v5.apk>) [APK arm-v7a](<https://github.com/downloads/mbernasocchi/qgis-android/Qgis-debug.apk>) and all dependencies (Qt libs as well) get installed… pretty amazing 🙂
### _Related_
