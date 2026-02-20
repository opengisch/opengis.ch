---
title: "Marco Bernasocchi – Page 13 – OPENGIS.ch"
date: "2011-05-19T18:26:04+02:00"
lastmod: "2020-04-29T16:07:59+02:00"
source: "www.opengis.ch/fr/author/mbernasocchi/page/13/index.html"
---

## [QGis Globe runs on a GeoWall using ubuntu natty](<../../../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html> "QGis Globe runs on a GeoWall using ubuntu natty")
After a day of work in the [GeoWall](<https://en.wikipedia.org/wiki/GeoWall>) lab at the [GIScience Center](<https://www.geo.uzh.ch/en/units/giscience-giva/>) of the Zurich University, I got QGis Globe to work in [QuadBuffer stereo](<https://en.wikipedia.org/wiki/Quad_buffering>) mode with [polarization glasses](<https://en.wikipedia.org/wiki/Polarized_3D_glasses>). [(suite…)](<../../../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html#more-204>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/05/19/qgis-globe-runs-on-a-geowall-using-ubuntu-natty/index.html>) 2020-04-29
## [QGIS Globe runs in Trunk](<../../../../2011/05/13/qgis-globe-runs-in-trunk/index.html> "QGIS Globe runs in Trunk")
Thanks to Marco Hugentobler’s idea of using Mutex, QGIS Globe now runs in Trunk, i just created a dev branch at https://github.com/mbernasocchi/Quantum-GIS/tree/mutex-globe and updated the installer script at https://www.opengis.ch/2010/12/01/qgis-globe-plugin-installer-script/ (I haven’t tried it yet but it should work) Cheers Marco
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/05/13/qgis-globe-runs-in-trunk/index.html>) 2020-04-29
## [Thats it!?](<../../../../2011/04/29/thats-it/index.html> "Thats it!?")
wow, what a long night, but finally I finished my masterr thesis… 🙂 and now a free wknd!!!!
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/04/29/thats-it/index.html>) 2020-04-29
## [GSoC 2011 – I'm in](<../../../../2011/04/25/gsoc-2011-im-in/index.html> "GSoC 2011 – I'm in")
Guess what appeared inmy inbox at 20.59 today!? Dear Marco, Congratulations! Your proposal « QGIS Mobile » as submitted to « OSGeo – Open Source Geospatial Foundation » has been accepted for Google Summer of Code 2011. Over the next few days, we will add you to the private Google Summer of Code Student[ Read more](<../../../../2011/04/25/gsoc-2011-im-in/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/04/25/gsoc-2011-im-in/index.html>) 2020-04-29
## [QGIS Anwendertag, 6.5., HSR Rapperswil](<../../../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html> "QGIS Anwendertag, 6.5., HSR Rapperswil")
Am Freitag dem 6. Mai, findet an der Hochschule für Technik Rapperswil das 2. deutschsprachige QGIS Anwendertreffen statt. Quantum GIS (oder kurz QGIS) ist ein benutzerfreundliches Open Source Desktop- und Server-GIS welches sich einer stark wachsenden Anwendergruppe erfreut. Sie finden Infos zu QGIS unter www.qgis.org Nach dem erfolgreichen ersten deutschsprachigen[ Read more](<../../../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html>) 2020-04-29
## [QGis plugins: Multiview and ScattergramIdentify](<../../../../2011/04/04/qgis-plugins-multiview-and-scattergramidentify/index.html> "QGis plugins: Multiview and ScattergramIdentify")
hi All, If you deal with multivariate, multitemporal and cyclic raster data you might find interesting my multiview plugin. See screenshot of what can be done in terms of different visualizations below. The code still has some minor glitches but it is very well usable (and stable). As well here[ Read more](<../../../../2011/04/04/qgis-plugins-multiview-and-scattergramidentify/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/04/04/qgis-plugins-multiview-and-scattergramidentify/index.html>) 2020-04-29
## [PyQT signals with arguments](<../../../../2011/02/22/pyqt-signals-with-arguments/index.html> "PyQT signals with arguments")
so , here a snippet on how to use the different types of signals in PyQt: connect a signal from C++ QObject.connect(self.sender, SIGNAL(« signalName( Arg1TYPE, Arg2TYPE ) »), self.slot) connect a signal from Python QObject.connect(self.sender, SIGNAL(« signalName » ), self.slot ) emit a signal in Python self.emit( SIGNAL( « signalName » ), arg1, arg2 ) emit[ Read more](<../../../../2011/02/22/pyqt-signals-with-arguments/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2011/02/22/pyqt-signals-with-arguments/index.html>) 2020-04-29
## [Qgis plugins starter plugin](<../../../../2010/12/06/qgis-plugins-starter-plugin/index.html> "Qgis plugins starter plugin")
Today I published my first QGis Python plugin. It does allow to configure a list of available plugins actions to execute in one click. It is published in pyqgis contributed repository and the source is developed on My GitHub Cheers Marco
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2010/12/06/qgis-plugins-starter-plugin/index.html>) 2020-04-29
## [QGis Globe Plugin installer script](<../../../../2010/12/01/qgis-globe-plugin-installer-script/index.html> "QGis Globe Plugin installer script")
Lately, thanks to ma Master Thesis, I’ve been co-working on the Globe Plugin for QGis here my install script for a threaded version of QGis with the Globe Plugin. By now the Globe has stereo 3D support, keyboard navigation (try all the num key), mouse navigation, a gui to control[ Read more](<../../../../2010/12/01/qgis-globe-plugin-installer-script/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2010/12/01/qgis-globe-plugin-installer-script/index.html>) 2020-04-29
## [Ubuntu 10.10 maverick meerkat on eeepc 1005 HA](<../../../../2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/index.html> "Ubuntu 10.10 maverick meerkat on eeepc 1005 HA")
WOW, today I realized that Ubuntu 10.10 maverick meerkat was out and that I missed it by couple of days… bad me!!! (btw you have to select « normal updates » instead of « long term release » in your update manager’s settings). After the update my little eeepc lookt great, and everything worked[ Read more](<../../../../2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/index.html>)
By [**Marco Bernasocchi**](<../../index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/index.html>) 2020-04-29
## Pagination des publications
[Précédent](<../12/index.html>) [1](<../../index.html>) … [12](<../12/index.html>) 13 [14](<../14/index.html>) [Suivant](<../14/index.html>)
