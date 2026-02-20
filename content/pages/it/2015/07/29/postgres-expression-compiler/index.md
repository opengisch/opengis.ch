---
title: "Postgres Expression Compiler for QGIS – OPENGIS.ch"
author: "Matthias Kuhn"
date: "2015-07-29T12:20:30+02:00"
lastmod: "2020-04-29T16:05:41+02:00"
categories:
  - "Uncategorised"
tags:
  - "qgis.org"
source: "www.opengis.ch/it/2015/07/29/postgres-expression-compiler/index.html"
---

# Performance
This project is all about performance of QGIS with a postgres/postgis database.  
A lot of people have QGIS connected to postgres/postgis (if you don’t: it’s a great combination in the open source geo stack). Databases are really optimized for querying. They keep indexes of geometries to be able to find them faster, they keep indexes of attributes to filter faster – and finally they often run on powerful servers.  
QGIS tries to be smart enough to make use of this additional information. So whenever a map canvas is being rendered it asks the database only for features in this area. But if it’s about other attributes, QGIS filters by them locally. This means if you have a list of all the cities in the world and only want the capitals, QGIS will get the list with all the cities from the database, check for every city if it’s a capital. If it’s not, it will discard it, if it is it will use it. That’s terribly slow and postgres itself could do it much faster.  
That’s where the postgres expression compiler comes into play. It is able to compile QgsExpressions (an SQL dialect) to postgres filter queries (another SQL dialect) and sends the converted SQL to the server if it is able to create matching SQL. If not it will gracefully fallback to the (slow) local evaluation.
# Where it can be used
When building enterprise scaled applications dealing with large amounts of data and only requiring a subset of it is a really common task.  
Let’s start with some cartography. Think of a small country-side village with some beautiful old houses and a lovely small river making its way through the nearby forest. This village is in a bigger district which has some other cities (some of them more, some of them less worth a visit) and this district is just one out of several others which together form a whole kingdom. One day the king asks a map for him to be drawn of his kingdom. And the man who has been tasked the job settles out and finds our nice small village. It’s a hard job for him to decide how to visualize it. Should he draw all this beautiful old houses? And the river? And the forest? He tried hard to do it but he couldn’t make the lines thin enough to fit everything on that piece of paper on which he had to paint the other 258 villages. After hours of trying he decided to put a small dot for the village there. He could not even label it with the name.  
In cartography the task of going to a smaller map scale is called generalization. There are various possibilities to help with this task, an important one is: leave out things. While QGIS cannot replace the whole generalization task which the king’s cartographer had done, it can still help you as you zoom out and in on the map canvas and show certain features only at certain scales. To configure this, you can use the _rule based renderer_. This let’s you define combinations of filters, scales and symbology. At small scales we will usually have only a subset of features being rendered. And this is where the expression compiler comes into play and helps you to not even let the server send them through the network but already filter all the small cities out before sending them to QGIS.  
On an example real world application (the QGEP project) the rendering speed on small scales has been increased by a factor of 3. This number is highly specific to this particular environment. The database server runs on the same machine (network latency, network throughput, CPU and memory shared between QGIS and postgres…) and can be better or worse, depending on the environment and the number of features which can be filtered on the server.
# The current status
It is currently in experimental state so it’s opt-in. Look for it in Options => Data Sources => Data Source Handling.
# For developers
If you are a developer and want to make use of it, it’s really simple. All you need to do is to use QgsFeatureRequest::setFilterExpression and make sure the setting is turned on.
    
    layer.getFeatures( QgsFeatureRequest().setFilterExpression( '"size" = \'capital\'' ) )
# Thanks
I would like to thank the [Swiss QGIS usergroup](<https://www.qgis.ch/en>) who made this project possible. It is amazing how this group helps to push QGIS forward.
### _Related_
