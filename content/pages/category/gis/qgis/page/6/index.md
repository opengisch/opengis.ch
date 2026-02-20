---
title: "QGIS – Page 6 – OPENGIS.ch"
date: "2016-09-19T16:01:39+02:00"
lastmod: "2020-04-29T16:05:13+02:00"
source: "www.opengis.ch/category/gis/qgis/page/6/index.html"
---

## [QGIS2 compatibility plugin](<../../../../../2016/09/19/qgis2-compatibility-plugin/index.html> "QGIS2 compatibility plugin")
Lately I’ve been spending time porting a bigger plugin from QGIS 2.8 to 3 while maintaining 2.8 compatibility. You can find it at https://github.com/opengisch/qgis2compat/ and https://plugins.qgis.org/plugins/qgis2compat/ One code to rule them all. My target was to have to edit the source code as little as possible to simulate a lazy[ Read more](<../../../../../2016/09/19/qgis2-compatibility-plugin/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 years ago](<../../../../../2016/09/19/qgis2-compatibility-plugin/index.html>) 2020-04-29
## [Updating PyQt signals that use lambda in QGIS with 2to3](<../../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html> "Updating PyQt signals that use lambda in QGIS with 2to3")
Just for the sake of documenting things, when running qgis 2to3 on a plugin I encountered a tricky situation regarding signals. MYQGISDIR/scripts/2to3 -f signals -w my/plugin/path The original code: extra_arg = “my test argument” QObject.connect( action, SIGNAL( “triggered()”), lambda extra_arg=my_arg: show_extra_arg(extra_arg)) def do_load_project(extra_arg): print extra_arg # “my test argument” The[ Read more](<../../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 years ago](<../../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>) 2020-04-29
## [Using threads in QGIS python plugins](<../../../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html> "Using threads in QGIS python plugins")
Here an example on how to work with threads in a consistent and clean manner in QGIS python plugins
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 years ago](<../../../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html>) 2020-04-29
## [QGIS: Qt5 and Python3 migration, current state](<../../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html> "QGIS: Qt5 and Python3 migration, current state")
Behind the scenes a lot has happened to get ready for Qt5 and Python3. On the same codebase that is becoming the next release QGIS 2.16. This is really a great thing since we can focus work on a single master branch and I’m very happy that we got so[ Read more](<../../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>)
By [**Matthias Kuhn**](<../../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>) 2020-04-29
## [Increasing the stability of processing algorithms](<../../../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html> "Increasing the stability of processing algorithms")
Processing just got a new testing framework to improve the long-term stability of this important plugin. And you can help to improve it, even if you are not a software developer! This is yet another piece in our never-stopping crusade to improve the stability and quality of the best desktop GIS on[ Read more](<../../../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html>)
By [**Matthias Kuhn**](<../../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html>) 2020-04-29
[](<../../../../../2015/12/10/geometry-generator-symbology/index.html> "Geometry generator symbology")
## [Geometry generator symbology](<../../../../../2015/12/10/geometry-generator-symbology/index.html> "Geometry generator symbology")
Say hello to geometry generators, a new way to use expression syntax to generate a geometry on the fly during the rendering process. 
![](../../../../../wp-content/uploads/2015/12/139aea6c-9b5a-11e5-9a07-dc0a982cc4af.png)
By [**Matthias Kuhn**](<../../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../../2015/12/10/geometry-generator-symbology/index.html>) 2020-04-29
[](<../../../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html> "QGIS Crowdfunding: 2.5D Rendering")
## [QGIS Crowdfunding: 2.5D Rendering](<../../../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html> "QGIS Crowdfunding: 2.5D Rendering")
![2.5D rendering](../../../../../wp-content/uploads/2015/10/title.png)
By [**Matthias Kuhn**](<../../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html>) 2020-04-29
[](<../../../../../2015/08/18/qgis-welcome-page/index.html> "QGIS Welcome Page")
## [QGIS Welcome Page](<../../../../../2015/08/18/qgis-welcome-page/index.html> "QGIS Welcome Page")
Whenever you start QGIS you basically do it because? Right, because you need to do GIS work. Ah, how I love rhetorical questions to start a post. And most of the time one continues to work on a QGIS project which he has prepared before. For me 99% of the time, I[ Read more](<../../../../../2015/08/18/qgis-welcome-page/index.html>)
By [**Matthias Kuhn**](<../../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../../2015/08/18/qgis-welcome-page/index.html>) 2020-04-29
## [Syntactic sugar for PyQGIS](<../../../../../2015/08/12/with-edit-layer/index.html> "Syntactic sugar for PyQGIS")
PyQGIS now supports a nice new addition for handling edit sessions in layers. This way, changes get committed automatically at the end of a successful (python) edit session.
    
    with edit(layer):
        do your changes here()
    
By [**Matthias Kuhn**](<../../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../../2015/08/12/with-edit-layer/index.html>) 2020-04-29
[](<../../../../../2015/06/15/qfield-in-the-wild/index.html> "QField in the wild")
## [QField in the wild](<../../../../../2015/06/15/qfield-in-the-wild/index.html> "QField in the wild")
QField Experimental is out, after a couple of months of requirements gathering, private early alpha testing and foremost tons of emails requesting access to the testes group we decided today to put the current BETA version in the playstore. This means that from now on you can install QField just like any other android app by using the playstore.
[![QField app on Google Play](https://developer.android.com/images/brand/en_app_rgb_wo_45.png)](<https://play.google.com/store/apps/details?id=ch.opengis.qfield>)
By [**Marco Bernasocchi**](<../../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [11 years ago](<../../../../../2015/06/15/qfield-in-the-wild/index.html>) 2020-04-29
## Posts pagination
[Previous](<../5/index.html>) [1](<../../index.html>) … [5](<../5/index.html>) 6 [7](<../7/index.html>) … [11](<../11/index.html>) [Next](<../7/index.html>)
