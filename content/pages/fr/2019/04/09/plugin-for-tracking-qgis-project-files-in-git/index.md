---
title: "Plugin for tracking QGIS project files in git – OPENGIS.ch"
author: "Matthias Kuhn"
date: "2019-04-09T15:53:45+02:00"
lastmod: "2020-04-29T18:57:33+02:00"
categories:
  - "QGIS"
  - "Uncategorised"
tags:
  - "qgis.org"
source: "www.opengis.ch/fr/2019/04/09/plugin-for-tracking-qgis-project-files-in-git/index.html"
---

We often have QGIS project files that are part of a customer project. To be able to manage versions of these project files or have multiple people working on it, they are managed inside a git repository.
This is however not easy, because with every save of a project file, thousands of lines change, even if the real change is minimal. Like a change of a layer name.
![](https://i0.wp.com/opengis.ch/wp-content/uploads/2019/04/image.png?resize=750%2C254&ssl=1)Current situation 
This blows up the git repository for no reason. And worse: it makes it impossible to review changes, because the signal to noise ratio is horrible.
OPENGIS.ch has just released a shiny jewel to make your life easier. The [Trackable QGIS Projects plugin](<https://github.com/opengisch/qgis_trackable_project_files>) will automatically rewrite the saved project into a much more stable format.
![](../../../../../../i2.wp.com/new.opengis.ch/wp-content/uploads/2019/04/image-11a1d.png?fit=664%2C421&ssl=1)Understandable changes thanks to the trackable QGIS plugin
Just download the plugin, install it and you are done. No user interface available, no configuration needed.  

### _Related_
