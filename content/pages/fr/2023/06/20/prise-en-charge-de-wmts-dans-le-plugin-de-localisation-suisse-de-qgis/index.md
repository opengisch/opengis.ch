---
title: "Prise en charge de WMTS dans le plugin de localisation suisse de QGIS – OPENGIS.ch"
author: "Matthias Kuhn"
date: "2023-06-20T06:03:05+02:00"
lastmod: "2023-06-20T06:03:10+02:00"
categories:
  - "QGIS"
  - "QGIS Plugins"
tags:
  - "qgis.org"
source: "www.opengis.ch/fr/2023/06/20/prise-en-charge-de-wmts-dans-le-plugin-de-localisation-suisse-de-qgis/index.html"
---

![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamede29a.png?resize=512%2C341&ssl=1)
Le plugin QGIS Swiss Locator facilite la vie de nombreux utilisateurs en Suisse en rendant accessibles les nombreuses géodonnées de swisstopo et opendata.swiss. Cela inclut un large éventail de couches de données, mais également des informations sur les objets et une recherche de noms de lieux.
Grâce à un projet financé par le groupe d’utilisateurs suisse, OPENGIS.ch a pu ajouter des fonctionnalités supplémentaires à son plugin. Cette fois avec l’intégration de WMTS comme source de données. Mais quelle est la différence entre WMS et WMTS ?
Tout d’abord, les similitudes : les deux protocoles – WMS et WMTS – conviennent au transfert d’images cartographiques d’un serveur vers un client. Cela signifie que ce ne sont pas des données brutes mais bien des données raster qui sont transmises qui conviennent donc pour des présentations dans le navigateur, dans le SIG de bureau ou pour une exportation PDF.
La différence est dans le T. Le T signifie « tuilé ». Avec un WMS (sans tuilage), n’importe quelle image peut être demandée. Avec un WMTS, les données sont livrées dans une grille prédéfinie.
Le principal avantage du WMTS réside dans la standardisation sur une grille. Cela permet à ces tuiles d’être temporairement stockées (c’est-à-dire mises en cache). Cela peut se faire sur le serveur, qui peut déjà précalculer toutes les tuiles et renvoyer un fichier directement sur demande sans avoir à recalculer une image. Cependant, il permet également la mise en cache côté client, ce qui signifie que le navigateur, ou dans le cas du localisateur suisse QGIS, peut simplement réutiliser chaque tuile sans recontacter le serveur. En conséquence, le temps de réaction peut être considérablement amélioré et vous pouvez travailler rapidement et avec fluidité au travers des applications.
Alors pourquoi continuer à utiliser WMS ?
Bien sûr, cela a aussi ses avantages. Le WMS peut fournir des images optimisées pour une requête précise. Par exemple, il peut placer de manière optimale toutes les étiquettes afin qu’elles ne soient pas coupées au bord de la carte. Ou combinez différentes couches interrogées avec des effets, les modes de fusion sont un moyen puissant de créer des cartes visuellement attrayantes. De plus, un WMS peut également fonctionner dans n’importe quelle résolution (DPI), ce qui signifie que les polices sont affichées dans une taille confortable sur chaque écran. Ou avec un export PDF.
Un WMS présente également l’avantage qu’il n’y a pas de mise en cache. S’il y a une base de données derrière, l’état actuel des données est toujours fourni. 
Dans le cas de QGIS swiss locator, il s’agit souvent de charger des fonds de carte. chargez des orthophotos ou des cartes nationales pour vous orienter. Ou d’autres données, qui sont de nature plus statique. Dans ce scénario, les avantages du WMTS prennent tout leur sens. Et c’est pourquoi nous tenons à remercier le groupe d’utilisateurs QGIS Suisse au nom de tous les utilisateurs suisses de QGIS pour avoir rendu cette implémentation possible !
Le plugin Swiss Locator est le couteau suisse de QGIS. Y’a-t’il un outil qui vous manque et que vous apprécierez voir intégré? Faites-le nous savoir!
### _Related_
