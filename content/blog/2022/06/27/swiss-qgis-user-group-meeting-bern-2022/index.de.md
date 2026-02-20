---
title: 'Swiss QGIS user group Meeting Bern 2022 – OPENGIS.ch'
date: 2022-06-27
slug: "swiss-qgis-user-group-meeting-bern-2022"
url: "/de/2022/06/27/swiss-qgis-user-group-meeting-bern-2022/"
source: "www.opengis.ch/de/2022/06/27/swiss-qgis-user-group-meeting-bern-2022/index.html"
---
## Lernen, Präsentieren, Diskutieren und SICH TREFFEN
Im Sommer 2022 kam die Schweizer QGIS User Community nach 3 Jahren Online-Meetings endlich wieder physisch zusammen, um sich an der Universität Bern zu treffen. Bis zu 90 QGIS-Benutzer und Entwickler aus Wissenschaft und Technik genossen und diskutierten die neuesten QGIS-Funktionen und Anwendungsfälle.
Nach einer herzlichen Begrüssung und Einführung durch Isabel Kiefer von OPENGIS.ch begannen die Präsentationen.
### QGIS Update
Marco Bernasocchi (CEO von OPENGIS.ch und Vorsitzender von Qgis.org) stellte die neuesten QGIS-Funktionen aus den Changelogs der [aktuellen Langzeitversion 3.22](<https://changelog.qgis.org/en/qgis/version/3.22>), gefolgt von [3.24](<https://changelog.qgis.org/en/qgis/version/3.24>) and [3.26](<https://changelog.qgis.org/en/qgis/version/3.26>) vor. Zu den Verbesserungen zählen das neue Vertex-Tool zur Kurvenkonvertierung und Verbesserungen beim Mesh-Editing, dem 3D-Modus, dem WMS-Server und der SQL-Protokollierung, um nur einige zu nennen.
### QGIS Animation Workbench
Die reale Welt ist nicht statisch. So lassen sich Informationen in animierter Form oft besser verstehen, etwa die Visualisierung des Verkehrs auf einer Karte mit sich bewegenden Fahrzeugen. QGIS unterstützt jetzt Dynamic Rendering mit dem Animation Workbench Plugin. Tim Sutton (Kartoza) führte durch ein [Youtube Video](<https://www.youtube.com/watch?v=DkS6yvnuypc>), das die zugrunde liegenden Mechanismen des Plugins und seine Verwendung zeigt.
### QGIS Model Baker Update
Beginnend mit dem neuen Logo zeigte Romedi Filli (GIS-Fachstelle, Kt. Schaffhausen) die neuesten Verbesserungen am [QGIS Model Baker Plugin](<https://opengisch.github.io/QgisModelBaker/>). Insbesondere der Data Validator und das [UsabILIty Hub](</usabilityhub.opengis.ch/index.html>) machen die QGIS-Projektgenerierung aus Interlis-Daten noch einfacher. Darüber hinaus gibt es jetzt ein [Python Package](<https://pypi.org/project/modelbaker>) für diejenigen, die es vorziehen, alles mit Python zusammen zu skripten.
### Verwendung des QGIS Model Baker beim OEREB Kataster
Adrian Weber (Dütschler + Partner) zeigte anschließend wie mit QGIS Model Baker die Verwaltung kommunaler Nutzungspläne Schritt für Schritt von proprietärer Software auf QGIS-basierte Arbeitsabläufen migriert wird. Zeit und Geld das System anzupassen ist knapp. Die Schwierigkeit bei der Erbringung dieser öffentlichen Dienstleistung besteht darin, dass Daten rechtsverbindlich sind und die Systemkomponenten diese Anforderungen erfüllen müssen.
### Dynamische Forms und Widgets mit QGIS Expressions
Nach einer Kaffeepause hielt Andreas Neumann (Amt für Geoinformation, Kt. Solothurn) einen technischen Vortrag über nun dynamischere QGIS-Formulare und Widgets. Formfelder können jetzt über Expressions definiert werden, sodass sie abhängig von Werten in anderen Formfeldern automatisch aktualisiert werden. Weiterhin können Action Buttons, welche beispielsweise externe Webservices aufrufen, in Forms eingebunden werden, datenabhängige Constraints definiert werden und mehr.
### Analyse von Flugtrajektorien
Angetrieben von technischem Ehrgeiz und dem Ziel, eine sachliche Grundlage für [politische Diskussionen](<https://www.fluglaermforum.ch/>) zu schaffen, führte Yvo Weidmann ([Geoidee](<https://www.geoidee.ch/>)) eine anspruchsvolle Analyse der Landeanflüge zum Flughafen Zürich basierend auf Open Source Flight Trajectories und swisstopo-Daten durch. Dafür verarbeitete er Daten von [opensky-network.org](<https://opensky-network.org/>) und der [Aeronautical Information Publication](<https://skyguide.ch/>). Ein grosser Teil der Arbeit war Datenvalidierung und -bereinig. Schließlich visualisierte er die Ergebnisse in einer schicken QGIS-gesteuerten Animation der Anflüge.
### Teksi utilities application modules
Alexandre Bosshard (Ville de Pully) stellte [TEKSI](<https://www.teksi.ch/>) vor, einen Verein, der es sich zur Aufgabe gemacht hat, den Betreibern öffentlicher Infrastruktur Entscheidungshilfen in Form von professionellen Modulen,namentlich QGEP und QWAT, zur Steuerung ihrer Aktivitäten zu geben. Die Module sid allesamt Open-Source-Software, die hauptsächlich auf QGIS und PostgresSQL/PostGIS basiert.
### GEP (by Teksi) und hydrologische Analyse mit SWMM
Timothée Produit (Alpnetsystem SA (IG-Group)) hielt einen eher technischen Vortrag über ihren Ansatz, eine zentrale Datenbank zu verwalten, die sowohl Teksis Abwassermanagementtool und QGIS-Erweiterung QGEP als auch der Storm Water Management Software SWMM als Quelle zur Durchführung von hydrologischen Analysen in der Romandie dienen soll. Er zeigte das notwendige Datenbank- und Infrastrukturesetup und ihre Arbeitsablaufschritte, um das gewünschte Produkt zu erstellen.
### Das neue Profile Tool in QGIS Core
Nyall Dawson (North Road) führte durch sein [Youtube Video](<https://www.youtube.com/watch?v=GuL-Zst1Xcw>) über Terrain-Einstellungen im QGIS-Projekt und wie sie mit 3D-Karten und dem neuen Höhenprofil-Tool interagieren. Dies ist erst ab Version 3.26 möglich ist. Dies bietet neue Möglichkeiten zur Verarbeitung und Visualisierung Höhen- und 3D-Geodaten. Nyall nahm nach dem Video virtuell an der Konferenz teil, um Fragen des beeindruckten Publikums zu beantworten.
### Cool Maps mit QGIS
Schließlich schloss Marco Bernasocchi die Präsentationen mit einer Sammlung unglaublich kreativer QGIS-Karten ab, darunter Weihnachtswünsche, Sporttatistiken und die Topologie menschlicher Gesichter.
## Workshops
Nach einem leckeren Mittagessen inklusive Käsebuffet und fruchtbaren Diskussionen wurden die Teilnehmer aufgefordert, in den vier Nachmittagsworkshops selbst aktiv zu werden. Neben anderen interessanten Themen konnten die Benutzer die Arbeit mit [QField](<https://qfield.org/>) und [QFieldCloud](<https://app.qfield.cloud/>) kennenlernen oder in die Arbeit mit QGIS Model Baker und Datenvalidierung eintauchen, alles unterrichtet von den Experten und Entwicklern von OPENGIS.ch.
![](./P6153916ef34.jpg)Lernen ![](./P6153946ef34.jpg)Diskutieren ![](./P6153911ef34.jpg)Präsentieren ![](./P6153928ef34.jpg)SICH TREFFEN
### _Related_
