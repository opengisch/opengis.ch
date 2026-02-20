---
title: 'Prepare your plugins for QGIS 3 – OPENGIS.ch'
date: 2016-03-23
slug: "prepare-your-plugins-for-qgis-3"
url: "/it/2016/03/23/prepare-your-plugins-for-qgis-3/"
source: "www.opengis.ch/it/2016/03/23/prepare-your-plugins-for-qgis-3/index.html"
---
QGIS 3 is not yet there and there is still plenty of time to prepare and migrate.  
But I thought I would give some advice about things that you can keep in mind while working on your plugins to make your life easier when you will have to actually do the migration. It’s mostly about making your code prepared for Python 3 and PyQt5.
## Do not use star imports
Don’t do
    
    from PyQt4.QtCore import *
some things have been been moved between different modules and it is easier to rewrite the code if it is known, where classes come from. So instead do
    
    from PyQt4.QtCore import (
        QDate,
        QTime,
        QDateTime,
        QVariant
    )
IDE’s make this task easier.
## Only cast to string where required
One of the things that changed between Python 2 and Python 3 is the handling of strings. Most notably the change in semantics of the type str . In Python 3 a str is a string. In Python 2 it is not, instead it is an array of bytes, a real string in Python 2 is unicode , the two things can often be used interchangeably, but no longer when you want to handle special characters like ä, ñ or even more modern characters like ✓ (you didn’t know that this is a character? It actually is part of modern character sets). In Python 3 there is also a pure array of bytes. It’s called bytes .  
If you want to get too much trouble, don’t do any unrequired extra conversions to unicode or str . Often python converts things automatically for you and you don’t need to be explicit about it.  
If you know a text will be in a variable  
instead of
    
    myWidget.setText(str(my_text))
use
    
    myWidget.setText(my_text)
  
There will still be situations where you need to be explicit, but in such cases you will get exceptions that tell you about it.
## Write unit tests
If you already have a good code coverage of unit tests you are in a comfortable position. Because you can easily try different tools that help to migrate the code and test the resulting code by running the unit tests in a PyQt5/Python 3 version of QGIS. This makes trial and error much, much faster than manually testing through the whole plugin again and again and again.  
You will even be able to run the tests on a Python 2 and a Python 3 version of QGIS and maintain a plugin that is compatible with the old and the new world.
## Read more about conversion from Python2 to Python3
<https://python3porting.com/noconv.html> and google for it. While reading it, forget about any python version <2.7 or 3.0 – 3.3. These versions are outdated, need not be supported and just make a developers life harder.  

### _Related_
