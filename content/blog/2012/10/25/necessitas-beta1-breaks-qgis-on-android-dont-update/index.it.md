---
title: 'Necessitas Beta1 \"breaks\" qgis on android – don''t update – OPENGIS.ch'
date: 2012-10-25
slug: "necessitas-beta1-breaks-qgis-on-android-dont-update"
url: "/it/2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update/"
source: "www.opengis.ch/it/2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update/index.html"
---
Hi all, it has been a while since my last post, and foremost QGIS on android release. I’m very sorry. I’ve been working hard on another project ([inasafe.org](<https://inasafe.org/>)) that toke up all my time since we just launched version 1.0.  
So now to the real problem, necessitas (the android Qt port) has had a sweet update that adds a lot of nice things (like native look and feel) to Qt apps. The only problem is that it has a grave [bug](<https://bugs.kde.org/show_bug.cgi?id=304240>) that makes the new shiny thing bad for QGIS. Basically there is no second level menu bars anymore. Yes exactly, every item like view>panels>gps can’t be selected. Basically all plugins, all panels and more can’t be selected with the new necessitas, So If QGIS is the only Qt app you have on your device, DON’T let ministro update it’s libraries.  
I’ve of course already discussed with the maintainer of necessitas and he promised me to have this fixed in the next release. Meanwhile, I’m looking into making a temporary package that includes the old Qt libraries.  
I’m sorry for the issue and really hope to solve this quickly but as everybody I need do do paid work as well to support my other developments, so if you can, give a nice poke to that donate button 😉  
ciao 
### _Related_
