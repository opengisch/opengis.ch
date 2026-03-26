---
title: 'Les arcs circulaires dans QGIS – OPENGIS.ch'
date: 2025-05-07
slug: "les-arcs-circulaires-dans-qgis"
url: "/fr/2025/05/07/les-arcs-circulaires-dans-qgis/"
source: "www.opengis.ch/fr/2025/05/07/les-arcs-circulaires-dans-qgis/index.html"
---
### **Pourquoi ils sont si importants et comment tu peux aider**.
![Diagram illustrating circular arcs used in GIS geometry instead of segmented straight lines](./pb6001.png)
Dans le monde du traitement des données géographiques, les **arcs circulaires** (en anglais _circular arcs_) sont un élément souvent négligé, mais extrêmement important. Dans **QGIS** , l’application SIG open-source de référence, ils ne sont actuellement pris en charge que de façon limitée, et c’est précisément ce que nous voulons changer.
🔗**Aide-nous ici** 👇
[![French crowdfunding call-to-action banner for reliable circular-arc support in QGIS](./arcs_crowdfunding_link-fr1bd6.png)](</crowdfunding-un-soutien-fiable-pour-les-arcs-de-cercle-dans-qgis/index.html>)
* * *
### **Que sont les arcs circulaires, et pourquoi sont-ils importants?**
Les arcs circulaires sont des éléments géométriques qui ne sont pas composés de segments de ligne droite, mais représentent de véritables **courbes**. Ils sont définis par trois points: un point de départ, un point final et un point d’intersection _(ou le centre du cercle)_.
**On les trouve dans:**
  - Les ronds-points
  - Les bifurcations
  - Les données de planification et de CAO
  - La mensuration officielle


Les véritables **arcs circulaires** permettent des analyses plus précises et de meilleurs résultats lors du traitement ultérieur. Sans eux, les systèmes SIG doivent souvent diviser les courbes en de nombreux petits segments de ligne _(segmentation)_ , ce qui réduit la précision et augmente inutilement le volume des données.
* * *
### **Quel est le problème actuel dans QGIS?**
Actuellement, QGIS prend en charge les arcs circulaires de manière native, mais **uniquement dans certaines situations**. Dans les autres cas, ils sont convertis en courtes séquences de segments de ligne, particulièrement lorsque les géométries sont modifiées, coupées ou analysées.
**Plusieurs problèmes se créent:**
  - **Résultats imprécis** : une belle courbe se transforme en une ligne en zigzag.
  - **Perte de qualité** : il en résulte une dégradation de qualité inutile.
  - **Sources d’erreurs** : certaines opérations spatiales produisent des résultats incorrects car la géométrie originale n’est pas correctement préservée.


Quand les arcs circulaires sont préservés dans un jeu de données, mais que dans un autre les mêmes données apparaissent en version segmentée, des problèmes se présentent rapidement.
* * *
### **Quelle bibliothèque est responsable?**
La bibliothèque centrale qui gère les calculs géométriques dans QGIS s’appelle **GEOS** (_Geometry Engine – Open Source_). GEOS est extrêmement puissante, mais jusqu’à présent, elle ne peut pas encore traiter complètement les véritables arcs circulaires. Tous les programmes SIG qui utilisent GEOS ont donc **des limitations similaires**.
Cela signifie que si nous améliorons la gestion des arcs circulaires dans GEOS, non seulement QGIS en bénéficiera, mais aussi **toute la communauté SIG open-source** : de PostGIS à GDAL.
* * *
### **Notre crowdfunding: nous avons déjà atteint plus de la moitié!**
Pour résoudre ce problème de manière durable, nous avons réalisé un projet préliminaire en 2024 et mis en œuvre une première intégration des arcs circulaires dans le modèle géométrique de GEOS. Cette année, nous voulons aller plus loin et adapter également les algorithmes.
En avril, nous avons lancé un **financement participatif**. Notre objectif:
  - Adapter le moteur de superposition _(Overlay Engine)_ de GEOS pour gérer les arcs circulaires
  - Et sur cette base, améliorer considérablement la gestion dans QGIS.

![Crowdfunding progress graphic showing the circular-arcs campaign already over halfway funded](./pb-sol65b5.png)
* * *
**La bonne nouvelle:** nous avons déjà réuni **la moitié du financement**!
Maintenant, nous avons besoin de ton aide pour réussir. Chaque soutien, qu’il soit financier, par le partage de la campagne ou simplement en en parlant autour de vous, nous rapproche d’une **version améliorée de QGIS** , accessible à tous.
🔗 **Le crowdfunding, c’est par ici** 👇
[![French crowdfunding call-to-action banner for reliable circular-arc support in QGIS](./arcs_crowdfunding_link-fr1bd6.png)](</crowdfunding-un-soutien-fiable-pour-les-arcs-de-cercle-dans-qgis/index.html>)
* * *
### **Ensemble, nous pouvons y arriver!**
Le monde de l’open-source vit du fait que les gens travaillent ensemble sur quelque chose de grand. Avec une véritable prise en charge des arcs circulaires, QGIS deviendra non seulement plus précis et plus rapide, mais aussi un outil encore plus puissant pour la pratique.
**Aide-nous – pour de meilleures données géographiques, de meilleures analyses, de meilleurs résultats!**

{{< blog-video src="https://videopress.com/embed/ZzDfFdzJ" title="VideoPress video" >}}

[https://videopress.com/embed/ZzDfFdzJ](<https://videopress.com/embed/ZzDfFdzJ>)

### _Related_
