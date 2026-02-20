---
title: 'GSoC 2011 weekly report #11 – OPENGIS.ch'
date: 2011-08-14
slug: "gsoc-2011-weekly-report-11"
url: "/de/2011/08/14/gsoc-2011-weekly-report-11/"
source: "www.opengis.ch/de/2011/08/14/gsoc-2011-weekly-report-11/index.html"
---
This week Imanaged to get libqgisapp.so to build automatically if cmake is passed -DANDROID. as well I managed to implement all the JNI stuff that comes from necessitas. Apk file gets installed and the app tries to start but it silently fails after startQtApp is called succesfully. Logcat shows no message or anything. This week I’ll investigate this problem and hopefully get it all to run, this part was definitively tougher than planed.
### _Related_
