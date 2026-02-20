---
title: 'Globe is in QGIS Trunk – OPENGIS.ch'
date: 2011-07-06
slug: "globe-is-in-qgis-trunk"
url: "/2011/07/06/globe-is-in-qgis-trunk/"
source: "www.opengis.ch/2011/07/06/globe-is-in-qgis-trunk/index.html"
---
Last night Pirmin committed our Globe plugin to the QGIS trunk. this means that getting the needed dependencies (see below), building QGIS with -DWITH_GLOBE=ON and activating the plugin its all it takes to get a super globe running on QGIS.  
Dependencies:  
sudo apt-get install osgearth osgearth-dev openscenegraph (should be enough)  
WARNING: it appears if you don’t install osgearth-dev, then the plugin will compile fine but will not be available for activation in the plugin list.  
Installer: I updated the [Installer Script](</2010/12/01/qgis-globe-plugin-installer-script/index.html> "QGis Globe Plugin installer script") although it is not really needed anymore since you just have to compile QGIS.  
I’m not aware yet of the dependency packaging situation for OSs other than ubuntu.  
Ciao Marco
### _Related_
