---
title: 'Updating PyQt signals that use lambda in QGIS with 2to3 – OPENGIS.ch'
date: 2016-09-11
slug: "updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3"
url: "/2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/"
source: "www.opengis.ch/2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html"
---
Just for the sake of documenting things, when running qgis 2to3 on a plugin I encountered a tricky situation regarding signals.
    
    MYQGISDIR/scripts/2to3 -f signals -w my/plugin/path
The original code:
    
    extra_arg = "my test argument"
    QObject.connect(
      action,
      SIGNAL( "triggered()"),
      lambda extra_arg=my_arg: show_extra_arg(extra_arg))
    def do_load_project(extra_arg):
      print extra_arg # "my test argument"
    
The generated code:
    
    extra_arg = "test_arg"
    action.triggered.connect(
      lambda extra_arg=my_arg: show_extra_arg(extra_arg))
    def do_load_project(extra_arg):
      print extra_arg # False
so in _do_load_project_ we get False instead of _“my test argument”_ , why?  
well due to a subtle difference in the generated code. in the original code we had the signature _triggered()_ which has no arguments, so in our lambda _extra_arg_ gets passed _my_arg_.  
in the generated code,  _triggered_ actually has an optional param _checked_ [1] which if emitted gets passed to _extra_arg_ causing the problem.  
The correct code (note the additional argument in the lambda definition)
    
    extra_arg = "test_arg"
    action.triggered.connect(
      lambda checked, extra_arg=my_arg: show_extra_arg(extra_arg))
    def do_load_project(extra_arg):
      print extra_arg # False
some reference:  
[0] <https://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html>  
[1] <https://doc.qt.io/qt-4.8/qaction.html#triggered>
### _Related_
