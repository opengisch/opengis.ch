---
title: "Model Baker INTERLIS Data Validator – OPENGIS.ch"
author: "Dave Signer"
date: "2022-11-15T06:47:00+01:00"
lastmod: "2024-08-13T23:37:51+02:00"
categories:
  - "GIS"
  - "Interlis"
  - "QGIS"
  - "QGIS Plugins"
  - "Uncategorised"
tags:
  - "ilivalidator"
  - "INTERLIS"
  - "Model Baker"
source: "www.opengis.ch/it/2022/11/15/model-baker-interlis-data-validator/index.html"
---

**The fully integrated Data Validator, which allows validating your** **data directly in QGIS against their INTERLIS model, exists for almost a year now. After lots of user feedback and some investments, it’s now shinier than ever. Time for an update and a little step-by-step guide.**
## Why is it so awesome?
Using the Model Baker Data Validator has two major advantages.
First, **you do not need to export your data before you validate them**. Thanks to the `--validate` option, Model Baker can use [ili2db](<https://github.com/claeis/ili2db>) to validate the data directly in the database.
Second, you can interactively use the result list and **zoom or pan to coordinates of validation issues** in the QGIS map canvas or directly **open or select the feature in question**. So fixing the errors is much easier.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/menu18ce.png?resize=750%2C149&ssl=1)
## Step-by-step guide
Though the validation is performed on the database, we start with importing an invalid transfer file. With this, we have the complete end-to-end journey ?‍?
### Import invalid data
Depending on the quality of your data, you need to create the schema already with less strict constraints in the database. Like if some mandatory (NOT NULL) constraints are violated in your data, you need create a database without these constraints enabled.
We use an [example model](<../../../../../../models.opengis.ch/demo_data/ModernCity_V1.ili>) in this guide to avoid complexity and some [invalid demo data](<../../../../../../models.opengis.ch/demo_data/invalid_data.xtf>). 
In  _Database > Model Baker > Import/Export Wizard_ choose _Run without constraints_ on the import session. 
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/runwithoutconstraints14dd.png?resize=750%2C63&ssl=1)
And when importing the transfer data choose _Run without validation_.
The database is created and the invalid data from the transfer file are imported. 
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/importedproject695f.png?resize=750%2C363&ssl=1)
> More information how to import models and transfer files in general you can find in the [official Model Baker documentation](<https://opengisch.github.io/QgisModelBaker/user_guide/import_workflow/>) or in this [blog post.](<../../../../2021/12/07/model-baker-6-7-noch-nie-wars-so-einfach/index.html>)
### Let’s validate
Now open the Data Validator panel with  _Database > Model Baker > Data Validator_.
There the current database is found according to the active layer. In our example, we have only one database, but if you use more than one in the same QGIS project, the Data Validator will recognize the source of the current layer.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/15dfd.png?resize=750%2C450&ssl=1)
After performing the validation we receive 14 errors. Geometry intersections, wrong formatted TIDs, out-of-range values and others. Actually, these are not many errors, still, sometimes you might want to separate the kind of errors that are found to keep the overview.
### Filtering data
Let’s start with the separation of the data and later we separate the kinds of errors. You can do it by filtering the data either by _models_ or _datasets_ or _baskets_. You can choose multiple of them, but only one kind of filter. Let’s validate only the data of the basket considering the TOPIC `nature`.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/25dfd.png?resize=750%2C450&ssl=1)
We have three intersection issues and one type error.
### Skip geometry errors
When the checkbox is activated, geometry errors are ignored and the validation of area topology is disabled. Errors like those will not be listed:
  - Intersecting geometries
  - Duplicate coordinates
  - Overlaying geometries


> In the back end the parameters `--skipGeometryErrors` and `--disableAreaValidation` are passed to ili2db.
After performing the validation only the error with the TID is left.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/35dfd.png?resize=750%2C450&ssl=1)
### Analise the error
Before we go narrowing down the error message by disabling constraints, let’s have a look at the fixing part. The error we see above tells us the TID needs to be a UUID but it is a string: “velopark_id”
The TID is the OID defined in the model like this:
    
    OID AS INTERLIS.UUIDOID;
In the physical model, it’s represented by the column called `t_ili_tid`.
With  _right-click_ in the Data Validator on the error a menu is opened with the following options:
– Zoom to coordinates (if coordinates are provided) with an extent of 10 map units  
– Open in Feature Form (if a stable `t_ili_tid` is available)  
– Select in Attribute Table (if a stable `t_ili_tid` is available)  
– Set to fixed (marking the entry mark green to have organize the fixing process)  
– Copy (to copy the message text)
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/45dfd.png?resize=750%2C450&ssl=1)
On opening the form, we see that we don’t have any possibility of changing the t_ili_tid. Since it’s an auto-generated value, Model Baker did not set it to the visible fields on creating the form. We would need to display it by clicking on the  _Layer > Properties… > Attribute Form_ or we use the other option to _Select in Attribute Table_.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/55dfd.png?resize=750%2C450&ssl=1)
Now we can use the QGIS Field Calculator to set a UUID on the `t_ili_tid` of the currently selected feature (the feature in question).
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/6bebf.png?resize=750%2C490&ssl=1)
After validating again, the error disappears.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/72cd1.png?resize=750%2C449&ssl=1)
Valid. But of course, there are still the geometry errors as well as all the errors we had in the other TOPIC `living`.
### Fixing geometry errors
Let’s have a look at the geometry errors. 
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/82cd1.png?resize=750%2C449&ssl=1)With _right-click_ > Zoom to Coordinates the canvas zoom to the coordinates in question and highlights them. 
To fix intersections as well as duplicate errors, the QGIS _Vertex Tool_ can be used. ![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Screenshot-from-2022-11-08-14-14-5630db.png?resize=44%2C34&ssl=1)As well the _Vertex Editor_ is very helpful.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Screenshot-from-2022-11-07-17-14-022cd1.png?resize=750%2C449&ssl=1)
### Navigating through the errors
With the three symbols on the bottom left you can navigate through the features and coordinates in the error list, like you are used to it in the attribute table. ![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/grafikfc12.png?resize=112%2C30&ssl=1)
Most of the errors concerning a value can be fixed comfortably by the tools provided with _right-click_ _> Open in Feature Form / Select in Attribute Table_.
### Using Config File with meta attributes
The possibility to skip the error messages is quite present. But there are much more possibilities to narrow down the errors by skipping more specific checks. 
To have all the validation functionalities available you can load a Config File (INI) the Data Validator passes to ili2db. In this Config File, meta attributes can be defined to enable / disable specific checks as well as naming and describe constraints in a more readable format. The basics are described [here](<https://opengisch.github.io/QgisModelBaker/user_guide/validation/#using-of-meta-attributes-in-the-validation>). Let’s continue in this post with the example.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Screenshot-from-2022-11-07-17-41-33f09e.png?resize=750%2C446&ssl=1)
#### Global parameters
    
    ["PARAMETER"]
    multiplicity="off"
    constraintValidation="off"
By disabling the `multiplicity` we disable mandatory constraints and cardinality checks on associations. By disabling `constraintValidation` all the defined logical constraints are not considered.
> See all the possible meta attributes in the official [documentation of ilivalidator](<https://github.com/claeis/ilivalidator/blob/master/docs/ilivalidator.rst#interlis-metaattribute>).
#### Specific class / attribute parameters
The errors that are left are type errors. A value in `Levels` that is too high (see in the Model: `Levels: 0 .. 200;`) then the error with control characters (mostly because of using multiple lines in normal `TEXT`) in the attribute `Description` and the values in `Email` that are not in the requested `INTERLIS.URI `format.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Screenshot-from-2022-11-07-17-53-3671ea.png?resize=750%2C237&ssl=1)
We can disable them by referencing the attribute in question with the format `Model.Topic.Attribute`:
    
    ["ModernCity_V1.Living.Building.Levels"]
    type="off"
    ["ModernCity_V1.Living.Building.Description"]
    type="off"
    ["ModernCity_V1.Living.Resident.Email"]
    type="off"
> See for all the global configurations the official [documentation of ilivalidator](<https://github.com/claeis/ilivalidator/blob/master/docs/ilivalidator.rst#ini-globale-konfigurationen>).
#### Add constraint description and name with meta attributes
Finally, let’s take a look at something particularly beautiful. 
This constraint here in the model is a logical constraint. It’s neither implemented in the physical database nor the validator can recognize what it means:
    
              Name: TEXT;
              IsHuman: BOOLEAN;
              SET CONSTRAINT WHERE IsHuman:
                DEFINED(Name);
It means that if the boolean value `IsHuman` is true, `Name` must not be NULL. Anyway, the validator output would be like this:
`Set Constraint ModernCity_V1.Living.Resident.Constraint1 is not true.`
Because we had in our example already a meta attribute defined, but in the model itself. It did not say Constraint1, but:
`Set Constraint ModernCity_V1.Living.Resident.MandatoryHumanName is not true.`
The definition in the model looks like this:
    
          !!@ name = MandatoryHumanName
          SET CONSTRAINT WHERE IsHuman:
            DEFINED(Name);
To define a better readable message you can use `!!@ ilivalid.msg` to define the complete error message as well.
But because normally the person doing the data validation is not the same as the person writing the model, these meta attributes are not in the model. So everyone can define his messages in the Config File, like this:
    
    ["ModernCity_V1.Living.Resident.Constraint1"]
    msg = "When the resident with the id {ID} is human, then it needs a name."
Notices that you can use other attribute values with curly brackets.
![](../../../../../../i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Screenshot-from-2022-11-08-13-54-17-1c767.png?resize=647%2C99&ssl=1)
## Well then, that’s it
For more information, check out the [Model Baker documentation.](<https://opengisch.github.io/QgisModelBaker/>)
Meanwhile happy baking and: Happy validating! ?‍?
### _Related_
