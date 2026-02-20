---
title: "Blog – Pagina 14 – OPENGIS.ch"
date: "2015-11-02T11:33:32+01:00"
lastmod: "2020-04-29T16:05:41+02:00"
source: "www.opengis.ch/it/blog/page/14/index.html"
---

[](<../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html> "QGIS Crowdfunding: 2.5D Rendering")
## [QGIS Crowdfunding: 2.5D Rendering](<../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html> "QGIS Crowdfunding: 2.5D Rendering")
![2.5D rendering](../../../../wp-content/uploads/2015/10/title.png)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html>) 2020-04-29
## [SpaceMouse in Ubuntu 15.04](<../../../2015/10/14/spacemouse-in-ubuntu-15-04/index.html> "SpaceMouse in Ubuntu 15.04")
While preparing some 3D scenes for an exibition I discovered the SpaceMouse by 3dconnexion. A neat device we plan on installing in front of a projected globe. To get it to run in Ubuntu first get the drivers from www.3dconnexion.eu/service/drivers.html then sudo apt-get install libmotif3 mkdir -p /tmp/3D3dxware-linux cd /tmp/3D3dxware-linux cp ~/Downloads/3dxware-linux-v1-8-0.x86_64.tar.gz /tmp/3D3dxware-linux tar -xf 3dxware-linux-v1-8-0.x86_64.tar.gz sudo ./install-3dxunix.sh answer yes, 4, yes. That’s it, you might get an error saying: “Red Hat EL 7 currently[ Read more](<../../../2015/10/14/spacemouse-in-ubuntu-15-04/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [10 anni ago](<../../../2015/10/14/spacemouse-in-ubuntu-15-04/index.html>) 2020-04-29
[](<../../../2015/08/18/qgis-welcome-page/index.html> "QGIS Welcome Page")
## [QGIS Welcome Page](<../../../2015/08/18/qgis-welcome-page/index.html> "QGIS Welcome Page")
Whenever you start QGIS you basically do it because? Right, because you need to do GIS work. Ah, how I love rhetorical questions to start a post. And most of the time one continues to work on a QGIS project which he has prepared before. For me 99% of the time, I start QGIS, move the mouse to the top left over “Project” go to “Recent Projects” and select the one I want. If I am lucky[ Read more](<../../../2015/08/18/qgis-welcome-page/index.html>)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2015/08/18/qgis-welcome-page/index.html>) 2020-04-29
## [Syntactic sugar for PyQGIS](<../../../2015/08/12/with-edit-layer/index.html> "Syntactic sugar for PyQGIS")
PyQGIS now supports a nice new addition for handling edit sessions in layers. This way, changes get committed automatically at the end of a successful (python) edit session.
    
    with edit(layer):
        do your changes here()
    
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2015/08/12/with-edit-layer/index.html>) 2020-04-29
## [Postgres Expression Compiler for QGIS](<../../../2015/07/29/postgres-expression-compiler/index.html> "Postgres Expression Compiler for QGIS")
Performance This project is all about performance of QGIS with a postgres/postgis database. A lot of people have QGIS connected to postgres/postgis (if you don’t: it’s a great combination in the open source geo stack). Databases are really optimized for querying. They keep indexes of geometries to be able to find them faster, they keep indexes of attributes to filter faster – and finally they often run on powerful servers. QGIS tries to be smart[ Read more](<../../../2015/07/29/postgres-expression-compiler/index.html>)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 anni ago](<../../../2015/07/29/postgres-expression-compiler/index.html>) 2020-04-29
## [QField in the wild](<../../../2015/06/15/qfield-in-the-wild/index.html> "QField in the wild")
QField Experimental is out, after a couple of months of requirements gathering, private early alpha testing and foremost tons of emails requesting access to the testes group we decided today to put the current BETA version in the playstore. This means that from now on you can install QField just like any other android app by using the playstore.
[![QField app on Google Play](https://developer.android.com/images/brand/en_app_rgb_wo_45.png)](<https://play.google.com/store/apps/details?id=ch.opengis.qfield>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [11 anni ago](<../../../2015/06/15/qfield-in-the-wild/index.html>) 2020-04-29
[](<../../../2015/06/15/qfield-in-the-wild/index.html> "QField in the wild")
## [QGIS Quality and Testing](<../../../2015/06/01/qgis-quality-and-testing/index.html> "QGIS Quality and Testing")
I promised that I will write a bit about what I’ve been up to at the last QGIS developer meeting – apart from the social part we also got some work done there. So let me start with something that really matters to me and I think can make a big impact. Unit Testing At the start of the developer conference Alessandro Pasotti asked me to do a workshop on unit tests. We quickly squatted[ Read more](<../../../2015/06/01/qgis-quality-and-testing/index.html>)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [11 anni ago](<../../../2015/06/01/qgis-quality-and-testing/index.html>) 2020-04-29
## [Tak Nødebo](<../../../2015/05/27/tak-nodebo/index.html> "Tak Nødebo")
After a week with QGIS members from all over the world we arrived back home and can say that once again, the QGIS developer meeting #13 was a great event. It started with the QGIS User Conference where a lot of interesting talks from experiences in day-to-day usage to low-level technology insights could be attended. Tim Sutton in the end took the chance to shortcut users and developers directly, asking for feedback and advice –[ Read more](<../../../2015/05/27/tak-nodebo/index.html>)
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [11 anni ago](<../../../2015/05/27/tak-nodebo/index.html>) 2020-04-29
## [Performance for mass updating features](<../../../2015/04/29/performance-for-mass-updating-features-on-layers/index.html> "Performance for mass updating features")
This post discusses how to improve the performance of pyqgis code which updates a lot of features by a factor of more than 10.
By [**Matthias Kuhn**](<../../../author/mkuhn/index.html> "Matthias Kuhn"), [11 anni ago](<../../../2015/04/29/performance-for-mass-updating-features-on-layers/index.html>) 2020-04-29
## [A star is born, QGIS mobile is now QField](<../../../2015/01/28/qgis-mobile-is-now-qfield/index.html> "A star is born, QGIS mobile is now QField")
It is with great pleasure that we want to announce the new name for what was briefly known as QGIS mobile. Please welcome QField for QGIS™!  
QField is an Open Source field data capture and management app fully compatible with QGIS™ which allows you to take your QGIS projects out of the office for effective field work while maintaining QGIS’ styling and edit widgets QField for great preparation time.  
QField will be released for free on the Playstore with the possibility of [donating to the project via paypal](<https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=X3TRREXGSC9CW>) (preferred) or by buying the [QField for QGIS Karma edition app](<../../../../../qfield.opengis.ch/karma>).
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [11 anni ago](<../../../2015/01/28/qgis-mobile-is-now-qfield/index.html>) 2022-03-04
[](<../../../2015/01/28/qgis-mobile-is-now-qfield/index.html> "A star is born, QGIS mobile is now QField")
## Paginazione degli articoli
[Precedenti](<../13/index.html>) [1](<../../index.html>) … [13](<../13/index.html>) 14 [15](<../15/index.html>) … [23](<../23/index.html>) [Successivi](<../15/index.html>)
