---
title: 'Suivi de l’arrière-plan QField – OPENGIS.ch'
date: 2023-12-20
slug: "suivi-de-larriere-plan-qfield"
url: "/it/2023/12/20/suivi-de-larriere-plan-qfield/"
source: "www.opengis.ch/it/2023/12/20/suivi-de-larriere-plan-qfield/index.html"
---
Il y a quelques années, la communauté QField et ses utilisateurs ont montré leur amour pour leur application de terrain préférée en soutenant un crowdfunding réussi pour améliorer la manipulation de l’appareil photo.
Depuis lors, OPENGIS.ch a continué à diriger le développement de QField avec le soutien régulier de sponsors. Nous ne pourrions être plus fiers des progrès que nous avons réalisés, avec de nombreuses nouvelles fonctionnalités ajoutées dans chaque version majeure. Il s’agit notamment d’améliorations majeures en matière de positionnement, y compris le suivi de la localisation, l’intégration de récepteurs GNSS externes par le biais non seulement de Bluetooth, mais aussi de connexions TCP/UDP et de ports série, d’indicateurs et de contraintes de précision et, plus récemment, de lecture de capteurs, pour n’en citer que quelques-uns.
Nous faisons maintenant appel à la communauté pour nous aider à améliorer QField et à franchir une étape importante : le **service de localisation en arrière-plan**.
S’engager maintenant
![](./gps-trackingf4e5.jpg)
## Objectif principal : localisation en arrière-plan sur Android – 25’000€.
Actuellement, QField exige que les utilisateurs gardent l’écran de leur appareil allumé et que l’application soit au premier plan pour suivre le positionnement de l’appareil. Sur les appareils mobiles, cela peut décharger les batteries plus rapidement que ce qui est souhaité, dans des environnements où les possibilités de recharge sont limitées.
Ce crowdfunding vise à supprimer cette contrainte et à **permettre à QField – par le biais d’un service en arrière-plan – de suivre en permanence la localisation** même lorsque l’appareil est suspendu (c’est-à-dire lorsque l’écran est éteint ou verrouillé). 
Pour ce faire, un travail important est nécessaire car le cadre de positionnement sur Android devra être déplacé vers un service d’arrière-plan dédié. Le travail récent que nous avons effectué en ajoutant un service d’arrière-plan pour synchroniser les pièces jointes des images capturées dans les [projets QFieldCloud](<https://qfield.cloud/>) nous a donné l’assurance que nous pouvions atteindre notre objectif tout en nous donnant une idée de l’ampleur du travail nécessaire.
### _Quelques avantages_
Être à court de batterie est le cauchemar de la plupart des géomètres de terrain. En déplaçant le suivi de la localisation vers un service d’arrière-plan, les utilisateurs pourront améliorer considérablement l’autonomie de leur batterie et continuer à se concentrer sur leurs tâches, même si cela implique de passer à une autre application.
De plus, alors que les ninjas d’OPENGIS.ch sont occupés à résoudre les problèmes de QField signalés tout au long de l’année, il y aura toujours des scénarios inattendus conduisant à des arrêts abrupts de l’application, tels que des applications tierces, des systèmes à court de batterie, etc. Pour y remédier, le cadre du service d’arrière-plan servira également **de sauvegarde pour éviter la perte de données de localisation** lorsque QField s’arrête inopinément et offrira aux utilisateurs des moyens de récupérer ces données lors de la réouverture de QField.
## Objectif 1 : navigation en arrière-plan avec retour d’information audio 5’000 €.
Le deuxième objectif complémentaire s’appuie sur l’agréable système de navigation de QField, de point à point. Si la communauté QField atteint ce seuil, un nouveau **retour audio de navigation en arrière-plan informant les utilisateurs sur le terrain de la proximité de leur cible** sera mis en place. 
Le retour audio utilisera la technologie de la synthèse vocale pour indiquer la distance à la cible en mètres pour un intervalle de temps ou de distance donné.
## Objectif 2 : iOS 15’000€
L’objectif principal couvrira uniquement la mise en œuvre d’Android. Comme il s’agit d’un travail de très bas niveau, nous devrons le reproduire pour chaque plateforme que nous supportons. Si nous atteignons l’objectif 2, nous le mettrons également en œuvre pour iOS.
# S’engager maintenant :
Si vous ne voyez pas le formulaire intégré, vous pouvez l’ouvrir directement [ici](<https://forms.clickup.com/2192114/f/22wqj-26041/KCQACZWJ84G4MJJ2XR>).
Merci de soutenir notre crowdfunding et gardez un œil sur notre blog pour des mises à jour sur l’état d’avancement.
### _Related_
