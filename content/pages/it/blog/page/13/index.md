---
title: "Blog – Pagina 13 – OPENGIS.ch"
date: "2016-09-19T16:01:39+02:00"
lastmod: "2020-04-29T16:05:13+02:00"
source: "www.opengis.ch/it/blog/page/13/index.html"
---

## [QGIS2 compatibility plugin](<../../../2016/09/19/qgis2-compatibility-plugin/index.html> "QGIS2 compatibility plugin")
Lately I’ve been spending time porting a bigger plugin from QGIS 2.8 to 3 while maintaining 2.8 compatibility. You can find it at https://github.com/opengisch/qgis2compat/ and https://plugins.qgis.org/plugins/qgis2compat/ One code to rule them all. My target was to have to edit the source code as little as possible to simulate a lazy or busy coder that has to upgrade his/her plugins. Lots of work has already gone into 2.14 to support PyQt 4 and 5 with the[ Read more](<../../../2016/09/19/qgis2-compatibility-plugin/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 anni ago](<../../../2016/09/19/qgis2-compatibility-plugin/index.html>) 2020-04-29
## [Updating PyQt signals that use lambda in QGIS with 2to3](<../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html> "Updating PyQt signals that use lambda in QGIS with 2to3")
Just for the sake of documenting things, when running qgis 2to3 on a plugin I encountered a tricky situation regarding signals. MYQGISDIR/scripts/2to3 -f signals -w my/plugin/path The original code: extra_arg = “my test argument” QObject.connect( action, SIGNAL( “triggered()”), lambda extra_arg=my_arg: show_extra_arg(extra_arg)) def do_load_project(extra_arg): print extra_arg # “my test argument” The generated code: extra_arg = “test_arg” action.triggered.connect( lambda extra_arg=my_arg: show_extra_arg(extra_arg)) def do_load_project(extra_arg): print extra_arg # False so in do_load_project we get False instead of “my test[ Read more](<../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 anni ago](<../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>) 2020-04-29
## [Using threads in QGIS python plugins](<../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html> "Using threads in QGIS python plugins")
Here an example on how to work with threads in a consistent and clean manner in QGIS python plugins
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 anni ago](<../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html>) 2020-04-29
## [QGIS: Qt5 and Python3 migration, current state](<../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html> "QGIS: Qt5 and Python3 migration, current state")
Behind the scenes a lot has happened to get ready for Qt5 and Python3. On the same codebase that is becoming the next release QGIS 2.16. This is really a great thing since we can focus work on a single master branch and I’m very happy that we got so far with this approach already. Testing At OPENGIS.ch we have put a huge effort into getting the Travis CI test infrastructure to test our code with Qt5[ Read more](<../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>) 2020-04-29
## [Prepare your plugins for QGIS 3](<../../../2016/03/23/prepare-your-plugins-for-qgis-3/index.html> "Prepare your plugins for QGIS 3")
QGIS 3 is not yet there and there is still plenty of time to prepare and migrate. But I thought I would give some advice about things that you can keep in mind while working on your plugins to make your life easier when you will have to actually do the migration. It’s mostly about making your code prepared for Python 3 and PyQt5. Do not use star imports Don’t do from PyQt4.QtCore import *[ Read more](<../../../2016/03/23/prepare-your-plugins-for-qgis-3/index.html>)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2016/03/23/prepare-your-plugins-for-qgis-3/index.html>) 2020-04-29
## [Increasing the stability of processing algorithms](<../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html> "Increasing the stability of processing algorithms")
Processing just got a new testing framework to improve the long-term stability of this important plugin. And you can help to improve it, even if you are not a software developer! This is yet another piece in our never-stopping crusade to improve the stability and quality of the best desktop GIS on the market. Processing You probably know processing. If you don’t: processing is the number one plugin to enable after every QGIS installation. It offers a[ Read more](<../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html>)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2016/02/04/increasing-the-stability-of-processing-algorithms/index.html>) 2020-04-29
[](<../../../2015/12/10/geometry-generator-symbology/index.html> "Geometry generator symbology")
## [Geometry generator symbology](<../../../2015/12/10/geometry-generator-symbology/index.html> "Geometry generator symbology")
Say hello to geometry generators, a new way to use expression syntax to generate a geometry on the fly during the rendering process. 
![](../../../../wp-content/uploads/2015/12/139aea6c-9b5a-11e5-9a07-dc0a982cc4af.png)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2015/12/10/geometry-generator-symbology/index.html>) 2020-04-29
## [QField Documentation](<../../../2015/12/10/qfield-documentation/index.html> "QField Documentation")
After getting QField up and running in Android 5, we felt it was time to start documenting how QField works, we started documenting how to install and use QField. We also added a section on how to handle your data to get them on QField. It is all pretty basic, but it dose give some hints. You can find the documentation here: https://qfield.org/docs/ As QField’s source code the docs are opensourced (on github) and we look[ Read more](<../../../2015/12/10/qfield-documentation/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [10 anni ago](<../../../2015/12/10/qfield-documentation/index.html>) 2020-04-29
## [Passing android Intents to Qt](<../../../2015/12/03/passing-android-intents-to-qt/index.html> "Passing android Intents to Qt")
Working on QField I had the necessity of passing values from the QtActivity.java to the Qt cpp world, here how I did it using an Intent that is sent to the QtActivity (the one you should not edit that comes with Qt). For much more information see this post series. hopefully this will be helpful to someone. private void startQtActivity() { String dotqgis2_dir = “Test dotqgis2_dir”; String share_dir = “Test share_dir”; // forward to startQtActivity and[ Read more](<../../../2015/12/03/passing-android-intents-to-qt/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [10 anni ago](<../../../2015/12/03/passing-android-intents-to-qt/index.html>) 2020-04-29
## [QField for Android 5](<../../../2015/12/01/qfield-for-android-5/index.html> "QField for Android 5")
It’s done, QField runs on any android from 4.0.3 (ICS) with a seamless installing experience. We suggest using at least Android 4.3 
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [10 anni ago](<../../../2015/12/01/qfield-for-android-5/index.html>) 2020-04-29
[](<../../../2015/12/01/qfield-for-android-5/index.html> "QField for Android 5")
## Paginazione degli articoli
[Precedenti](<../12/index.html>) [1](<../../index.html>) … [12](<../12/index.html>) 13 [14](<../14/index.html>) … [23](<../23/index.html>) [Successivi](<../14/index.html>)
