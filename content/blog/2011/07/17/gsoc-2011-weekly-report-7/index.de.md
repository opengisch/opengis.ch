---
title: 'GSoC 2011 weekly report #7 – OPENGIS.ch'
date: 2011-07-17
slug: "gsoc-2011-weekly-report-7"
url: "/de/2011/07/17/gsoc-2011-weekly-report-7/"
source: "www.opengis.ch/de/2011/07/17/gsoc-2011-weekly-report-7/index.html"
---
This week I was at a mountaineering course so I could only work in the evening/nights. despite of the lack of time I made some nice progresses, I got qgis to configure properly (for some reasons it still needs to run twice) and to start compile. while compiling I run into the problem that qreal are typedef to float when compiling from arm, so I patched qglobal.h to remove the float typedef and set it to double. According to [the documentation](<https://doc.qt.nokia.com/latest/qtglobal.html#qreal-typedef>) this has to do with performance issues. So it might be god to check this in the future. The alternative (cleaner but immensely longer would be to replace every appearance of „double“ with qreal in the full source code of qgis.  
After solving this problem, the compilation went further and got stuck at the compilation of internal spatiallite, since libiconv is not present. Right now I’m trying to compile it but I’ve some errors happening.  
By the end of this week I hope to be able to finally have qgis compiling and to start daling with the UI and GPS.
### _Related_
