---
title: 'QGIS on android ALPHA 5 – OPENGIS.ch'
date: 2012-02-23
slug: "qgis-on-android-alpha-5"
url: "/it/2012/02/23/qgis-on-android-alpha-5/"
source: "www.opengis.ch/it/2012/02/23/qgis-on-android-alpha-5/index.html"
---
Hi all couple of days ago I pushed a new alpha version of qgis for android on android.qgis.org  
This release includes all the goodies that I got to implement lately including: – right click support through longClick – shape file support – gps – compass – android 4 support – partial hardware optimization for armV7a (most newish devices have it) – no debug symbols  
I m very happy with this release because it adresses and fixes all high priority bugs. Adding support for a armv7a optimized whit no debug symbols build increased greatly the speed of the app. The package you need to install is the same and includes both armv5 and armv7a code. Android will take care of using the correct version. Gdal and geos are not available yet in v7a code so the v5 versions will be loaded. I couldn’t test much the v7 code so I hope you can help me testing it. As well, on www.opengis.ch I published many videos and screenshots of qgis. As usual, please remember if you can (or if you know anybody that could) that sponsoring would help a lot implementing some more great features.  
Ciao
### _Related_
