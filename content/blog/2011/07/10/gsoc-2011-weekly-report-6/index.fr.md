---
title: 'GSoC 2011 weekly report #6 – OPENGIS.ch'
date: 2011-07-10
slug: "gsoc-2011-weekly-report-6"
url: "/fr/2011/07/10/gsoc-2011-weekly-report-6/"
source: "www.opengis.ch/fr/2011/07/10/gsoc-2011-weekly-report-6/index.html"
---
This week I started cross compiling qgis and encountered some problems that I could’t solve yet but I’m working on it.  
UPDATE: I just managed to have QGIS to properly configure, by using -DQT_QTUITOOLS_INCLUDE_DIR=/usr/include/qt4/QtUiTools since it appears that necessitas has no QtUiTools yet. I’ll look into it.  
UPPDATE2:or maybe not… got more errors now 🙁  
As well I met with my mentor and we discussed the next steps needted after qgis compiles. We decided which toolbars where needed and that we would start by preconfiguring the install using the new configuration tool. As weel we had a look at which dialogs are not adapted for te screen of a tablet. Finally we had a look at how the GPS can be integrated and identified the useful classes. Here the results.  
**Needed toolbars**  
*Navigation  
*Layer load  
*basic digitizing (add, move nodes)  
*infotool  
*attribute table  
*measurements  
*layer legend  
**GUI Adaptations**  
*Layer properties add scrollbars  
**GPS**  
core/gps  
app/gps  
qgsGpsConnection sub class with parseData() (like nmeaConnection)  
QIODevice subclass listening to android gps api and emitting readyRead()  
extend QgsGpsDetector$  
Next week I’ll focus on getting qgis to cross compile.  
As soon as I’ll be done, I’ll start adding the vertical scrollbars to the gui dialogs that don’t have them (only the layer properties dialog) and then to support the GPS. Finally I’ll configure the toolbars.
### _Related_
