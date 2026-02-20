---
title: 'Best practices for writing Python QGIS Expression Functions – OPENGIS.ch'
date: 2017-05-10
slug: "best-practices-for-writing-python-qgis-expression-functions"
url: "/de/2017/05/10/best-practices-for-writing-python-qgis-expression-functions/"
source: "www.opengis.ch/de/2017/05/10/best-practices-for-writing-python-qgis-expression-functions/index.html"
---
Recently there have been some questions and discussions about python based expression functions and how parameters like usesGeometry need to be used. So I thought I’d quickly write down how this works.
# There is some intelligence
If the geometry or a column is passed in as a parameter you do not need to request it manually, you can even specify explicitly that you do not require the geometry or a column here.
    
    @qgsfunction(args='auto', group='Custom', usesGeometry=False, referencedColumns=[])
    def my_buffer(geom, distance, feature, parent):
        return geom.buffer(distance, 5)
We can still call it within an expression by writing
    
    my_buffer($geometry, "impact_radius")
The expression engine will do the appropriate thing and request the geometry and attributes automatically.
# Hardcoded parameters
We can also write the function the following way. The difference is, that we will only ever be able to use it for this layer because it’s not portable. But sometimes there might be a good reason for doing that.
    
    @qgsfunction(args='auto', group='Custom', usesGeometry=True, referencedColumns=['impact_radius'])
    def impact_radius_buffered_geometry(feature, parent):
        if feature.geometry():
            return feature.geometry().buffer(feature['impact_radius'], 5)
        else:
            return None
Notice that the geometry and columns were mentioned in two places. The decorator (usesGeometry=True and referencedColumns=[‚impact_radius‘]) as well as within the function body with feature.geometry() and feature[‚impact_radius‘] .  
Also notice that it was checked if the feature actually does have a geometry. with if feature.geometry() . It’s a common pitfall, that sometimes features with a NULL geometry suddenly make expression functions fail. It’s very easy to oversee this in development and then hard to track down in a production environment. Better stay on the safe side.  
When you call this from an expression, you will call it the following way.
    
    impact_radius_buffered_geometry()
# Require all attributes
Sometimes it’s required to actually make sure that you have all attributes available. In this case you can specify [QgsFeatureRequest.ALL_ATTRIBUTES].  
The following expression generates a list of all attributes of a feature, separated by a , . For this it obviously requires access to all attributes:
    
    @qgsfunction(args='auto', group='Custom', referencedColumns=[QgsFeatureRequest.ALL_ATTRIBUTES])
    def concat_attributes(feature, parent):
        my_string = ', '.join([str(attr) for attr in feature.attributes()])
        return my_string
# Break it down
  - If you don’t hardcode attributes or the geometry inside your function, specify usesGeometry=False, referencedColumns=[] . As a rule of thumb, prefer to do things this way, this makes it easier to reuse functions in the future.
  - If you do hardcode geometry or attributes, specify this manually.


### _Related_
