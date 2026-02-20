---
title: "PyQt – OPENGIS.ch"
date: "2018-06-22T13:30:25+02:00"
lastmod: "2020-08-06T20:52:57+02:00"
source: "www.opengis.ch/fr/category/programming/python/pyqt/index.html"
---

[![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2018/06/pexels-wendy-van-zyl-1212179-scaleda86e.jpg?resize=360%2C240&ssl=1)](<../../../../2018/06/22/threads-in-pyqgis3/index.html> "Using Threads in PyQGIS3")
## [Using Threads in PyQGIS3](<../../../../2018/06/22/threads-in-pyqgis3/index.html> "Using Threads in PyQGIS3")
While porting a plugin to QGIS3 I decided to also move all it’s threading infrastructure to QgsTasks. Here three possible variants to implement this.the first uses the static method QgsTask.fromFunction and is simpler to use. A great quick solution. If you want need control you can look at the second[ Read more](<../../../../2018/06/22/threads-in-pyqgis3/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [8 ans ago](<../../../../2018/06/22/threads-in-pyqgis3/index.html>) 2020-08-06
## [Porting QGIS plugins to API v3 – Strategy and tools](<../../../../2018/04/13/porting-qgis-plugins-to-api-v3-strategy-and-tools/index.html> "Porting QGIS plugins to API v3 – Strategy and tools")
The Release of QGIS 3.0 was a great success and with the first LTR (3.4) scheduled for release this fall, it is now the perfect time to port your plugins to the new API. QGIS 3.0 is the first major release since September 2013 when QGIS 2.0 was released. During[ Read more](<../../../../2018/04/13/porting-qgis-plugins-to-api-v3-strategy-and-tools/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [8 ans ago](<../../../../2018/04/13/porting-qgis-plugins-to-api-v3-strategy-and-tools/index.html>) 2020-04-29
## [QGIS2 compatibility plugin](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html> "QGIS2 compatibility plugin")
Lately I’ve been spending time porting a bigger plugin from QGIS 2.8 to 3 while maintaining 2.8 compatibility. You can find it at https://github.com/opengisch/qgis2compat/ and https://plugins.qgis.org/plugins/qgis2compat/ One code to rule them all. My target was to have to edit the source code as little as possible to simulate a lazy[ Read more](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 ans ago](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html>) 2020-04-29
## [Updating PyQt signals that use lambda in QGIS with 2to3](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html> "Updating PyQt signals that use lambda in QGIS with 2to3")
Just for the sake of documenting things, when running qgis 2to3 on a plugin I encountered a tricky situation regarding signals. MYQGISDIR/scripts/2to3 -f signals -w my/plugin/path The original code: extra_arg = « my test argument » QObject.connect( action, SIGNAL( « triggered() »), lambda extra_arg=my_arg: show_extra_arg(extra_arg)) def do_load_project(extra_arg): print extra_arg # « my test argument » The[ Read more](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 ans ago](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>) 2020-04-29
