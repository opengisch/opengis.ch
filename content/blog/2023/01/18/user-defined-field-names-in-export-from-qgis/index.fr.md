---
title: 'User defined field names in export from QGIS – OPENGIS.ch'
date: 2023-01-18
slug: "user-defined-field-names-in-export-from-qgis"
url: "/fr/2023/01/18/user-defined-field-names-in-export-from-qgis/"
source: "www.opengis.ch/fr/2023/01/18/user-defined-field-names-in-export-from-qgis/index.html"
---
Thanks to the sponsoring of the [Swiss QGIS User Group,](<https://www.qgis.ch/>) starting from QGIS 3.26 is it possible to override field names in the layer export dialog. Previous to that, QGIS would always export with the technical names from the database, whereas now it’s possible to override with the alias defined in QGIS or any custom name. One use for this in Switzerland — a highly polyglot country — is an export with translated names.
This is done via an additional column « Export name ». For convenience we also added a tri-state checkbox to toggle export names to their alias defined in the layer configuration or back to the field name. If a name is changed by hand the checkbox shows a mixed state.
![](https://i0.wp.com/user-images.githubusercontent.com/9881900/156719947-6e2183f0-27cb-41c4-a65b-9855822da233.gif?w=750&ssl=1)
### _Related_
