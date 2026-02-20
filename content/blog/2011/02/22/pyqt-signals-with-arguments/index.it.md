---
title: 'PyQT signals with arguments – OPENGIS.ch'
date: 2011-02-22
slug: "pyqt-signals-with-arguments"
url: "/it/2011/02/22/pyqt-signals-with-arguments/"
source: "www.opengis.ch/it/2011/02/22/pyqt-signals-with-arguments/index.html"
---
so , here a snippet on how to use the different types of signals in PyQt:
  - connect a signal from C++  
`QObject.connect(self.sender, SIGNAL("signalName( Arg1TYPE, Arg2TYPE )"), self.slot)`
  - connect a signal from Python  
`QObject.connect(self.sender, SIGNAL("signalName" ), self.slot )`
  - emit a signal in Python  
`self.emit( SIGNAL( "signalName" ), arg1, arg2 )`
  - emit a signal in c++  
`emit signalName( arg1, arg2 );`


more: [https://www.eurion.net/python-snippets/snippet/Connecting%20signals%20and%20slots.html](<https://www.eurion.net/python-snippets/snippet/Connecting signals and slots.html>)
### _Related_
