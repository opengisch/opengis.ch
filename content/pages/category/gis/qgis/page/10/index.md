---
title: "QGIS – Page 10 – OPENGIS.ch"
date: "2011-08-09T03:07:17+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
source: "www.opengis.ch/category/gis/qgis/page/10/index.html"
---

## [GSoC 2011 weekly report #10](<../../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html> "GSoC 2011 weekly report #10")
This week I finally managed to get a test Qt application packaged as an apk file. The application uses the native Proj lib to do some projections conversions. Basically it does the same as what qgis will do just with much more dependencies. The key problem was that necessitas wipes[ Read more](<../../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../../2011/08/09/gsoc-2011-weekly-report-10/index.html>) 2020-04-29
## [QGIS Globe runs on Win](<../../../../../2011/08/02/qgis-globe-runs-on-win/index.html> "QGIS Globe runs on Win")
I just set up a win xp virtual box (remember to enable 3D acceleration) and to test out globe on windows. here what I did: Get OSGeo4W installer and run it Choose advanced install Select qgis-dev, osgearth-bin, osg-bin from the desktop packages Select osgeart-dev, osg-dev from libs Run Open Qgis,[ Read more](<../../../../../2011/08/02/qgis-globe-runs-on-win/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../../2011/08/02/qgis-globe-runs-on-win/index.html>) 2020-04-29
## [GSoC 2011 weekly report #9](<../../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html> "GSoC 2011 weekly report #9")
This week I managed to cross compile qgis and started working on packaging it. See the previous post for more details.
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../../2011/07/29/gsoc-2011-weekly-report-9/index.html>) 2020-04-29
## [QGIS cross compiles using android NDK](<../../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html> "QGIS cross compiles using android NDK")
Finally I managed to cross compile qgis using a NDK r5c standalone toolchain. Currently the scripts to produce the binaries require the necessitas qt source to be present on the host since QtUiTools need to be compiled as well. This should be only until QtUitools is included in necessitas (maybe[ Read more](<../../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../../2011/07/28/qgis-cross-compiles-using-android-ndk/index.html>) 2020-04-29
## [GSoC 2011 weekly report #8](<../../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html> "GSoC 2011 weekly report #8")
This week I fought against libiconv and spatialite that did not want to properly crosscompile. Due to time pressure I decided to temporarly work on it and moved on compiling qgis. I get to the linking part of the process where I get many errors. I m now looking into[ Read more](<../../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../../2011/07/24/gsoc-2011-weekly-report-8/index.html>) 2020-04-29
## [Globe is in QGIS Trunk](<../../../../../2011/07/06/globe-is-in-qgis-trunk/index.html> "Globe is in QGIS Trunk")
Last night Pirmin committed our Globe plugin to the QGIS trunk. this means that getting the needed dependencies (see below), building QGIS with -DWITH_GLOBE=ON and activating the plugin its all it takes to get a super globe running on QGIS. Dependencies: sudo apt-get install osgearth osgearth-dev openscenegraph (should be enough)[ Read more](<../../../../../2011/07/06/globe-is-in-qgis-trunk/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 years ago](<../../../../../2011/07/06/globe-is-in-qgis-trunk/index.html>) 2020-04-29
## [QGIS Globe runs in Trunk](<../../../../../2011/05/13/qgis-globe-runs-in-trunk/index.html> "QGIS Globe runs in Trunk")
Thanks to Marco Hugentobler’s idea of using Mutex, QGIS Globe now runs in Trunk, i just created a dev branch at https://github.com/mbernasocchi/Quantum-GIS/tree/mutex-globe and updated the installer script at https://www.opengis.ch/2010/12/01/qgis-globe-plugin-installer-script/ (I haven’t tried it yet but it should work) Cheers Marco
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 years ago](<../../../../../2011/05/13/qgis-globe-runs-in-trunk/index.html>) 2020-04-29
## [GSoC 2011 – I'm in](<../../../../../2011/04/25/gsoc-2011-im-in/index.html> "GSoC 2011 – I'm in")
Guess what appeared inmy inbox at 20.59 today!? Dear Marco, Congratulations! Your proposal “QGIS Mobile” as submitted to “OSGeo – Open Source Geospatial Foundation” has been accepted for Google Summer of Code 2011. Over the next few days, we will add you to the private Google Summer of Code Student[ Read more](<../../../../../2011/04/25/gsoc-2011-im-in/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 years ago](<../../../../../2011/04/25/gsoc-2011-im-in/index.html>) 2020-04-29
## [QGIS Anwendertag, 6.5., HSR Rapperswil](<../../../../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html> "QGIS Anwendertag, 6.5., HSR Rapperswil")
Am Freitag dem 6. Mai, findet an der Hochschule für Technik Rapperswil das 2. deutschsprachige QGIS Anwendertreffen statt. Quantum GIS (oder kurz QGIS) ist ein benutzerfreundliches Open Source Desktop- und Server-GIS welches sich einer stark wachsenden Anwendergruppe erfreut. Sie finden Infos zu QGIS unter www.qgis.org Nach dem erfolgreichen ersten deutschsprachigen[ Read more](<../../../../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 years ago](<../../../../../2011/04/20/qgis-anwendertag-6-5-hsr-rapperswil/index.html>) 2020-04-29
## [Qgis plugins starter plugin](<../../../../../2010/12/06/qgis-plugins-starter-plugin/index.html> "Qgis plugins starter plugin")
Today I published my first QGis Python plugin. It does allow to configure a list of available plugins actions to execute in one click. It is published in pyqgis contributed repository and the source is developed on My GitHub Cheers Marco
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 years ago](<../../../../../2010/12/06/qgis-plugins-starter-plugin/index.html>) 2020-04-29
## Posts pagination
[Previous](<../9/index.html>) [1](<../../index.html>) … [9](<../9/index.html>) 10 [11](<../11/index.html>) [Next](<../11/index.html>)
