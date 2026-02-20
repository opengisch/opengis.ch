---
title: "QGIS data providers and map canvas – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2011-08-19T23:43:52+02:00"
lastmod: "2021-06-06T08:45:45+02:00"
categories:
  - "Android QGIS"
  - "GIS"
  - "GSoC 2011"
  - "QGIS"
tags:
  - "Android"
  - "Android NDK"
  - "Android Qt"
  - "qgis.org"
source: "www.opengis.ch/it/2011/08/19/qgis-data-providers-and-map-canvas/index.html"
---

After finishing with the gui(see previous post) i started testing the data providers.reading and writing shp files always ends in an app crash. Loading rasters, wms and gpx seems to work but the mapcanvas is never drawn. I have to investigate why. But probably it has to do with the draw used in qgis. The properties are there and get updated, but the canvasstays black. The same happens with decorations plugins like north arrow and copyright.  
Next things i want to check is the shape error and the canvas problem. Then probably sqlite and gps.  
Ciao Marco
### _Related_
