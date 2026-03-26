---
title: "Crowdfunding: Erweiterte Unterstützung für Kreisbögen in QGIS – OPENGIS.ch"
source: "www.opengis.ch/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.html"
aliases:
  - "/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/"
---

![Banner for the QGIS circular arc support crowdfunding campaign](../../i0.wp.com/www.opengis.ch/wp-content/uploads/2025/04/image87f2b.png?resize=750%2C360&ssl=1)
#### Die Vision: Datensätze mit Kreisbögen sauber bearbeiten
Kreisbögen sind ein zentrales Element im Vermessungswesen, der saubere Umgang damit ist eine zwingende Voraussetzung für das Arbeiten an und mit Daten der Amtlichen Vermessung. Eine komplette Unterstützung von Kreisbögen in der Standardsoftware QGIS wird es ermöglichen, diese Applikation für eine ganze Palette von neuen Anwendungsfällen einzusetzen, sowohl für die Nachführung der Amtlichen Vermessung, als auch für das Arbeiten mit darauf aufsetzenden Datensätzen wie der Nutzungsplanung. QGIS unterstützt bereits das Erfassen und Speichern von Kreisbögen, diese gehen jedoch oft verloren, wenn Geometrien verschnitten oder zusammengeführt werden. Dies führt zu einer aufwändigen Nachbearbeitung, wir möchten gerne erreichen, dass QGIS das für uns übernimmt: zuverlässig, sauber und fehlerfrei.
**Finanzierung erfolgreich abgeschlossen!**  

<div class="page-inline-embed crowdfunding-progress-embed">
  <iframe
    class="page-inline-embed__iframe crowdfunding-progress-iframe"
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSQUZgZV6MYLKxjYwshhudga3VP-mIT_9sTyGfaNQ7PUcywszPXC9VmCIV9BOZGKEQ5QN1FEsSVsXNa/pubchart?oid=1555133790&amp;format=interactive"
    title="Crowdfunding progress"
    loading="lazy"
    frameborder="0"
    scrolling="no"
  ></iframe>
</div>

#### Was bisher geschah: Basisimplementierung in GEOS
GEOS ist die Bibliothek, welche in QGIS und anderen Open-Source Applikationen wie PostGIS eingesetzt wird für Geometrieoperationen. Sie erlaubt es, Datensätze miteinander zu verschneiden und sonstige geometrische Operationen durchzuführen. Im Jahr 2024 haben wir dank den Kantonen Basel-Landschaft und Zug sowie der Anwendergruppe Deutschland eine Basisintegration von Kreisbögen. Seit der GEOS Version 3.13 kennt das Geometriemodell von GEOS Kreisbögen und kann diese abbilden, sowie in sehr einfachen Berechnungsfunktionen damit umgehen. Damit steht der Weg nun frei, Kreisbögen auch in fortgeschrittenen Funktionen zu berücksichtigen.
#### Das nächste Ziel: Overlay Engine und QGIS Integration
Die nächste Phase beinhaltet die Anpassungen von Algorithmen in der Overlay Engine. Die Overlay Engine ist für Berechnungen wie Verschneidungen, Differenzen und Vereinen zuständig. Diese Funktionen sind nicht nur direkt über Verarbeitungswerkzeuge verfügbar, sondern oft auch in Werkzeuge zur Datenbearbeitung wie dem Verschneiden integriert. Durch eine saubere Berücksichtigung von Kreisbögen in den entsprechenden Berechnungsfunktionen stehen diese dem gesamten QGIS Funktionsumfang zur Verfügung.
Konkrete Aufgaben in diesem Bereich sind
  - Eine Vielzahl von Datenstrukturen und Algorithmen, welche im Hinblick auf lineare Geometrien geschrieben wurden müssen angepasst werden
  - Die Berechnung von Schnittpunkten muss überarbeitet werden. Die aktuelle Grundannahme der Implementierung, welche auf monotonen Ketten beruht, wobei zwischen zwei Liniensegmenten genau ein Schnittpunkt besteht, ist nicht mehr zutreffend und muss überarbeitet werden
  - Die Behandlung von Grenzfällen wie Kreisbögen mit extrem grossen Radien
  - Eine möglichst hohe nummerische Stabilität trotz Rundungsfehlern
  - Eine gute Testabdeckung der umgesetzten Funktionalitäten für langfristige Stabilität


Die Integration der neuen GEOS-Funktionalitäten in QGIS ist ein weiterer essenzieller Schritt, um die Algorithmen auch tatsächlich nutzbar zu machen. Dafür müssen QGIS Geometrien mit Kreisbögen zuverlässig in GEOS Geometrien umgewandelt werden können und umgekehrt. Weiter muss eine solide Fehlerbehandlung umgesetzt werden, damit QGIS weiterhin mit GEOS Funktionen umgehen kann, welche (noch) keine Kreisbogenunterstützung haben.
Während der Implementierung werden wir sicherstellen, dass QGIS weiterhin mit älteren GEOS Versionen funktioniert, welche noch keine Kreisbögen unterstützen. 
#### Deine Unterstützung macht einen Unterschied !
Deine Unterstützung dieses Crowdfundings macht es möglich
  - Neue Anwendungsfälle mit QGIS zu ermöglichen
  - Open-Source GIS Technologien voranzutreiben
  - Multiplikationseffekte zu erziehlen, GEOS wird auch in PostGIS, MapServer, GeoDjango, GRASS und vielen weiteren Applikationen verwendet


#### Vorgehen
Das Crowdfunding läuft bis zum 31. Juli 2025. Sobald die nötige Unterstützung zusammengekommen ist, gilt das Projekt als finanziert und wird gestartet. Die Rechnungen werden versendet, wenn die Finanzierung für das Projekt sichergestellt ist.
Die Umsetzung in GEOS werden bis Juni 2026 abgeschlossen. Die Integration in QGIS wird mit dem Oktoberrelease 2026 geschehen.
Die Umsetzung findet in Zusammenarbeit zwischen OPENGIS.ch und Dan Baston von iSciences statt, welcher als GEOS Kernentwickler bereits im Vorprojekt eine hervorragende Arbeit geleistet hat.
