---
title: 'Python Bindings für INTERLIS – OPENGIS.ch'
date: 2023-11-24
slug: "python-bindings-fuer-interlis"
url: "/de/2023/11/24/python-bindings-fuer-interlis/"
source: "www.opengis.ch/de/2023/11/24/python-bindings-fuer-interlis/index.html"
---
**Seit einiger Zeit existiert die Idee von Python Bindings, erzeugt durch einen INTERLIS Compiler, welche die Modellinformationen für eine breite Entwicklerbasis zugänglich macht, was einen schnelleren Innovationszyklus ermöglicht und damit die Grundlage für neue Plattformen, Werkzeuge und Integrationen schafft.**
## How comes
Möchte man den Inhalt einer XTF Datei im QGIS visualisieren, muss man heutzutage die folgenden Schritte ausführen.
  1. Mit ili2db das physische Schema mit allen nötigen Parametern in einer relationalen Datenbank erstellen
  2. Mit ili2db die Daten in die relationale Datenbank importieren
  3. Durch __ Model Baker die Meta-Tabellen analysieren und das QGIS-Projekt erstellen
  4. Und trotzdem sind oft manuelle Nacharbeiten nötig, um im Modell enthaltene Informationen auf die Layer und Formulare im QGIS zu übertragen
  5. Am Ende muss wieder ein Export aus der relationalen Datenbank erfolgen, um zurück zum XTF zu kommen


Und jetzt stelle man sich mal vor, dass würde in einem Schritt gemacht werden können. Mit Drag’n’drop das XTF ins QGIS ziehen, die Formulare würden erstellt und die Daten visualisiert – ganz ohne Databank.
Natürlich ist für die Datenbearbeitung dann eine Datenbank noch immer sinnvoll (schon nur wegen der Performance), dies schliesst sich aber gegenseitig nicht aus.
Aber besonders nützlich wäre der Ansatz für die alltäglichen kleinen Arbeiten rund um INTERLIS.
Nur mal schnell …
  - … das XTF angucken
  - … den Fehler lokalisieren
  - … eine kleine Korrektur vornehmen
  - …


Beinahe nebenbei erschliessen sich dann ganz neue Möglichkeiten.
  - Erzeugen einer objektorientierten Abbildung des Klassenmodelles in Python Code (Insbesondere interessant als Grundlage für komplexere Fachapplikationen)
  - Automatisierte Erzeugung einer Modelldokumentation aus den INTERLIS Definitionen als HTML, Markdown, Word oder PDF.
  - Oder auch eines Modelldiagrammes
  - …


Solche Anforderungen sind mit dem aktuell verfügbaren Ansatz via ili2db bedingt lösbar auf Datenbankebene. Das zugrunde liegende Datenmodell wird abstrahiert und als “Blackbox” betrachtet. Dazwischen steht ili2c, welches die nötige Introspektion der Modelle übernimmt. Dies limitiert die Möglichkeiten bei der Entwicklung von Fachapplikationen basierend auf INTERLIS Datenmodellen und unterstützenden Werkzeugen.
Die Konsequenz davon ist, dass für Applikationen, welche darauf aufsetzen, anstelle der kompletten Modellinformationen nur noch ein relationales Abbild oder anderweitig vereinfachte Informationen davon zur Verfügung steht. Das erfordert einerseits, dass schwer wartbarer Code in SQL geschrieben wird. Dies ist langfristig ineffizient und fehleranfällig. Andererseits können gewisse Anforderungen wie rollenbasierte Zugriffsrechte nicht in der Datenbank, sondern nur auf Ebene Webservice umgesetzt werden, was dazu führt, dass Code an zwei Stellen nachgeführt werden soll und bei Modelländerungen von Hand nachgeführt werden muss.
Und ja, wir wissen um die Existenz des [GDAL/OGR Treibers](<https://gdal.org/drivers/vector/ili.html>). Doch dieser behält die Object-Relational-Mapping Denkweise bei und dient mehrheitlich dazu daten von einem _Tabellenformat_ in ein anderes zu transformieren. Das ist nicht unser Ziel.
Für die effiziente Programmierung von Fachapplikationen wünscht man sich, dass Entwickler ein INTERLIS-Modell direkt in ihrem Framework zur Verfügung haben, um alle diese Anforderungen entsprechend moderner IT-Entwicklungsansätze benutzen und zeitgemässe Anwendungen programmieren zu können. Stabil und effizient. Unter Berücksichtigung der Modells aber mit dem Hauptfokus auf die Anwendungsfälle der Nutzer. Immer mit der Möglichkeit den unvermeidlichen Modelländerungen folgen zu können, da die Interfaces ja einfach abgeleitet werden.
## Ansätze
Es sind einige grundsätzlich unterschiedliche Ansätze für die Umsetzung denkbar. Dabei ist es wichtig, dass dies in die Strategie Geoinformation Schweiz eingepasst ist und sich gut ins Ökosystem integriert.
  1. Benutzen des bestehenden ili2c XML (XSD) Interfaces womit man Python Bindings generiert
  2. Erstellen der Python Bindings auf der Basis eines [Metamodells](<https://www.interlis.ch/modelle/metamodell>)
  3. Aufbau einer API auf dem bestehenden ili2c um die Python Bindings zu generieren (aka Java2Python)
  4. Implementierung einer direkten Python Basierten Lösung um die Zwischenschritte zu verhindern (INTERLIS Python Compiler)


Nach eingehender Auseinandersetzung mit dem Thema kann der Weg via ili2c XSD ausgeschlossen werden, da wichtige Informationen nicht transparent übermittelt werden (z.B. Constraints). 
Die Entwicklung einer auf IOX/ili2c basierten Java-Komponente um damit Python Code und damit die erwünschten Bindings erstellen zu können, erscheint möglich aber nicht erstrebenswert. 
Die Entwicklung eines eigenen Compilers sehen wir als kritisch. Es bestehen bereits 2 Projekte und wir sehen nicht ein, warum ein Werkzeug mit identischem Funktionsumfang und Lösungsansatz (ANTLR als Parser/Lexer) nur in einer anderen Programmiersprache einen Mehrwert bieten sollte.
Den grössten Mehrwert sehen wir bei der Nutzung des Metamodells. Einem XML, welches eigens zu dem angestrebten Zwecke geschaffen wurde. So verfolgen wir bisher den Ansatz, über ili2c (oder alternativem Compiler) das Metamodell (IMD16) zu erstellen und daraus die Python-Bindings zu erzeugen. Die logische Konsequenz ist dann aus diesen Bindings auch generisch Reader abzuleiten welche in der Lage sind die zum Modell gehörenden XTF zu lesen.
![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/285478925-d75356fc-ce90-4d64-b607-f06e591d061a.png?w=750&ssl=1)
## Vorgehen
Erarbeiten eines Proof of Concepts, um die technologischen Grundlageentscheide zu validieren.
### Ziele des PoCs
  - Parsen des Metamodells
  - Generieren der Python Bindings (ILI=>Python-Klassen)
  - Ableitung generischer Reader (XTF=>Python-Objekte)
  - QGIS Integration Prototyp (Drag’n’Drop ILI oder XTF) zu Demonstrationszwecken


Voraussichtlich ist es möglich, mit einem Subset an Funktionalitäten der breiten Palette von INTERLIS-Konstrukten zu starten (Vererbung und Topics oder Integration von Repositorien sind von höherer Priorität als Constraints oder Views. Die genaue Priorisierung ist noch zu prüfen).
Die Resultate werden als open source Bibliotheken zur Verfügung gestellt, dokumentiert und getestet.
Dieses Projekt setzt eine erfolgreiche Einbettung in die bestehende Werkzeuglandschaft und eine enge Zusammenarbeit mit den Schlüsselpersonen im INTERLIS Umfeld voraus.
### Produkte
Implementierung von Produkten, welche einen tatsächlichen Mehrwert bieten für eine breitere Anwenderbasis. Hier seien zwei Beispiele vorgestellt.
#### Python Klassengenerator
Ein Generator für Python-Klassen, der ein Python-Datenmodell äquivalent zum INTERLIS-Datenmodell erzeugt. Dies ist als erster Schritt in Richtung einer langfristigen Basis für Fachapplikationen zu betrachten. Denkbar ist eine Webapplikation zur Modellkonformen Datenerfassung  
auf Basis von z.B. Django:
    
    generate_django_models.py --model [modelname] --output my_source/generated_classes/
#### Modelldokumentation
Ein Generator für eine Modelldokumentation, als Markdown (ermöglicht HTML, PDF, DOCX, …). Ausserdem besteht die Option, das Klassendiagramm grafisch als UML abzubilden.
    
    generate_ili_doc.py --model [modelname] # Online lookup
    generate_ili_doc.py --model [filename].ili # Local file
## Visionen
Bei Fachapplikationen für komplizierten Datenmodelle oder mit komplexen Workflows soll es möglich sein, eine durchgängige Entwicklung vom Modell bis zur fertigen Applikation zu ermöglichen. Das Modell soll sich dabei nahtlos als Basis für Fachapplikationen nutzen lassen.
Frameworks wie beispielsweise Django verfügen über Möglichkeiten, um (Web-)applikationen effizient zu entwickeln. Dabei werden Werkzeuge zur Verfügung gestellt, um Anforderungen zu lösen wie:
  - **Rollenbasierte Zugriffsrechte:** Es ist möglich, pro User und Rolle zu definieren, wer, was, unter welchen Umständen lesen und bearbeiten darf
  - **Nebeneffekte bei Bearbeitungsschritten:** Es ist möglich, sicherzustellen, dass bei gewissen Veränderungen auch Anpassungen in damit verwandten Daten nachgeführt werden
  - **Logging von Zugriffen:** Es ist möglich, Mutationen und Zugriffe sauber zu protokollieren
  - **Migrationen zwischen Versionen von Datenmodellen:** Bei einer Anpassung der Datenmodellversion können die dafür notwendigen Migrationsschritte kontrolliert durchgeführt werden (Bindings müssen lediglich neu generiert werden).
  - **Ansichten:** Es ist möglich, den Anwendern eine kontextbasierte Ansicht auf die Daten zu ermöglichen, welche aus Anwenderperspektive sinnvoll ist.
  - **Erweiterungen:** Verschiedene Erweiterungen werden über eine grosse Community gepflegt welche sich auch ausserhalb der Geo-Szene befindet. Beispielsweise die Möglichkeit, Ansichten als OGC API Features zur Verfügung zu stellen, inklusive der oben genannten rollenbasierten Zugriffsrechte, Logging etc.
  - **Modularisierung:** Saubere Trennung von Datenmodell und darauf aufbauenden Anwendungsfällen. Applikationsrelevante Zusatzinformationen wie temporäre Stati oder Caches können im Applikationscode verwaltet werden.
  - **Testing:** Applikationen können automatisiert getestet werden
  - **Nahtlos vom Modell zur dokumentierten Python Library:** Bereitstellung von Interface-Bibliotheken für Anwendungshersteller, welche die  
Modelldokumentation bereits als Python-Docstring enthalten.
  - **Kompromissloser Einsatz von Automatisierung:** Inwertsetzung des sich ergebenden Potentials in Verbindung mit CI/CD. Also vom publizierten Modell zur Python-Bibliothek, der Dokumentation in belibigen Formaten oder dem Klassendiagramm ohne manuelle Unterbrüche.
  - **Verbreitung:** Die Schaffung eines _Ökosystems_ rund um INERLIS wie beschrieben, führt zwangsläufig zur Verbreitung (Erfassungsapplikationen).


### _Related_
