---
title: "Adapting doctrineexport.grt.lua to symfony standards – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2009-09-17T16:35:43+02:00"
lastmod: "2020-04-29T16:08:00+02:00"
categories:
  - "Web Development"
tags:
  - "qgis.org"
  - "Symfony"
source: "www.opengis.ch/fr/2009/09/17/adapting-doctrineexport-grt-lua-to-symfony-standards/index.html"
---

Using Mysql workbench to visually design a data model for a symfony application is pretty cool. Thanks to the guys of <https://code.google.com/p/mysql-workbench-doctrine-plugin/> you can export the model to a YAML file ready for Doctrine.  
the only problem I found using version 0.36 is that classes names are not in UpperCamelCase but in lowerCameCase and that if you have a table column that starts wit id (like idea) it gets cut to id (issue report: <https://code.google.com/p/mysql-workbench-doctrine-plugin/issues/detail?id=15>). so here my two modifications of the script to behave the way I want.  
At the end of function buildTableName(s) add:
    
    if ( string.sub(s, 1, 2) == 'sf' or  string.sub(s, 1, 2) == 'Sf') then
          -- same as lcfirst
          s = string.lower(string.sub(s, 1, 2)) .. string.sub(s, 3, #s)
        else
          s = ucfirst(s)
        end
        return s
Comment out the content of the renameIdColumns function
    
    function renameIdColumns(s)
       -- s = string.gsub(s, "(id%w+)", function(v)
       --      return "id"
       --    end)
       return s
    end
    
### _Related_
