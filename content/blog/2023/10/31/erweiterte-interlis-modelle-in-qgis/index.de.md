---
title: 'Erweiterte INTERLIS Modelle in QGIS – OPENGIS.ch'
date: 2023-10-31
slug: "erweiterte-interlis-modelle-in-qgis"
url: "/de/2023/10/31/erweiterte-interlis-modelle-in-qgis/"
source: "www.opengis.ch/de/2023/10/31/erweiterte-interlis-modelle-in-qgis/index.html"
---
_**QGIS Model Baker[Release 7.6](<https://github.com/opengisch/QgisModelBaker/releases/tag/v7.6.0>) ist draussen und bringt einige nützliche Features auf die Karte, die deine Arbeit mit INTERLIS Datenmodellen in QGIS noch effizienter machen. Eines dieser Features betrifft das Handling von erweiterten INTERLIS Modellen. Denn das konnte bisher ziemlich mühsam sein. Doch dem ist nicht mehr so…**_
### Vom Problem zur Lösung
Wenn ein INTERLIS Modell  _erweiterte Klassen_ enthält, werden diese  _inklusive Basisklassen_ in der physischen Datenbank implementiert…
… und folglich Layer in QGIS erstellt.
Wenn dann die erweiterten Klassen die  _gleichen Namen_ haben, wird es schwierig sich zurecht zu finden. Und das war ziemlich oft der Fall.
[![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835555-2847b676-49ee-43fb-a7ef-66c79b7db173.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835555-2847b676-49ee-43fb-a7ef-66c79b7db173.png?ssl=1>)
#### Beispiel
Hier haben das fiktive Modell [`Ortsplanung_V1_1`](<https://github.com/opengisch/QgisModelBakerLibrary/blob/v1.5.1/tests/testdata/ilimodels/Ortsplanung_V1_1.ili>) mit dem Topic `Konstruktionen` und darin die Klasse `Gebaeude`. Im [Kantonalen Modell](<https://github.com/opengisch/QgisModelBakerLibrary/blob/v1.5.1/tests/testdata/ilimodels/Kantonale_Ortsplanung_V1_1.ili>) wurde diese Klasse um einigen Attributen zu `Kantonale_Ortsplanung_V1_1.Konstruktionen.Gebaeude` erweitert. Und nun wurde auch noch ein [Städtisches Modell](<https://github.com/opengisch/QgisModelBakerLibrary/blob/v1.5.1/tests/testdata/ilimodels/Staedtische_Ortsplanung_V1_1.ili>) gemacht, wo diese Klasse in zwei Topics weiter spezifiziert worden sind: `Staedtische_Ortsplanung_V1_1.Freizeit.Gebaeude` und `Staedtische_Ortsplanung_V1_1.Gewerbe.Gebaeude`.
Verwirrt? Wenn ja, dann keine Sorge. Denn genau darum geht es in dieser Erweiterung. Es existieren nun nämlich vier Implementierungen der Klasse `Gebaeude`. Und bisher hat Model Baker alle gleichberechtigt im QGIS Projekt angelegt.
Wenn nun die Klasse `Gebaeude` im Basismodell `Ortsplanung_V1_1` eine Beziehung zur Klasse `BesitzerIn` hat – und so auch alle ihre Erweiterungen, wurden in QGIS für jede Erweiterung eine Relation erstellt.
![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835326-67529484-43f3-452d-9524-93ce1e6db6c9.png?w=750&ssl=1)
[](<https://user-images.githubusercontent.com/28384354/278835326-67529484-43f3-452d-9524-93ce1e6db6c9.png>)
Vor allem wenn Kataloge im Spiel sind, wurden die Formulare dazu ziemlich übel.
_Dabei möchtest du doch gar nicht alle diese Layer sehen, sondern nur die, welche in dem Modell relevant sind, auf dem du gerade arbeitest. Musst du dich damit wirklich herumschlagen?_
_Nein._
#### Denn damit ist jetzt Schluss
Neu kannst du beim Erstellen des Projektes im Model Baker bestimmen, wie es optimiert werden soll.
[![Screenshot from 2023-10-28 22-01-30](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835762-b50ac25a-c2f1-405c-8a52-79d8a6843db9.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835762-b50ac25a-c2f1-405c-8a52-79d8a6843db9.png?ssl=1>)
Und schon wird dir ein schönes Projekt ohne überflüssige Layer generiert. Denn in diesem Beispiel arbeitest du auf dem Städtischen Modell mit den zwei spezifizierten `Gebaeude` Klassen.
[![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835718-97071cd9-a0cf-453f-a4ee-2b8723a8aab8.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835718-97071cd9-a0cf-453f-a4ee-2b8723a8aab8.png?ssl=1>)
… und auch die Relations sind jetzt schön schlank.
[![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835830-af650aca-a914-4d75-8d04-0556359eb2e3.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835830-af650aca-a914-4d75-8d04-0556359eb2e3.png?ssl=1>)
### Strategien (Verstecken/Gruppieren)
Die irrelevanten Layer müssen aber nicht immer versteckt werden. Auch wenn dies der Standard ist, kann es sein, dass du zwar ein optimiertes Projekt, aber dennoch Layer nicht einfach „nicht sehen“ möchtest. Deshalb gibt es die Option, alle irrelevanten Layer in einer Gruppe zu „sammeln“.
[![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/278836121-f1c45599-4eea-4d1f-8248-1d830f305202.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278836121-f1c45599-4eea-4d1f-8248-1d830f305202.png?ssl=1>)
Hier werden dann zwar die Relationen aller Layer erstellt, doch werden den Formularen die Widgets nicht hinzugefügt. Also bleibt das Arbeiten sehr angenehm.
> Übrigens: Die Layer werden neu so benannt, dass ihre Namen einmalig sind. Das heisst, sobald ein gleichnamiger Layer besteht, wird der Topicname oder wenn nötig auch der Modellname vorangesetzt.
Wenn dir das schon reicht, kannst du dich nun sinnvollerem widmen 😊 Falls du aber gerne etwas mehr über die _Funktionsweise_ wissen möchtest, geht’s jetzt weiter mit Hintergrundinfos 🧑‍🏭
### Wie funktionierts?
In der Implementierungsphase bemerkte man schnell:
_Der Model Baker kann nicht immer wissen, was die Benutzer:innen sehen möchten und was nicht._
Und da es fast unmöglich ist, alle Fälle zu berücksichtigen, mussten einige Annahmen getroffen werden.
#### Annahmen
Es wird angenommen, dass:
  - Wenn du eine Basisklasse mit  _demselben_ Namen erweiterst, willst du sie „ersetzen“, sonst würdest du sie umbenennen.
  - Wenn du eine Basisklasse  _mehrfach_ erweiterst (was man mit unterschiedlichen Namen tut), dann willst du sie ebenfalls „ersetzen“.
  - Ausnahme der beiden Fällen: Wenn du die Klasse im gleichen Modell, aber in einem anderen Thema erweiterst (denn wenn du die Absicht hättest, sie zu „ersetzen“, hättest du sie zu `ABSTRACT` gemacht).


#### Ansatz
Also wurde – technisch formuliert – folgendes umgesetzt:
  - Basisklassen mit  _gleichnamigen_ Erweiterungen gelten als  _irrelevant_
  - Basisklassen mit  _mehreren_ Erweiterungen gelten als  _irrelevant_
  - Ausser wenn die Erweiterungen im  _gleichen**** Modell_ sind, dann gelten sie _nicht_ als  _irrelevant_


#### Die Strategien
Je nach dem, was du dann bei der Projektgenerierung anwählst, wird eine der Strategien umgesetzt.
##### Strategie 1: Verstecken
  - Basisklassen-Layer mit gleichnamigen Erweiterungen werden  _ausgeblendet_ und Basisklassen-Layer mit mehreren Erweiterungen  _ebenfalls_. Es sei denn, die Erweiterung befindet sich im selben Modell, dann wird sie  _nicht**** ausgeblendet_, sondern  _umbenannt_.
  - Beziehungen von ausgeblendeten Ebenen werden  _nicht**** erstellt_ und damit auch  _keine**** Widgets_.


##### Strategie 2: Gruppieren
  - Basisklassen-Layer mit gleichnamigen Erweiterungen werden  _in einer Gruppe zusammengefasst_ , Basisklassen-Layer mit mehreren Erweiterungen  _ebenfalls_. Ausser wenn die Erweiterung im gleichen Modell ist, dann wird sie  _nicht gruppiert_ , sondern  _umbenannt_.
  - Beziehungen der gruppierten Ebenen werden  _erstellt_ , aber die Widgets werden  _nicht auf das Formular angewendet_.


#### Und ohne Strategie?
Sofern ein Layer mit gleichem Namen besteht, wird das Topic vorangesetzt. Ist er noch immer nicht eindeutig, dann auch noch das Model.
[![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/278836354-8e66b969-896f-4b62-89dc-f29e9d34cfdc.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278836354-8e66b969-896f-4b62-89dc-f29e9d34cfdc.png?ssl=1>)
### Baskets für erweiterte Klassen
Kurzes Recap über [Baskets (Behälter)](</2021/12/07/model-baker-6-7-noch-nie-wars-so-einfach/index.html#datasets>): Ein Basket ist eine Instanz eines Topics und die Schnittmenge zum aktuellen Dataset. Ein Basket kann Objekte basierend auf Klassen enthalten, die im Topic zulässig sind. Also sind das die Klassen, welche im aktuellen Topic definiert sind und die, welche in Topic definiert sind, das vom aktuellen Topic erweitert wurde. Wenn man nun Objekte im Basket des aktuellen Topics erfasst, muss man auch die Objekte der Klassen, die im Basistopic definiert sind, im Basket des aktuellen Topics erfassen.
Falls das jetzt etwas verwirrend klingt, haben wir gute News für dich:
_In den optimierten Projekten werden zukünftig nur die relevanten Baskets angeboten._
Das heisst, auch wenn die Klasse in einem anderen Topic definiert ist, werden dem Layer nur die Baskets angeboten, in denen man auch wirklch erfassen möchte. Je nach gewählter Strategie sind das die Instanzen, auf denen man arbeitet.
[![image](https://i0.wp.com/user-images.githubusercontent.com/28384354/278836486-e170e939-a98e-4a86-9930-af01186d3eaa.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278836486-e170e939-a98e-4a86-9930-af01186d3eaa.png?ssl=1>)
### Und das wars dann auch schon
Mehr Infos zur Umsetzung auch mit den betreffenden Modellen findest du in der [Dokumentation](<https://opengisch.github.io/QgisModelBaker/background_info/extended_models_optimization/>) und die Liste aller anderen tollen Features des Model Baker 7.6 im [Changelog](<https://github.com/opengisch/QgisModelBaker/releases/tag/v7.6.0>)
Übrigens wurde dieses tolle Feature von der [QGIS Anwendergruppe Schweiz](<https://qgis.ch/en>) finanziert. Also von der Community, also von dir. Vielen Dank 🙂
### _Related_
