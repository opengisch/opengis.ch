---
title: "Syntactic sugar for PyQGIS – OPENGIS.ch"
author: "Matthias Kuhn"
date: "2015-08-12T15:58:17+02:00"
lastmod: "2020-04-29T16:05:41+02:00"
categories:
  - "Programming"
  - "Python"
  - "QGIS"
tags:
  - "qgis.org"
source: "www.opengis.ch/fr/2015/08/12/with-edit-layer/index.html"
---

If you are a python coder you probably already know the with-statement.  
If yes, you can directly jump to the with edit-section.  
If not, here’s a short summing up.  
If you want to edit a file you can do:
    
    f = open('file', 'w')
    do_some_changes_to(f)
    f.write()
This is a bad idea. The file is not closed and [you should always do that](<https://stackoverflow.com/questions/11095474/why-do-i-have-to-use-close-to-close-a-file>). We can easily add that, right?
    
    f = open('file', 'w')
    do_some_changes_to(f)
    f.write()
    f.close()
Now what happens if do_some_changes_to(f) causes an exception? f.close() is never called.  
You may remember something called finally. That can be appended to a try-block and will be executed in the end no-matter-what.
    
    try:
        f = open('file', 'w')
        do_some_changes_to(f)
        f.write()
    finally:
        f.close()
That’s a lot of code for something that was originally very slick. That’s where the with-statement comes into play:
    
    with open('file', 'w') as f:
        do_some_changes_to(f)
        f.write()
It does the very same thing. Plus it is easier to read and faster to write than the whole try–finally-block.  
Now QGIS has the same for editing layers since today (read: shipped with version 2.12).
## with edit(layer)
Instead of writing
    
    try:
        layer.startEditing()
        layer.updateFeature(f)
        layer.commitChanges()
    except SomeError:
        layer.rollBack()
You can do:
    
    with edit(layer):
        layer.addFeature(...)
        layer.updateFeatures(...)
If all goes well, the changes will be saved persistently to the datasource without any call to commitChanges() .  
If any exception occurs, the changes will be rolled back. So like for the with -statement for files: it is easier to read, easier to write and it is comparable to a [database transaction](<https://en.wikipedia.org/wiki/Database_transaction>): Commit everything in the end or nothing at all if an error happens. How cool is that!  
Plus you will get a python exception if something went wrong in committing (normally you will have to check the return value of layer.commitChanges() )and who does that anyway?
    
    try:
        with edit(layer):
            layer.addFeature(...)
            layer.updateFeatures(...)
    except QgsEditException as err:
        print repr(err)
If you are writing your own .py files you will have to
    
    from qgis.core import edit, QgsEditException
And a final note since I am already on the topic of modifying data in persistent backends:  
**Avoid using the dataProvider() methods!**
    
    layer.dataProvider().addFeatures()
    layer.dataProvider().deleteFeatures()
    layer.dataProvider().changeAttributeValues()
    layer.dataProvider().changeGeometryValues()
  - You cannot undo them easily
  - They generate one request per call what may reduce performance
  - They do not emit internal signals for map redraws and other refreshes of the user interface
  - They do not take uncommitted changes into account so the python changes will get overwritten by the user when he commits the layer changes


There is a theoretical advantage of slightly more control over how the communication with the backend happens (e.g. how many features are sent per request). But this is hardly ever required in real life unless you are working with really, really, really huge datasets.
### _Related_
