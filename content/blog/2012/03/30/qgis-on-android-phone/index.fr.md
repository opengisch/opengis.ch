---
title: 'QGIS on Android Phone – OPENGIS.ch'
date: 2012-03-30
slug: "qgis-on-android-phone"
url: "/fr/2012/03/30/qgis-on-android-phone/"
source: "www.opengis.ch/fr/2012/03/30/qgis-on-android-phone/index.html"
---
At FOSSGIS I was asked to try to install qgis on a very small android phone, I think it was a 3.2″ screen. the install went smoothly after making some space but then the problems came because of the small screen.  
Eventually I thought about setting a smaller font size to make the UI scale more, the problem was that it was impossible to get to the size setting because the UI was to big.  
As a workaround I created a QGIS.conf file with this content  
`[General] IconSize=32  
fontPointSize=4`and pushed it to the device using the [android debug bridge](<https://developer.android.com/guide/developing/tools/adb.html>) like this:  
`adb push myQGISConfigFile.conf /data/data/org.qgis.qgis/files/Settings/QuantumGIS/QGIS.conf`  
On the next start the whole gui was nice and small and fitted the screen.  
Here some screenshots from my Samsung galaxy 9000 with 4″ screen and a video demonstrating digitising (with pen and fingers), GPS, compass and zooming on the phone.  
[![QGIS map view running on a Samsung Galaxy S Android phone](./P20120330131311465b.png)](</i0.wp.com/www.opengis.ch/wp-content/uploads/2012/02/P20120330131311eb45.png?ssl=1>) [![QGIS interface scaled down to fit a Samsung Galaxy S screen](./P20120330123638465b.png)](</i0.wp.com/www.opengis.ch/wp-content/uploads/2012/02/P20120330123638eb45.png?ssl=1>)  

This video shows QGIS on a Samsung I9000 Galaxy S Android smartphone with 4.0″ screen. the point size in settings->option->general is set to 4

{{< blog-video src="https://player.vimeo.com/video/39473397" title="Vimeo video 39473397" >}}

[https://vimeo.com/39473397](<https://vimeo.com/39473397>)

### _Related_
