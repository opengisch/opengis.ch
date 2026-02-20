---
title: "Master Thesis – OPENGIS.ch"
date: "2012-03-30T11:18:15+02:00"
lastmod: "2020-04-29T16:06:56+02:00"
source: "www.opengis.ch/it/category/master-thesis/index.html"
---

## [QGIS Multiview and globe screenshots](<../../2012/03/30/qgis-multiview-and-globe-screenshots/index.html> "QGIS Multiview and globe screenshots")
This screenshots have been created using the QGIS with the following plugins: Multitemporal and multivariate data visualisation (https://hub.qgis.org/projects/multiview) Scttergram identify (https://hub.qgis.org/projects/scattergramdentify Globe Plugin
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 anni ago](<../../2012/03/30/qgis-multiview-and-globe-screenshots/index.html>) 2020-04-29
## [Globe is in QGIS Trunk](<../../2011/07/06/globe-is-in-qgis-trunk/index.html> "Globe is in QGIS Trunk")
Last night Pirmin committed our Globe plugin to the QGIS trunk. this means that getting the needed dependencies (see below), building QGIS with -DWITH_GLOBE=ON and activating the plugin its all it takes to get a super globe running on QGIS. Dependencies: sudo apt-get install osgearth osgearth-dev openscenegraph (should be enough)[ Read more](<../../2011/07/06/globe-is-in-qgis-trunk/index.html>)
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2011/07/06/globe-is-in-qgis-trunk/index.html>) 2020-04-29
## [QGis Globe runs on a GeoWall using ubuntu natty](<../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html> "QGis Globe runs on a GeoWall using ubuntu natty")
After a day of work in the [GeoWall](<https://en.wikipedia.org/wiki/GeoWall>) lab at the [GIScience Center](<https://www.geo.uzh.ch/en/units/giscience-giva/>) of the Zurich University, I got QGis Globe to work in [QuadBuffer stereo](<https://en.wikipedia.org/wiki/Quad_buffering>) mode with [polarization glasses](<https://en.wikipedia.org/wiki/Polarized_3D_glasses>). [(altro…)](<../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html#more-204>)
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html>) 2020-04-29
## [QGIS Globe runs in Trunk](<../../2011/05/13/qgis-globe-runs-in-trunk/index.html> "QGIS Globe runs in Trunk")
Thanks to Marco Hugentobler’s idea of using Mutex, QGIS Globe now runs in Trunk, i just created a dev branch at https://github.com/mbernasocchi/Quantum-GIS/tree/mutex-globe and updated the installer script at https://www.opengis.ch/2010/12/01/qgis-globe-plugin-installer-script/ (I haven’t tried it yet but it should work) Cheers Marco
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2011/05/13/qgis-globe-runs-in-trunk/index.html>) 2020-04-29
## [Thats it!?](<../../2011/04/29/thats-it/index.html> "Thats it!?")
wow, what a long night, but finally I finished my masterr thesis… 🙂 and now a free wknd!!!!
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2011/04/29/thats-it/index.html>) 2020-04-29
## [QGIS Anwendertag, 6.5., HSR Rapperswil](<../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html> "QGIS Anwendertag, 6.5., HSR Rapperswil")
Am Freitag dem 6. Mai, findet an der Hochschule für Technik Rapperswil das 2. deutschsprachige QGIS Anwendertreffen statt. Quantum GIS (oder kurz QGIS) ist ein benutzerfreundliches Open Source Desktop- und Server-GIS welches sich einer stark wachsenden Anwendergruppe erfreut. Sie finden Infos zu QGIS unter www.qgis.org Nach dem erfolgreichen ersten deutschsprachigen[ Read more](<../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html>)
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html>) 2020-04-29
## [QGis plugins: Multiview and ScattergramIdentify](<../../2011/04/04/qgis-plugins-multiview-and-scattergramidentify/index.html> "QGis plugins: Multiview and ScattergramIdentify")
hi All, If you deal with multivariate, multitemporal and cyclic raster data you might find interesting my multiview plugin. See screenshot of what can be done in terms of different visualizations below. The code still has some minor glitches but it is very well usable (and stable). As well here[ Read more](<../../2011/04/04/qgis-plugins-multiview-and-scattergramidentify/index.html>)
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2011/04/04/qgis-plugins-multiview-and-scattergramidentify/index.html>) 2020-04-29
## [Qgis plugins starter plugin](<../../2010/12/06/qgis-plugins-starter-plugin/index.html> "Qgis plugins starter plugin")
Today I published my first QGis Python plugin. It does allow to configure a list of available plugins actions to execute in one click. It is published in pyqgis contributed repository and the source is developed on My GitHub Cheers Marco
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2010/12/06/qgis-plugins-starter-plugin/index.html>) 2020-04-29
## [QGis Globe Plugin installer script](<../../2010/12/01/qgis-globe-plugin-installer-script/index.html> "QGis Globe Plugin installer script")
Lately, thanks to ma Master Thesis, I’ve been co-working on the Globe Plugin for QGis here my install script for a threaded version of QGis with the Globe Plugin. By now the Globe has stereo 3D support, keyboard navigation (try all the num key), mouse navigation, a gui to control[ Read more](<../../2010/12/01/qgis-globe-plugin-installer-script/index.html>)
By [**Marco Bernasocchi**](<../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../2010/12/01/qgis-globe-plugin-installer-script/index.html>) 2020-04-29
