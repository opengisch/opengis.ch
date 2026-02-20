---
title: "C++ – Page 2 – OPENGIS.ch"
date: "2012-02-01T00:52:30+01:00"
lastmod: "2020-04-29T18:55:48+02:00"
source: "www.opengis.ch/fr/category/programming/cpp/page/2/index.html"
---

## [QGIS gets Compass support](<../../../../../2012/02/01/qgis-gets-compass-support/index.html> "QGIS gets Compass support")
After implementing GPS support for QGIS on Android I’ve implemented a plugin that reads the internal compass readings and shows the value in a small dock widget. All theese new features are available in the master-alpha4 version and the nightly. Hope you enjoy
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../../2012/02/01/qgis-gets-compass-support/index.html>) 2020-04-29
[](<../../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html> "QGIS on Android gets GPS support")
## [QGIS on Android gets GPS support](<../../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html> "QGIS on Android gets GPS support")
Lately I’ve been working on adding native GPS support to QGIS on Android, here is a short video showing how it works. A big thanks goes to the municipality of Schoten in Belgium which sponsored the development. This functionality is included in the latest nightly builds as of yesterday. GPS[ Read more](<../../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../../2012/01/31/qgis-on-android-gets-gps-support/index.html>) 2020-04-29
## [QGIS on ANDROID talk at the Università degli Studi di Urbino](<../../../../../2011/12/14/qgis-on-android-talk-at-the-universita-degli-studi-di-urbino/index.html> "QGIS on ANDROID talk at the Università degli Studi di Urbino")
Yesterday, thanks to Prof. Mauro De Donatis who invited me, I held a 2h talk at the Università degli Studi di Urbino about QGIS and QGIS on Android. The talk was attended by around 50 students and staff from Computer science, Geology and Ambient sciences. I liked finally holding my[ Read more](<../../../../../2011/12/14/qgis-on-android-talk-at-the-universita-degli-studi-di-urbino/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../../2011/12/14/qgis-on-android-talk-at-the-universita-degli-studi-di-urbino/index.html>) 2020-04-29
## [Creating non-versioned shared libraries for android](<../../../../../2011/11/23/creating-non-versioned-shared-libraries-for-android/index.html> "Creating non-versioned shared libraries for android")
While porting QGIS to android using necessitas I encountered the problem of versioned libs. Android does not support versioned libs and it is not going to. In the first vesions I used rpl -R -e libqgis_core.so.1.9.90 « libqgis_core.sox00x00x00x00x00x00x00 » $APK_LIBS_DIR and similar hacks to remove the version from the libs. But it was[ Read more](<../../../../../2011/11/23/creating-non-versioned-shared-libraries-for-android/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../../2011/11/23/creating-non-versioned-shared-libraries-for-android/index.html>) 2020-04-29
## [QGIS on Android has a proper GUI](<../../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html> "QGIS on Android has a proper GUI")
Today I managed to get QGIS to load all the icons, providers and plugins. The GUI looks very good and quick, it is easy to use with the finger, beside the small arrows hiding multiple icons. Furthermore I discovered that customization works so that we could pre configure qgis to[ Read more](<../../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../../2011/08/18/qgis-on-android-has-a-proper-gui/index.html>) 2020-04-29
## [QGIS on Android](<../../../../../2011/08/17/qgis-on-android/index.html> "QGIS on Android")
Hi all, it is a pleasure to announce that I finally got Quantum GIS to start on an android (3.2) tablet (Asus transformer). I tested as well on a Samsung Galaxy phone with cyanogen mod 7 RC1 and it works a well (with the obvious screen size limitations). Qgis still[ Read more](<../../../../../2011/08/17/qgis-on-android/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../../2011/08/17/qgis-on-android/index.html>) 2020-04-29
## [QGIS Globe runs on Win](<../../../../../2011/08/02/qgis-globe-runs-on-win/index.html> "QGIS Globe runs on Win")
I just set up a win xp virtual box (remember to enable 3D acceleration) and to test out globe on windows. here what I did: Get OSGeo4W installer and run it Choose advanced install Select qgis-dev, osgearth-bin, osg-bin from the desktop packages Select osgeart-dev, osg-dev from libs Run Open Qgis,[ Read more](<../../../../../2011/08/02/qgis-globe-runs-on-win/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 ans ago](<../../../../../2011/08/02/qgis-globe-runs-on-win/index.html>) 2020-04-29
## [Globe is in QGIS Trunk](<../../../../../2011/07/06/globe-is-in-qgis-trunk/index.html> "Globe is in QGIS Trunk")
Last night Pirmin committed our Globe plugin to the QGIS trunk. this means that getting the needed dependencies (see below), building QGIS with -DWITH_GLOBE=ON and activating the plugin its all it takes to get a super globe running on QGIS. Dependencies: sudo apt-get install osgearth osgearth-dev openscenegraph (should be enough)[ Read more](<../../../../../2011/07/06/globe-is-in-qgis-trunk/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../../2011/07/06/globe-is-in-qgis-trunk/index.html>) 2020-04-29
## [QGIS Globe runs in Trunk](<../../../../../2011/05/13/qgis-globe-runs-in-trunk/index.html> "QGIS Globe runs in Trunk")
Thanks to Marco Hugentobler’s idea of using Mutex, QGIS Globe now runs in Trunk, i just created a dev branch at https://github.com/mbernasocchi/Quantum-GIS/tree/mutex-globe and updated the installer script at https://www.opengis.ch/2010/12/01/qgis-globe-plugin-installer-script/ (I haven’t tried it yet but it should work) Cheers Marco
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../../2011/05/13/qgis-globe-runs-in-trunk/index.html>) 2020-04-29
## [GSoC 2011 – I'm in](<../../../../../2011/04/25/gsoc-2011-im-in/index.html> "GSoC 2011 – I'm in")
Guess what appeared inmy inbox at 20.59 today!? Dear Marco, Congratulations! Your proposal « QGIS Mobile » as submitted to « OSGeo – Open Source Geospatial Foundation » has been accepted for Google Summer of Code 2011. Over the next few days, we will add you to the private Google Summer of Code Student[ Read more](<../../../../../2011/04/25/gsoc-2011-im-in/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 ans ago](<../../../../../2011/04/25/gsoc-2011-im-in/index.html>) 2020-04-29
## Pagination des publications
[Précédent](<../../index.html>) [1](<../../index.html>) 2 [3](<../3/index.html>) [Suivant](<../3/index.html>)
