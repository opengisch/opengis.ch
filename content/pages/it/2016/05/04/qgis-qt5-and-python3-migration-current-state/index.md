---
title: "QGIS: Qt5 and Python3 migration, current state – OPENGIS.ch"
author: "Matthias Kuhn"
date: "2016-05-04T10:50:18+02:00"
lastmod: "2020-04-29T16:05:13+02:00"
categories:
  - "C++"
  - "GIS"
  - "Programming"
  - "Python"
  - "QGIS"
tags:
  - "qgis.org"
source: "www.opengis.ch/it/2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html"
---

Behind the scenes a lot has happened to get ready for Qt5 and Python3. On the same codebase that is becoming the next release QGIS 2.16. This is really a great thing since we can focus work on a single master branch and I’m very happy that we got so far with this approach already.
## Testing
At OPENGIS.ch we have put a huge effort into getting the Travis CI test infrastructure to test our code with Qt5 and Python 3. This gives us confidence that we don’t have regressions introduced once we declare Qt5 and Python 3 to be default. At the time of writing we have [177 tests passing on Qt5/Python3](<https://travis-ci.org/qgis/QGIS/jobs/127728328>) vs [211 tests on Qt4/Python2](<https://travis-ci.org/qgis/QGIS/jobs/127728327>). Most of the missing tests are caused by a single issue (PyQt5 and NULL, see below).
## Migration tool
There is a [script 2to3](<https://github.com/qgis/QGIS/blob/master/scripts/2to3>) that takes care of migrating “old” python code to portable code. That means, after running this tool on your python code it is compatible with PyQt4, PyQt5, Python2 and Python3.  
It uses the [future library for python compatibility](<https://python-future.org/>) and a custom qgis.PyQt module that takes care of importing from the appropriate PyQt4 or PyQt5 modules.  
This can be done on build for core plugins with a new cmake option We do this on our (travis) CI builds when building for Qt5.  
Please note that the tool does a very good job (kudos to Jürgen at this point) but it cannot do everything, so plugin developers will also need to test in-depth and we’ll need to also prepare a migration guide that lists things to manually take care of.
## PyQt5
PyQt5 – just like Qt5 – is very similar to PyQt4. This is a good thing since it makes it easier to write portable code.  
The main issue which we have found so far is [the lack of PyQtNullVariant](<https://www.riverbankcomputing.com/pipermail/pyqt/2016-April/037300.html>) and without this we don’t have proper support for NULL values. Definitely a no-go. Or we use to a different handling of attributes which would mean major manual updates to all plugins, IMHO also a no-go. The good thing is, there are good chances that PyQtNullVariant will be re-introduced in PyQt 5.7 but this means that our minimum Qt requirement will be Qt 5.7 which in turn means that older linux distros will be locked into using old QGIS versions.
## Qt5
A lot of these updates have been done some time ago already. Qt5 (without python involved) runs quite painless. [QField](<https://opengisch.github.io/QField-docs/>) wouldn’t run without it.
## What’s left to do
  - Finding a solution for the PyQt5 NULL issue
  - Check which tests still fail after the issue has been fixed
  - [Implement many other changes](<https://github.com/qgis/qgis3.0_api/issues>) which we want to work on before being able to ship QGIS with a version number 3.0.
  - Writing a migration guide


## Building
If you are curious to test it, make sure you have the build dependencies (recent distros ship with Qt5 and Python3, so just apt-get, dnf, pacman or however them from the repositories)  
Here the commands I use to build and run from the build directory (so you can do this on a system with other QGISes installed as well)
    
    $ cmake -DENABLE_QT5=ON -DPORT_PLUGINS=ON ../QGIS
    $ make
    $ ./output/bin/qgis
    
### _Related_
