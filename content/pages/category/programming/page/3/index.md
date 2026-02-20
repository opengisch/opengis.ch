---
title: "Programming – Page 3 – OPENGIS.ch"
date: "2015-08-12T15:58:17+02:00"
lastmod: "2020-04-29T16:05:41+02:00"
source: "www.opengis.ch/category/programming/page/3/index.html"
---

## [Syntactic sugar for PyQGIS](<../../../../2015/08/12/with-edit-layer/index.html> "Syntactic sugar for PyQGIS")
PyQGIS now supports a nice new addition for handling edit sessions in layers. This way, changes get committed automatically at the end of a successful (python) edit session.
    
    with edit(layer):
        do your changes here()
    
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 years ago](<../../../../2015/08/12/with-edit-layer/index.html>) 2020-04-29
## [Performance for mass updating features](<../../../../2015/04/29/performance-for-mass-updating-features-on-layers/index.html> "Performance for mass updating features")
This post discusses how to improve the performance of pyqgis code which updates a lot of features by a factor of more than 10.
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [11 years ago](<../../../../2015/04/29/performance-for-mass-updating-features-on-layers/index.html>) 2020-04-29
## [Python support even closer](<../../../../2013/05/21/python-suport-even-closer/index.html> "Python support even closer")
anybody has a hint?
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [13 years ago](<../../../../2013/05/21/python-suport-even-closer/index.html>) 2020-04-29
## [Getting closer to taming the snake](<../../../../2013/05/21/getting-closer-to-taming-the-snake/index.html> "Getting closer to taming the snake")
very geeky but I have to post this: D/Qt (27512): src/python/qgspythonutilsimpl.cpp: 188: (runString) COMAND OK: import sys D/Qt (27512): src/python/qgspythonutilsimpl.cpp: 188: (runString) COMAND OK: import os D/Qt (27512): src/python/qgspythonutilsimpl.cpp: 188: (runString) COMAND OK: sys.path = [“/data/data/org.qgis.qgis/files/share/python”,”/data/data/org.qgis.qgis/files//python”,”/data/data/org.qgis.qgis/files//python” + “/plugins”,”/data/data/org.qgis.qgis/files/share/python/plugins”] + sys.path D/Qt (27512): src/python/qgspythonutilsimpl.cpp: 91: (initPython) newpaths: “/data/data/org.qgis.qgis/files/share/python”,”/data/data/org.qgis.qgis/files//python”,”/data/data/org.qgis.qgis/files//python” + “/plugins”,”/data/data/org.qgis.qgis/files/share/python/plugins” D/Qt[ Read more](<../../../../2013/05/21/getting-closer-to-taming-the-snake/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [13 years ago](<../../../../2013/05/21/getting-closer-to-taming-the-snake/index.html>) 2020-04-29
## [Python support in qgis is getting there](<../../../../2013/05/20/python-support-in-qgis-is-getting-there/index.html> "Python support in qgis is getting there")
Never been so close, but it took the heck out of me… now lets see if after 4 days of continuous fiddling around I manage to tame the snake
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [13 years ago](<../../../../2013/05/20/python-support-in-qgis-is-getting-there/index.html>) 2020-04-29
[](<../../../../2012/11/12/inasafe-1-0-launched/index.html> "InaSAFE 1.0 Launched")
## [InaSAFE 1.0 Launched](<../../../../2012/11/12/inasafe-1-0-launched/index.html> "InaSAFE 1.0 Launched")
End October after a heavy development sprint, the InaSAFE team (which consists of developers from around the world, funded by AUSAID and The World Bank / GFDRR) released inaSAFE 1.0 at the AMCDRR, a high level conference for disaster risk reduction in Asia. During the same event, inaSAFE was even demonstrated to the President of Indonesia.
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [13 years ago](<../../../../2012/11/12/inasafe-1-0-launched/index.html>) 2020-04-29
## [Necessitas Beta1 "breaks" qgis on android – don't update](<../../../../2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update-2/index.html> "Necessitas Beta1 "breaks" qgis on android – don't update")
Hi all, it has been a while since my last post, and foremost QGIS on android release. I’m very sorry. I’ve been working hard on another project (inasafe.org) that toke up all my time since we just launched version 1.0. So now to the real problem, necessitas (the android Qt[ Read more](<../../../../2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update-2/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [13 years ago](<../../../../2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update-2/index.html>) 2020-04-29
## [Necessitas Beta1 "breaks" qgis on android – don't update](<../../../../2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update/index.html> "Necessitas Beta1 "breaks" qgis on android – don't update")
Hi all, it has been a while since my last post, and foremost QGIS on android release. I’m very sorry. I’ve been working hard on another project (inasafe.org) that toke up all my time since we just launched version 1.0. So now to the real problem, necessitas (the android Qt[ Read more](<../../../../2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [13 years ago](<../../../../2012/10/25/necessitas-beta1-breaks-qgis-on-android-dont-update/index.html>) 2020-04-29
## [dealing with MTP (media transfer protocol) on Android](<../../../../2012/06/22/dealing-with-mtp-media-transfer-protocol-on-android/index.html> "dealing with MTP \(media transfer protocol\) on Android")
MTP is probably the most annoying thing I encounter lately on tablets, why don’t I get a simple USB mass storage when I connect my tablet? here some hints on how to get (maybe) rid of mtp in ICS (android 4.0) Just change the connection mode to Mass Storage or[ Read more](<../../../../2012/06/22/dealing-with-mtp-media-transfer-protocol-on-android/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2012/06/22/dealing-with-mtp-media-transfer-protocol-on-android/index.html>) 2020-04-29
[](<../../../../2012/05/12/qgis-4200m/index.html> "QGIS @ 4200m")
## [QGIS @ 4200m](<../../../../2012/05/12/qgis-4200m/index.html> "QGIS @ 4200m")
One of the nice things of being freelance it that you can work on Sundays when the weather is horrible and get out on Tuesdays when it rocks 😉 . So Tuesday I decided to go test QGIS at high altitude and went to the Breithorn and the Pollux with my best friend for[ Read more](<../../../../2012/05/12/qgis-4200m/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [14 years ago](<../../../../2012/05/12/qgis-4200m/index.html>) 2020-04-29
## Posts pagination
[Previous](<../2/index.html>) [1](<../../index.html>) [2](<../2/index.html>) 3 [4](<../4/index.html>) … [6](<../6/index.html>) [Next](<../4/index.html>)
