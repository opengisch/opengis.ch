---
title: "Programming – Page 2 – OPENGIS.ch"
date: "2017-12-01T08:18:07+01:00"
lastmod: "2020-04-29T16:05:13+02:00"
source: "www.opengis.ch/category/programming/page/2/index.html"
---

## [Interlis translation](<../../../../2017/12/01/interlis-translation/index.html> "Interlis translation")
Lately, I have been confronted with the need of translating Interlis files (from French to German) to use queries originally developed for German data. I decided to create an automated convertor for Interlis (version 1) Transfer Format files (.ITF) based on the existing cadastral data model from the Swiss confederation[ Read more](<../../../../2017/12/01/interlis-translation/index.html>)
By [**Mario Baranzini**](<../../../../author/marioba/index.html> "Mario Baranzini"), [8 years ago](<../../../../2017/12/01/interlis-translation/index.html>) 2020-04-29
## [Best practices for writing Python QGIS Expression Functions](<../../../../2017/05/10/best-practices-for-writing-python-qgis-expression-functions/index.html> "Best practices for writing Python QGIS Expression Functions")
Recently there have been some questions and discussions about python based expression functions and how parameters like usesGeometry need to be used. So I thought I’d quickly write down how this works. There is some intelligence If the geometry or a column is passed in as a parameter you do not[ Read more](<../../../../2017/05/10/best-practices-for-writing-python-qgis-expression-functions/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [9 years ago](<../../../../2017/05/10/best-practices-for-writing-python-qgis-expression-functions/index.html>) 2020-04-29
## [QGIS Expressions Engine: Performance boost](<../../../../2017/05/02/qgis-expressions-engine-performance-boost/index.html> "QGIS Expressions Engine: Performance boost")
Expressions in QGIS are more and more widely used for all kinds of purposes. For example the recently introduced geometry generators allow drawing awesome effects with modified feature geometries on the fly. The last days at the QGIS developer meeting 2017, I spent some time looking into and improving the[ Read more](<../../../../2017/05/02/qgis-expressions-engine-performance-boost/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [9 years ago](<../../../../2017/05/02/qgis-expressions-engine-performance-boost/index.html>) 2020-04-29
## [QGIS2 compatibility plugin](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html> "QGIS2 compatibility plugin")
Lately I’ve been spending time porting a bigger plugin from QGIS 2.8 to 3 while maintaining 2.8 compatibility. You can find it at https://github.com/opengisch/qgis2compat/ and https://plugins.qgis.org/plugins/qgis2compat/ One code to rule them all. My target was to have to edit the source code as little as possible to simulate a lazy[ Read more](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 years ago](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html>) 2020-04-29
## [Updating PyQt signals that use lambda in QGIS with 2to3](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html> "Updating PyQt signals that use lambda in QGIS with 2to3")
Just for the sake of documenting things, when running qgis 2to3 on a plugin I encountered a tricky situation regarding signals. MYQGISDIR/scripts/2to3 -f signals -w my/plugin/path The original code: extra_arg = “my test argument” QObject.connect( action, SIGNAL( “triggered()”), lambda extra_arg=my_arg: show_extra_arg(extra_arg)) def do_load_project(extra_arg): print extra_arg # “my test argument” The[ Read more](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 years ago](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>) 2020-04-29
## [Using threads in QGIS python plugins](<../../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html> "Using threads in QGIS python plugins")
Here an example on how to work with threads in a consistent and clean manner in QGIS python plugins
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 years ago](<../../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html>) 2020-04-29
## [QGIS: Qt5 and Python3 migration, current state](<../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html> "QGIS: Qt5 and Python3 migration, current state")
Behind the scenes a lot has happened to get ready for Qt5 and Python3. On the same codebase that is becoming the next release QGIS 2.16. This is really a great thing since we can focus work on a single master branch and I’m very happy that we got so[ Read more](<../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>) 2020-04-29
## [Increasing the stability of processing algorithms](<../../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html> "Increasing the stability of processing algorithms")
Processing just got a new testing framework to improve the long-term stability of this important plugin. And you can help to improve it, even if you are not a software developer! This is yet another piece in our never-stopping crusade to improve the stability and quality of the best desktop GIS on[ Read more](<../../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html>) 2020-04-29
## [Passing android Intents to Qt](<../../../../2015/12/03/passing-android-intents-to-qt/index.html> "Passing android Intents to Qt")
Working on QField I had the necessity of passing values from the QtActivity.java to the Qt cpp world, here how I did it using an Intent that is sent to the QtActivity (the one you should not edit that comes with Qt). For much more information see this post series. hopefully[ Read more](<../../../../2015/12/03/passing-android-intents-to-qt/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [10 years ago](<../../../../2015/12/03/passing-android-intents-to-qt/index.html>) 2020-04-29
[](<../../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html> "QGIS Crowdfunding: 2.5D Rendering")
## [QGIS Crowdfunding: 2.5D Rendering](<../../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html> "QGIS Crowdfunding: 2.5D Rendering")
![2.5D rendering](../../../../wp-content/uploads/2015/10/title.png)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html>) 2020-04-29
## Posts pagination
[Previous](<../../index.html>) [1](<../../index.html>) 2 [3](<../3/index.html>) … [6](<../6/index.html>) [Next](<../3/index.html>)
