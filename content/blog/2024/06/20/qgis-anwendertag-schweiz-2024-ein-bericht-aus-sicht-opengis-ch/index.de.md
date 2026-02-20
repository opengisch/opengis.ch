---
title: 'QGIS Anwendertreffen Schweiz 2024 – ein Bericht aus Sicht OPENGIS.ch – OPENGIS.ch'
date: 2024-06-20
slug: "qgis-anwendertag-schweiz-2024-ein-bericht-aus-sicht-opengis-ch"
url: "/de/2024/06/20/qgis-anwendertag-schweiz-2024-ein-bericht-aus-sicht-opengis-ch/"
source: "www.opengis.ch/de/2024/06/20/qgis-anwendertag-schweiz-2024-ein-bericht-aus-sicht-opengis-ch/index.html"
---
Während der Pandemie bemerkte man, wie effizient man eigentlich remote kann, wie produktiv Meetings per Videocall sein können und wie gut Webinare funktionieren. Für uns bei OPENGIS.ch war das nichts Neues, da wir schon immer 100% remote gearbeitet haben. Aber was wir während dieser Zeit wirklich vermisst haben, waren die unplanmässigen, persönlichen Interaktionen bei einer Kaffeepause, auf dem Weg zur Toilette oder beim Feierabendbier in der Sonne. Deshalb freuten wir uns sehr, dass das QGIS Anwendertreffen letzte Woche nun schon zum zweiten Mal seither stattgefunden hat.
OPENGIS.ch ist seit der Entstehung von QGIS dabei. Eigentlich sogar schon davor; unser CEO Marco begann 2004 mit QGIS 0.6 zu arbeiten und unser CTO Matthias mit Version 1.7 im Jahr 2012. Und seit 2019 sind wir Weltweit die Firma mit den meisten QGIS Core Committer. Wir können definitiv sagen, dass OPENGIS.ch eine der treibenden Kräfte hinter der grossen Verbreitung von QGIS in der Schweiz und weltweit war.
![](./contrib15bf.png)Beiträge zum QGIS-Kern, gemessen in Commit-Zahlen
Wenn man sich die Arbeit im QGIS-Code ansieht, sind wir bei weitem das produktivste Unternehmen in der Schweiz und stehen weltweit nach North Road Consulting an zweiter Stelle. Darüber hinaus waren wir das erste – und immer noch eines von nur zwei – Unternehmen, das QGIS.org seit 2021 als[ large sustaining member unterstützt](<https://qgis.org/de/site/about/sustaining_members.html>).
Das macht uns sehr stolz und deshalb freuen wir uns umso mehr zu sehen, wie viel rund um QGIS in der Schweiz passiert und wie sehr es mit den Visionen und Zielen übereinstimmt, die wir uns vor Jahren gesetzt haben.
Nun zum Anwendertreffen: Der Morgen begann mit einer Präsentation unseres CTO Matthias „Neues aus der QGIS Welt“, die auch viele von der Anwendergruppe Schweiz gesponserte Arbeiten vorstellte.
![](./IMG_20240611_0859256aed.jpg)Unser CTO Matthias beantwortet QGIS-Fragen
Verbesserungen bei DXF, die Veröffentlichung von SwissLocator 3.0 mit swissalti3d und Vector-Tiles-Integration sowie ein Update zu den Fortschritten bei der Handhabung von Kreisbögen – eine Voraussetzung für die saubere Handhabung von AV-Daten in der Schweiz – waren nur einige der Highlights.
Der geheime Star von Matthias‘ Präsentation war die bessere Unterstützung von OGC API Features in QGIS, die auch in einem nachfolgenden Vortrag über Kablo hervorgehoben wurde, in dem gezeigt wurde, wie die nächste Generation von Fachschalen umgesetzt wird.
    
    Slides: [Neues aus der QGIS Welt - QGIS Anwendertag 2024](<https://docs.google.com/presentation/d/1ITN71d_Otv3e0DH63Muod9kpdE1FMd-wRmSPUVO-1Yg/edit?usp=sharing>)
Es folgte eine kurze Präsentation zum Projekt DMAV, vorgestellt durch Christoph Lauber. Dieses setzt es sich zum Ziel, eine Fachschale für die amtliche Vermessung mit QGIS zu implementieren.
Adrian Wicki vom Bundesamt für Umwelt (BAFU) und Isabel präsentierten, wie wir und unsere Partner Puzzle und Zeilenwerk dem BAFU mit dem SAM-Projekt helfen, die Gefahren von Hochwasser, Waldbrand oder Erdrutschen zu bewerten und sowohl Behörden als auch Bevölkerung zu warnen. Mit einer agilen Organisation gelingt es dem komplexen Projekt, die Anforderungen durch die Anwendung nutzerzentrierter Entwicklungsmethoden effizient umzusetzen. QGIS wird zur Visualisierung und Analyse von Daten verwendet und hilft den Prognostikern, Einblicke in die aktuelle Situation zu gewinnen.
    
    Slides: [BAFU_SAM](<https://docs.google.com/presentation/d/18bGeUzrVw7g58VxKrdLuAhTVt-BEYMpTvIDVTp4ZMJY/edit?usp=sharing>)
Andreas Neumann von der ETH Zürich und Michael stellten der Schweizer QGIS-Anwendergruppe das [qgis-js-Projekt](<https://github.com/qgis/qgis-js>) vor. qgis-js portiert den QGIS-Kern auf WebAssembly und kann damit direkt in einem Webbrowser ausgeführt werden kann. Obwohl das Projekt noch in Kinderschuhen steckt, hat es grosses Potenzial, interessante neue Anwendungsfälle zu ermöglichen, die vorher undenkbar waren.
    
    Slides: <https://boardend.github.io/qgis-js-demo/> 
Olivier Monod von der Stadt Yverdon stellte [Kablo](<https://kablo.ch/>) vor. Kablo ist ein Proof of Concept für das Management von Elektrizitätsinfrastruktur, das in Zusammenarbeit mit uns entwickelt wurde. Durch die Anwendung einer Middleware, die auf OGC API Features und Django basiert, zeigt Kablo, wie die üblichen Einschränkungen der aktuellen Fachschalen (wie Berechtigungsmanagement und atomare Operationen) überwunden werden können und wie die Zukunft Desktop und Web näher zusammenbringt.
    
    Slides: [kablo-qgis-user-days](<https://docs.google.com/presentation/d/1PQx48mr33cJcppWhoswofSj0zxGpHmncsjj24OtUCtI/edit?usp=sharing>)
Natürlich war nicht nur die Beiträge von OPENGIS.ch spannend. Sandro Mani von Sourcepole präsentierte die letzten Verbesserungen an [QWC2](<https://github.com/qgis/qwc2>), wie die Integration von Street View und coolen QGIS-Funktionen, die in diesem wunderschönen Web-GIS integriert wurden. Andreas Schmid vom Kanton Solothurn stellte vor, wie praktisch cloudoptimierte GeoTIFFs (COG) sind und welche Herausforderungen in einer Infrastruktur damit verbunden sein können. Interessiert an dem Thema? Lies mehr in unserem [Bericht zu cloudoptimierten Formaten](</04/09/cloud-optimized-geospatial-formats/index.html>). Mattia Panduri vom Kanton Tessin erklärte, wie sie QGIS genutzt haben, um die kantonalen Gebäudedaten zu harmonisieren. Und Timothée Produit von IG Group SA präsentierte, wie pic2map hilft, Fotos in 3D auf Karten zu bringen.
Um den Vormittag abzurunden, machte Nyall Dawson von North Road Consulting eine Live-Session vom anderen Ende der Welt, um die neuesten Entwicklungen zur Höhenfilterung in QGIS zu zeigen.
Am Nachmittag folgten Workshops. Claas Leiner leitete einen Workshop zu Ausdrücken in QGIS, während Matthias und Michael zeigten, wie man die QGIS-Verarbeitung für den Aufbau geospatialer Datenverarbeitungs-Workflows nutzen kann.
Im dritten Raum fand das erste [QGIS Model Baker](<https://modelbaker.ch/>) Anwendertreffen statt, bei dem dieses fantastische Werkzeug diskutiert wurde, welches wir seit Jahren entwickeln, um alles aus INTERLIS herauszuholen und zu helfen, angenehm und effizient damit zu arbeiten.
![](./10000508056aed.jpg)Erstes QGIS Model Baker Anwendertreffen
Es war wirklich ein sehr reichhaltiges und konstruktives QGIS-Anwendertreffen. Wir kamen mit vielen neuen Ideen und einem Gefühl der Erfüllung nach Hause. Wir sahen, wie grossartig die Community geworden ist, die wir beim Wachsen miterlebt und unterstützt haben.
Ein riesiger Dank geht an die Organisatoren und alle Beteiligten, die eine so grossartige Veranstaltung möglich gemacht haben. Nur das Bier in der Sonne fiel buchstäblich ins Wasser. Trotzdem gab es noch spannende Diskussionen im Bahnhofs-Bistro oder in den Speisewagen auf dem Nachhauseweg.
Bis zum nächsten Mal, und bis dahin helft weiterhin mit, QGIS und seine Community besser zu machen.
Wir danken allen, welche mit uns über die Jahre Visionen geformt haben. Gemeinsam machen wir auch aus den nächsten Jahren das Beste 🙂
### _Related_
