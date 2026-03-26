---
title: 'QField 3.0 “Amazonia” is here – Feature-packed and super slick. – OPENGIS.ch'
date: 2023-10-24
slug: "qfield-3-0-amazonia-is-here"
url: "/fr/2023/10/24/qfield-3-0-amazonia-is-here/"
source: "www.opengis.ch/fr/2023/10/24/qfield-3-0-amazonia-is-here/index.html"
image: "/i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/30splasha86e.png"
---
We’re so excited and proud of this latest QField version that we’ve opted for a major 3.0 version update. 
[Get it now](<https://qfield.app/>)
Shipped with many new features and built with the latest generation of Qt’s cross-platform framework, this new chapter marks an important milestone for the most powerful open-source field GIS solution.
![QField 3.0 Amazonia release graphic highlighting the major update](https://lh5.googleusercontent.com/tN3P-TFu7O2_hcEwShJYmQeneSN9oddAMQ64xkdoSr5Yn9MVZ-v9iBCkRo-3Sb7Ya1AGZSKID-_mG1PbR3sFma6ST66Zi0bqmm9-xqMnIZx_C5vNWz-3wp7TwoQADLWhtpT0KF5ghZz33hP23xKcap4)
## Main highlights
Upon launching this new version of QField, users will be greeted by a revamped recent projects list featuring shiny map canvas thumbnails. While this is one of the most obvious UI improvements, countless interface tweaks and harmonization have occurred. From the refreshed dark theme to the further polishing of countless widgets, QField has never looked and felt better.
The top search bar has a new functionality that allows users to look for features within the currently active vector layer by matching any of its attributes against a given search term. Users can also refine their searches by specifying a specific attribute. The new functionality can be triggered by typing the ‘f’ prefix in the search bar followed by a string or number to retrieve a list of matching features. When expanding it, a new list of functionalities appears to help users discover all of the tools available within the search bar.
QField’s tracking has also received some love. A **new erroneous distance safeguard** setting has been added, which, when enabled, will dictate the tracker not to add a new vertex if the distance between it and the previously added vertex is greater than a user-specified value. This aims at preventing “spikes” of poor position readings during a tracking session. QField is now also capable of resuming a tracking session after being stopped. When resuming, tracking will reuse the last feature used when first starting, allowing sessions interrupted by battery loss or momentary pause to be continued on a single line or polygon geometry. 
{{< blog-video src="https://videopress.com/embed/W2nwrWjt" title="QField 3.0 release video" >}}

[https://videopress.com/embed/W2nwrWjt](<https://videopress.com/embed/W2nwrWjt>)

On the feature form front, QField has gained **support for feature form text widgets,** a new read-only type introduced in QGIS 3.30**,** which allows users to create expression-based text labels within complex feature form configurations. In addition, **relationship-related form widgets now allow for zooming to children/parent** features within the form itself.
To enhance digitizing work in the field, QField now makes it **possible to turn snapping on and off** through a new snapping button on top of the map canvas when in digitizing mode. When a project has enabled advanced snapping, the dashboard’s legend item now showcases snapping badges, allowing users to **toggle snapping for individual vector layers**. 
{{< blog-video src="https://videopress.com/embed/2LMsUg9l" title="QField 3.0 snapping capabilities" >}}

[https://videopress.com/embed/2LMsUg9l](<https://videopress.com/embed/2LMsUg9l>)

In addition, digitising lines and polygons by using the volume up/down hardware keys on devices such as smartphones is now possible. This can come in handy when digitizing data in harsh conditions where gloves can make it harder to use a touch screen. 
While we had to play favourites in describing some of the new functionalities in QField, we’ve barely touched the surface of this feature-packed release. Other major additions include support for **Near-Field Communication (NFC) text tag reading** and a new geometry editor’s eraser tool to delete part of lines and polygons as you would with a pencil sketch using an eraser.
Thanks to [Deutsches Archäologisches Institut](<https://www.dainst.org/dai/meldungen>), [Groupements forestiers Québec](<https://groupementsforestiers.quebec/>), [Amsa](<https://www.amsa.it/cittadini>), and [Kanton Luzern](<https://www.luzern.ch/>) for sponsoring these enhancements. 
## Quality of life improvements
Starting with this new version, the scale bar overlay will now respect projects’ distance measurement units, allowing for **scale bars in imperial and nautical units**.
QField now offers a **rendering quality setting which, at the cost of a slightly reduced visual quality, results in faster rendering speeds and lower memory usage**. This can be a lifesaver for older devices having difficulty handling large projects and helps save battery life.
Vector tile layer support has been improved with the automated download of missing fonts and the possibility of toggling label visibility. This pair of changes makes this resolution-independent layer type much more appealing.
**On iOS, layouts are now printed by QField as PDF documents** instead of images. While this was the case for other platforms, it only became possible on iOS recently after work done by one of our ninjas in QGIS itself.
Many thanks to [DB Fahrwgdienste](<https://fahrweg.dbnetze.com/fahrweg-de>) for sponsoring stabilization efforts and fixes during this development cycle.
## Qt 6, the latest generation of the cross-platform framework powering QField
Last but not least, QField 3.0 is now built against Qt 6. This is a significant technological milestone for the project as this means we can fully leverage the latest technological innovations into this cross-platform framework that has been powering QField since day one.
On top of the new possibilities, QField benefited from years of fixes and improvements, including better integration with Android and iOS platforms. In addition, the positioning framework in Qt 6 has been improved with awareness of the newer GNSS constellations that have emerged over the last decade.
## Forest-themed release names
![Forest landscape used to introduce the Amazonia release theme](./qfield3f4e5.jpg)
Forests are critical in climate regulation, biodiversity preservation, and economic sustainability. Beginning with QField 3.0 “Amazonia” and throughout the 3.X’s life cycle, we will choose forest names to underscore the importance of and advocate for global forest conservation. 
As always, we hope you enjoy this new release. Happy field mapping!
### _Related_
