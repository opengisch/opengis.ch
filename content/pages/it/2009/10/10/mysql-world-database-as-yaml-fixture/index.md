---
title: "MySql World Database as YAML fixture – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2009-10-10T09:36:28+02:00"
lastmod: "2020-04-29T16:08:00+02:00"
categories:
  - "Web Development"
tags:
  - "qgis.org"
  - "Symfony"
source: "www.opengis.ch/it/2009/10/10/mysql-world-database-as-yaml-fixture/index.html"
---

For Symfony application I’m developing I needed all the Region separated by continent (7 continents model). I converted the MySql World Database (https://dev.mysql.com/doc/world-setup/en/world-setup.html) to a YAML NestedSet fixture file.  
I just had to make 4 minor changes to it:  
– rename the 3 continents that had region with the same name name (North America, South America, Antarctica)  
– rename the Micronesia/Caribbean region to Micronesia-Caribbean.  
thats’ all, enjoy the file [Region.yml](<../../../../../wp-content/uploads/2009/10/Region.html>)  
Marco
### _Related_
