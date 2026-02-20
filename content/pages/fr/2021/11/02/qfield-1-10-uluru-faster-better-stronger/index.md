---
title: "QField 1.10 Uluru: Faster, Better, Stronger – OPENGIS.ch"
author: "Mathieu"
date: "2021-11-02T07:48:00+01:00"
lastmod: "2021-10-26T19:17:41+02:00"
categories:
  - "Faits saillants de QField"
tags:
  - "qgis.org"
source: "www.opengis.ch/fr/2021/11/02/qfield-1-10-uluru-faster-better-stronger/index.html"
---

While OPENGIS.ch’s GeoNinjas are busy getting QFieldCloud ready for primetime, it has not kept them away from concocting a brand new feature-packed QField 1.10 « Uluru ». Most users will find something to fall in love with in this release. From an improved feature form to new digitizing functionalities and quality of live updates.
[Get it now](<https://qfield.org/get>)
## Major feature form improvements
QField’s feature form has received lots of attention during this development cycle. Its user interface and stability have greatly improved, and there are simply too many individual changes to list here.
On the new functionality front, the feature form has gained:
  - An**ordered relation** editor widget allowing users to re-order the children features of a relationship
  - A **complete-as-you-type** mode for value relation editor widget
  - A new **UUID generator** editor widget
  - Support for **“live” default expression** value to be on feature update


## Speed up workflow with new duplicate and move feature(s) actions
QField 1.10 brings in a pair of new useful actions: the duplicate feature(s) and move feature(s). This can speed up work in the field for many surveyors by avoiding potentially lengthy digitizing and attribute filling processes in favour of quickly duplicating what’s already done whenever possible.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2021/10/move_duplicate6d1b.jpg?resize=750%2C407&ssl=1)
## Vertex digitizing logger
Conducting quality assurance (QA) reviews from work done in the field with QField has just gotten a lot better thanks to the brand new vertex digitizing logger. When enabled, each vertex entered while digitizing new features or editing preexisting geometries are logged as point features onto a ‘digitizing logs’ layer. Each point feature added has access to snapping result context, position context including horizontal and vertical accuracy, and more. This allows for data reviewers to get a fuller picture of how geometries were built.
## Quality of life improvements
Quite a few improvements have landed in QField 1.10 which should improve users’ experience. To list a few:
  - To save battery, QField will now**automatically dim the screen** backlight after a period of inactivity, allowing users to conduct longer tracking sessions before running out of power
  - Tracking settings are now remembered and **sub-meter minimum distance constraint** allowed
  - The map scale bar now avoids degrees and instead **automatically converts units into meters**
  - Opening an individual point dataset will **automatically setup and show feature labels** ; for other geometry types, users can show labels via a new checkbox in the layer item properties panel


![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2021/10/labelstracking-1225f.jpg?resize=606%2C542&ssl=1)
## QField speaks many languages
Thanks to community efforts, QField has been translated into a growing number of languages. However, the user interface language adopted by QField was until now hard-coded to match that of the device onto which QField was running.
Starting with QField 1.10, users are able to customize the language used by going to the settings panel.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2021/10/russianjapanese225f.jpg?resize=606%2C542&ssl=1)
## Updates to foundational libraries
Time was spent during this development cycle to update a large number of libraries powering up QField, which is now running against QGIS 3.22, gdal 3.3.2, PROJ 8.1.1. This has resulted in increased stability as well as speed gains in a number of scenarios.
## The Future is almost here
We are working hard to get QFieldClour open to the public, we currently have more than 2/3 of our waiting list actively using it. In the next 2-3 weeks we will invite all waiting users and then open up Beta registrations to the public.Meanwhile, we have also been working on fully supporting iOS, Windows and Linux. Simply go to <https://qfield.org/get> and start using QField immediately on your favourite device.
### _Related_
