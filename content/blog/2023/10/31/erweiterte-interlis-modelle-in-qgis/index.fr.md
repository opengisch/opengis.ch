---
title: 'Les modèles INTERLIS étendus dans QGIS – OPENGIS.ch'
date: 2023-10-31
slug: "erweiterte-interlis-modelle-in-qgis"
url: "/fr/2023/10/31/erweiterte-interlis-modelle-in-qgis/"
source: "www.opengis.ch/fr/2023/10/31/erweiterte-interlis-modelle-in-qgis/index.html"
---
**_Le lancement de[QGIS Model Baker Release 7.6](<https://github.com/opengisch/QgisModelBaker/releases/tag/v7.6.0>) est arrivé et apporte plusieurs fonctionnalités utiles qui rendront votre travail avec les modèles de données INTERLIS dans QGIS encore plus efficace. L’une de ces fonctionnalités concerne la gestion des modèles INTERLIS avancés, qui pouvait être assez fastidieuse jusqu’à présent. Mais ce n’est plus le cas…_**
### Du problème à la solution
Lorsqu’un modèle INTERLIS contient des sous-classes qui étendent les fonctionnalités d’une classe de base, celles-ci, y compris la classe de base, sont matérialisées dans la base de données physique…
… et par conséquent, des couches sont créées dans QGIS.
De plus, lorsque les classes ont les mêmes noms, il devient difficile de s’y retrouver. C’était assez fréquent.
[![QGIS layer tree showing multiple Gebaeude layers from base and extended INTERLIS models with conflicting names](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835555-2847b676-49ee-43fb-a7ef-66c79b7db173.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835555-2847b676-49ee-43fb-a7ef-66c79b7db173.png?ssl=1>)
#### Exemple
Imaginons le modèle fictif `[Ortsplanung_V1_1](<https://github.com/opengisch/QgisModelBakerLibrary/blob/v1.5.1/tests/testdata/ilimodels/Ortsplanung_V1_1.ili>)` avec le topique `Konstruktionen` et la classe `Gebaeude`. Dans le [modèle cantonal](<https://github.com/opengisch/QgisModelBakerLibrary/blob/v1.5.1/tests/testdata/ilimodels/Kantonale_Ortsplanung_V1_1.ili>), cette classe est étendue avec plusieurs attributs via une sous-classe `Kantonale_Ortsplanung_V1_1.Konstruktionen.Gebaeude`. Ensuite, un [modèle communal](<https://github.com/opengisch/QgisModelBakerLibrary/blob/v1.5.1/tests/testdata/ilimodels/Staedtische_Ortsplanung_V1_1.ili>) a été créé où cette sous-classe s’est vu attribuer deux thèmes différents : `Staedtische_Ortsplanung_V1_1.Freizeit.Gebaeude` et `Staedtische_Ortsplanung_V1_1.Gewerbe.Gebaeude`.
Confus? Si c’est le cas, ne vous inquiétez pas. Car c’est précisément à cela que vise cette nouvelle versionde ModelBaker. Nous avons donc quatre implémentations de la classe `Gebaeude`. Jusqu’à présent, Model Baker les ajoutait de manière équivalente dans le projet QGIS.
Ainsi, si la classe `Gebaeude` dans le modèle de base `Ortsplanung_V1_1` avait une relation avec la classe `BesitzerIn` – et donc toutes ses sous-classes – une relation était créée dans QGIS pour chaque extension.
![QGIS form with duplicated relation widgets created from multiple extended Gebaeude classes](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835326-67529484-43f3-452d-9524-93ce1e6db6c9.png?w=750&ssl=1)
[](<https://user-images.githubusercontent.com/28384354/278835326-67529484-43f3-452d-9524-93ce1e6db6c9.png>)
Lorsque des catalogues sont impliqués, les formulaires associés deviennent particulièrement compliqués.
_Mais après tout, vous ne voulez pas voir tous ces calques, seulement ceux qui sont pertinents pour le modèle sur lequel vous travaillez actuellement. Devriez-vous vraiment vous embêter à gérer manuellement ces couches?_
_Non._
#### C’est fini à présent
Désormais, lors de la création du projet avec Model Baker, vous pouvez déterminer comment optimiser le projet.
[![Screenshot from 2023-10-28 22-01-30](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835762-b50ac25a-c2f1-405c-8a52-79d8a6843db9.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835762-b50ac25a-c2f1-405c-8a52-79d8a6843db9.png?ssl=1>)
Voilà, un projet clair et sans couches superflues est généré. Par exemple, vous travaillez sur le modèle urbain avec les deux sous-classes de Gebaeude.
[![Optimized QGIS project showing only the relevant extended Gebaeude layers for the city model](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835718-97071cd9-a0cf-453f-a4ee-2b8723a8aab8.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835718-97071cd9-a0cf-453f-a4ee-2b8723a8aab8.png?ssl=1>)
… et les relations sont dorénavant plus concises.
[![Optimized QGIS relation editor with a reduced set of relation widgets for the extended model](https://i0.wp.com/user-images.githubusercontent.com/28384354/278835830-af650aca-a914-4d75-8d04-0556359eb2e3.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278835830-af650aca-a914-4d75-8d04-0556359eb2e3.png?ssl=1>)
### Stratégies (Masquer/Grouper)
Cependant, les couches non pertinentes ne doivent pas toujours être masquées. Même si c’est la norme, il se peut que vous souhaitiez un projet optimisé, mais que vous vouliez simplement « ne pas voir » certaines couches. C’est pourquoi il existe l’option de regrouper toutes les couches non pertinentes dans un groupe.
[![QGIS layer tree grouping irrelevant base layers while keeping the optimized project structure readable](https://i0.wp.com/user-images.githubusercontent.com/28384354/278836121-f1c45599-4eea-4d1f-8248-1d830f305202.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278836121-f1c45599-4eea-4d1f-8248-1d830f305202.png?ssl=1>)
Dans ce cas, toutes les relations des couches sont créées, mais les widgets ne sont pas ajoutés aux formulaires. Cela rend le travail très agréable.
> _Au fait : les couches sont désormais renommées de manière unique. Ainsi, dès qu’une couche du même nom existe, le nom du thème ou, si nécessaire, le nom du modèle est ajouté en préfixe._
Si cela vous convient, vous pouvez maintenant vous consacrer à des tâches plus pertinentes 😊 Mais si vous souhaitez en savoir plus sur le fonctionnement, voici quelques informations complémentaires 🧑‍🏭
### Comment ça fonctionne ?
Pendant la phase de mise en œuvre, on a rapidement remarqué :
__Model Baker ne peut pas toujours savoir ce que les utilisateurs veulent voir et ce qu’ils ne veulent pas voir.__
Comme il est presque impossible de prendre en compte tous les cas, certaines hypothèses ont dû être formulées.
#### Hypothèses
On suppose que :
  - Si vous étendez une classe de base avec le _même nom_ , vous voulez la « remplacer », sinon vous la renommeriez.
  - Si vous étendez une classe de base _plusieurs fois_ (ce que l’on fait avec des noms différents), vous voulez également la « remplacer ».
  - Exception des deux cas : si vous étendez la classe dans le même modèle, mais dans un autre thème (car si vous aviez l’intention de la « remplacer », vous l’auriez rendue `ABSTRACT`).


#### Approche
Donc, techniquement formulé, voici ce qui a été mis en place :
  - Les classes de base avec des extensions portant _le même nom_ sont considérées comme _non pertinentes_.
  - Les classes de base avec _plusieurs extensions_ sont considérées comme _non pertinentes_.
  - Sauf si les extensions se trouvent _dans le même modèle_ , elles _ne sont pas_ considérées comme _non_ _pertinentes_.


#### Les stratégies
Selon ce que vous choisissez lors de la génération du projet, l’une des stratégies est mise en œuvre.
##### Stratégie 1 : Masquer
  - Les couches de classes de base avec des extensions portant le même nom sont masquées, de même que les couches de classes de base avec plusieurs extensions. Sauf si l’extension se trouve dans le même modèle, elle n’est pas masquée, mais renommée.
  - Les relations des couches masquées ne sont pas créées, donc aucun widget n’est ajouté.


##### Stratégie 2 : Grouper
  - Les couches de classes de base avec des extensions portant le même nom sont regroupées, de même que les couches de classes de base avec plusieurs extensions. Sauf si l’extension se trouve dans le même modèle, elle n’est pas regroupée, mais renommée.
  - Les relations des couches regroupées sont créées, mais les widgets ne sont pas appliqués dans le formulaire.


#### Sans stratégie ?
Si une couche porte le même nom, le nom du thème est ajouté. S’il n’est toujours pas unique, le nom du modèle est également ajouté.
[![QGIS layer tree with topic and model name prefixes added to keep extended-model layer names unique](https://i0.wp.com/user-images.githubusercontent.com/28384354/278836354-8e66b969-896f-4b62-89dc-f29e9d34cfdc.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278836354-8e66b969-896f-4b62-89dc-f29e9d34cfdc.png?ssl=1>)
### Baskets pour les classes étendues
Un bref rappel sur les baskets (paniers) : Un basket est une instance d’un thème et représente l’intersection avec l’ensemble de données actuelles. Un basket peut contenir des objets basés sur des classes qui sont autorisées dans le thème actuel. Il s’agit donc des classes définies dans le thème actuel et de celles définies dans le thème étendu par le thème actuel. Lorsque vous saisissez des objets dans le basket du thème actuel, vous devez également saisir les objets des classes définies dans le basket du thème actuel du thème de base.
Si cela semble un peu déroutant, nous avons de bonnes nouvelles pour vous :
__Dans les projets optimisés, seuls les baskets pertinents seront proposés à l’avenir.__
Cela signifie que même si la classe est définie dans un autre topique, seuls les baskets que vous voulez vraiment saisir seront proposés pour la couche. Selon la stratégie choisie, ce sont les instances sur lesquelles vous travaillez.
[![Basket selector limited to the relevant baskets for the chosen extended INTERLIS classes](https://i0.wp.com/user-images.githubusercontent.com/28384354/278836486-e170e939-a98e-4a86-9930-af01186d3eaa.png?w=750&ssl=1)](<https://i0.wp.com/user-images.githubusercontent.com/28384354/278836486-e170e939-a98e-4a86-9930-af01186d3eaa.png?ssl=1>)
### Voilà, c’est tout
Pour plus d’informations sur la mise en œuvre avec les modèles concernés, consultez la [documentation](<https://opengisch.github.io/QgisModelBaker/background_info/extended_models_optimization/>) et la liste de toutes les autres fonctionnalités géniales de Model Baker 6.7 dans le [journal des modifications](<https://github.com/opengisch/QgisModelBaker/releases/tag/v7.6.0>).
D’ailleurs, cette super fonctionnalité a été financée par [le groupe d’utilisateurs QGIS Suisse](<https://qgis.ch/fr>). Donc, par la communauté, c’est-à-dire par vous. Merci beaucoup 🙂 »
### _Related_
