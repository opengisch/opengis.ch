---
title: 'QGIS data providers and map canvas – OPENGIS.ch'
date: 2011-08-19
slug: "qgis-data-providers-and-map-canvas"
url: "/it/2011/08/19/qgis-data-providers-and-map-canvas/"
source: "www.opengis.ch/it/2011/08/19/qgis-data-providers-and-map-canvas/index.html"
---
After finishing with the gui(see previous post) i started testing the data providers.reading and writing shp files always ends in an app crash. Loading rasters, wms and gpx seems to work but the mapcanvas is never drawn. I have to investigate why. But probably it has to do with the draw used in qgis. The properties are there and get updated, but the canvasstays black. The same happens with decorations plugins like north arrow and copyright.  
Next things i want to check is the shape error and the canvas problem. Then probably sqlite and gps.  
Ciao Marco
### _Related_
