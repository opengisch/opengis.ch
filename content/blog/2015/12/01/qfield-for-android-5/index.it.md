---
title: 'QField for Android 5 – OPENGIS.ch'
date: 2015-12-01
slug: "qfield-for-android-5"
url: "/it/2015/12/01/qfield-for-android-5/"
source: "www.opengis.ch/it/2015/12/01/qfield-for-android-5/index.html"
---
[![QField app on Google Play](https://i0.wp.com/developer.android.com/images/brand/en_app_rgb_wo_45.png?resize=129%2C45&ssl=1)](<https://play.google.com/store/apps/details?id=ch.opengis.qfield>)
QField app
[![QField Karma edition app on Google Play](https://i0.wp.com/developer.android.com/images/brand/en_app_rgb_wo_45.png?resize=129%2C45&ssl=1)](<https://play.google.com/store/apps/details?id=ch.opengis.qfieldkarmaedition>)
QField Karma edition app
It’s done, finally we managed to get rid of Ministro so that we finally can say, QField runs on any android from 4.0.3 (ICS). This makes as of today (according to [google](<https://developer.android.com/about/dashboards/index.html>)) 96% of the android installations worldwide. Eventually we want to settle to 4.3 (JB) as minimum to allow us using certain features and avoiding [one known issue](<https://github.com/opengisch/QField/issues/6>), but for now it would mean cutting of another 25% of the users.  
**So as of today it is: 4.0.3 (Ice cream sandwich API 15) is the required minimal Android version to run QField and Android 4.3 (Jelly Bean API 18) is the suggested minimal version.**  
We tested with 4.4, 5.0.1 and 5.1 but we haven’t had the chance to get our hands on an Android 6 so if you can, let us know how it works.  
But adding support for android 5 isn’t the only great news, during the process we also:
  - Reintroduced WMS support
  - Removed ministro dependency. All libs are now bundled so that the installation is as simple as possible
  - Drastically reduced total download size from 300MB+ to 36MB
  - Updated libs to QGIS 2.13 (https://github.com/qgis/QGIS/commit/6b3eddd)


We would like to thank to the City of Vevey and the QGIS hack fest Gran Canaria for supporting the development of this critical feature.  
QField is an Open Source project led by OPENGIS.ch LLC, more [information](</android-gis/qfield/index.html>), the [source code](</qfield.opengis.ch/repo>) and a possibility to donate to the project can be found on the [QField page](</android-gis/qfield/index.html>) (preferred) or by buying the QField for [QGIS Karma edition app](</qfield.opengis.ch/karma>).  
Also if you need a specific feature, [contact us](</contact/index.html>) to sponsor its development.
### _Related_
