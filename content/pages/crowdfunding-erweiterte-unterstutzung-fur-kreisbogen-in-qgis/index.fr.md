---
title: "Crowdfunding: un soutien fiable pour les arcs de cercle dans QGIS – OPENGIS.ch"
source: "www.opengis.ch/fr/crowdfunding-un-soutien-fiable-pour-les-arcs-de-cercle-dans-qgis/index.html"
aliases:
  - "/fr/crowdfunding-un-soutien-fiable-pour-les-arcs-de-cercle-dans-qgis/"
---

![](../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2025/04/image87f2b.png?resize=750%2C360&ssl=1)
#### La vision: un traitement optimal des jeux de données avec des arcs de cercle
Les arcs de cercle sont un élément central dans le domaine de la géomatique. Une gestion précise et fiable de ces éléments est une condition essentielle pour travailler avec les données de la mensuration officielle.
Une prise en charge complète des arcs de cercle dans le logiciel QGIS permettra d’exploiter cette application pour de nombreux nouveaux cas d’utilisation, tant pour la mise à jour des données de la mensuration officielle que pour le travail sur des jeux de données connexes, tels que la planification de l’utilisation du sol.
QGIS permet déjà la saisie et l’enregistrement des arcs de cercle, mais ces derniers sont souvent perdus lors d’opérations comme l’intersection ou la fusion de géométries, qui entraîne un travail de post-traitement laborieux. Notre objectif est que QGIS prenne en charge ces opérations de manière fiable, efficace et sans erreur.
### Ce qui a été fait jusqu’à présent: implémentation de base dans GEOS
GEOS est la bibliothèque utilisée par QGIS et d’autres applications open source comme PostGIS pour les opérations géométriques. Elle permet d’effectuer l’intersection des jeux de données et de réaliser diverses transformations géométriques.
En 2024, grâce au soutien des cantons de Bâle-Campagne et de Zoug ainsi qu’au groupe d’utilisateurs QGIS Allemagne, une intégration de base des arcs de cercle a été réalisée. Depuis la version 3.13 de GEOS, le modèle géométrique de GEOS reconnaît les arcs de cercle et peut les représenter, ainsi que les manipuler dans des calculs simples.Cette avancée permet leur intégration dans des fonctionnalités plus avancées.
### Prochaine étape: amélioration du moteur de superposition et intégration dans QGIS
La prochaine phase consiste à adapter les algorithmes du moteur de superposition (_Overlay Engine_), qui est responsable des calculs d’intersections, de différences et de fusions de géométries. Ces fonctions sont utilisées non seulement dans les outils de traitement, mais aussi dans des outils interactifs comme l’outil de découpe. Une gestion propre des arcs de cercle dans ces calculs les rendra pleinement exploitables dans l’ensemble des fonctionnalités de QGIS.
#### Travaux concrets à réaliser:
  - Adapter de nombreuses structures de données et algorithmes conçus à l’origine pour les géométries linéaires.  

  - Revoir le calcul des points d’intersection. L’implémentation actuelle repose sur l’hypothèse que deux segments de ligne n’ont qu’un seul point d’intersection, ce qui n’est plus valable avec les arcs de cercle.  

  - Gérer des cas particuliers, comme les arcs de cercle avec des rayons extrêmement grands.  

  - Assurer une stabilité numérique élevée malgré les erreurs d’arrondi.  

  - Assurer une couverture de tests robuste pour garantir la durabilité à long terme.  



L’intégration des nouvelles fonctionnalités de GEOS dans QGIS est une autre étape essentielle pour rendre ces algorithmes réellement exploitables. Pour cela:
  - Les géométries contenant des arcs de cercle dans QGIS devront être correctement converties en géométries GEOS et inversement.  

  - Un traitement rigoureux des erreurs devra être mis en place afin que QGIS continue à fonctionner avec des versions de GEOS qui ne prennent pas encore en charge les arcs de cercle.  

  - Durant l’implémentation, nous veillerons à ce que QGIS reste compatible avec les anciennes versions de GEOS.  



### Ton soutien fait la différence!
Ta contribution à ce financement participatif permettra :
  - D’ouvrir de nouveaux cas d’utilisation pour QGIS.  

  - De faire progresser les technologies SIG open source.  

  - De générer un effet multiplicateur, car GEOS est utilisé dans PostGIS, MapServer, GeoDjango, GRASS et bien d’autres applications.


### Calendrier du projet
  - Fin du crowdfunding: 31 juillet 2025.  

  - Finalisation de l’implémentation dans GEOS: juin 2026.  

  - Intégration dans QGIS: avec la version LTR d’octobre 2026.  



Le projet est réalisé en collaboration avec OPENGIS.ch et Dan Baston de iSciences, un développeur clé de GEOS qui a déjà apporté une contribution majeure lors de la phase préliminaire.
