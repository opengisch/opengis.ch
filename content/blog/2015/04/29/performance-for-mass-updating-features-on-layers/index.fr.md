---
title: 'Performance for mass updating features – OPENGIS.ch'
date: 2015-04-29
slug: "performance-for-mass-updating-features-on-layers"
url: "/fr/2015/04/29/performance-for-mass-updating-features-on-layers/"
source: "www.opengis.ch/fr/2015/04/29/performance-for-mass-updating-features-on-layers/index.html"
---
This post discusses how to improve the performance of pyqgis code that updates a lot of features by a factor of more than 10.
## Scenario
Once in a while you want to modify every feature of a layer. Or a bunch of features meeting certain criteria. That’s pretty straightforward. Let’s say you want to shift them all in x direction by 0.1 and in y direction by 0.3 (map units).  
Straightforward and easy to do:
    
    delta_x = 0.1
    delta_y = 0.3
    vlayer = iface.activeLayer()
    u = QgsVectorLayerEditUtils( vlayer )
    for f in vlayer.getFeatures():
      u.translateFeature( f.id(), delta_x, delta_y )
## Benchmarking
This code however may take a considerable amount of time. Python has a nice little module called timeit that helps you to benchmark by running the code a couple of times. [1]  
Let’s do it 5 times
    
    from timeit import *
    delta_x = 0.1
    delta_y = .3
    vlayer = iface.activeLayer()
    u = QgsVectorLayerEditUtils( vlayer )
    def funct():
        for f in vlayer.getFeatures():
            u.translateFeature( f.id(), delta_x, delta_y )
    t = Timer( stmt=funct )
    print t.timeit( number = 5 )
On a postgres layer with ~11000 features this gives me 25 seconds the first run and then constantly around 17 seconds (refer to [1]).  
I wouldn’t be writing about it if we couldn’t do any better 🙂
## Optimize the feature request
The first step to optimization is, that we actually only need the feature id and nothing else. So we modify the request like this:
    
    from timeit import *
    delta_x = 0.1
    delta_y = .3
    vlayer = iface.activeLayer()
    u = QgsVectorLayerEditUtils( vlayer )
    def funct():
        for f in vlayer.getFeatures( QgsFeatureRequest().setFlags( QgsFeatureRequest.NoGeometry ).setSubsetOfAttributes([]) ):
            u.translateFeature( f.id(), delta_x, delta_y )
    t = Timer( stmt=funct )
    print t.timeit(number = 5 )
    
Nice, down to ~14 seconds.
## Grouping in the undo stack
But we can optimize it even further. Remember that you can undo things in QGIS? That’s a nice feature but it isn’t for free. For every operation that is done an item is put onto the « undo stack », a quite costly operation. But for our operation we don’t really need a separate undo operation for every feature on the layer, we can just have one « grouped » undo item instead. That’s not only faster but also more user-friendly. For this, QgsVectorLayer offers the methods beginEditCommand( text ) and endEditCommand() .
    
    from timeit import *
    delta_x = 0.1
    delta_y = .3
    vlayer = iface.activeLayer()
    u = QgsVectorLayerEditUtils( vlayer )
    def funct():
        # Start an undo block
        vlayer.beginEditCommand( 'Translating all features' )
        for f in vlayer.getFeatures( QgsFeatureRequest().setFlags( QgsFeatureRequest.NoGeometry ).setSubsetOfAttributes([]) ):
            u.translateFeature( f.id(), delta_x, delta_y )
        # End the undo block
        vlayer.endEditCommand()
    t = Timer( stmt=funct )
    print t.timeit( number = 5 )
    
And the winner is… down to ~1.38 seconds. We have just cut down the time to execute this by a factor of 10!  
Remember this whenever you do bulk updates on a layer.
## Working with the provider
Another very common approach is not to use the vector layer at all and directly work on the provider. This completely bypasses the undo stack. When doing this, what you need to take care of is that QGIS itself sends update operations to the backend in groups when saving a vector layer. If you bypass the vector layer you will have to do this yourself or you will send a new request to your backend for each and every feature which is especially slow if network latency is involved. Therefore the QgsVectorDataProvider object has methods that take more than a single change at once: changeAttributeValues and changeGeometryValues . Use these wisely.  
[1] Benchmarking is hard to get right and influenced by many parameters. The main problem is that it is impossible to completely separate the signal from the noise. In this example, the first time iterating the layer took considerably longer, this could have been caused by a cold cache, the postgres connection pool still being empty, system load… When benchmarking, always treat the results with a good portion of reluctance.
### _Related_
