---
title: 'The PostgreSQL Connection Service File and Why We Love It – OPENGIS.ch'
date: 2024-05-28
slug: "the-postgresql-connection-service-file-and-why-we-love-it"
url: "/fr/2024/05/28/the-postgresql-connection-service-file-and-why-we-love-it/"
source: "www.opengis.ch/fr/2024/05/28/the-postgresql-connection-service-file-and-why-we-love-it/index.html"
---
**_The PostgreSQL Connection Service File`pg_service.conf` is nothing new. It has existed for quite some time and maybe you have already used it sometimes too. But not only the new QGIS plugin [PG service parser](<https://github.com/opengisch/qgis-pg-service-parser-plugin>) is a reason to write about our love for this file, as well we generally think it’s time to show you how it can be used for really cool things._**
## **What is the Connection Service File?**
The Connection Service File allows you to save connection settings for each so-called “service” locally.
So when you have a database called `gis` on a local PostgreSQL with port `5432` and username/password is `docker`/`docker` you can store this as a service called `my-local-gis`.
    
    # Local GIS Database for Testing purposes
    
[my-local-gis] 
host=localhost port=5432 dbname=gis user=docker password=docker
This Connection Service File is called `pg_service.conf` and is by client applications (such as [psql](<https://www.postgresql.org/docs/current/app-psql.html>) or [QGIS](<https://qgis.org/en/site/>)) generally found directly in the user directory. In Windows it is then found in the user’s application directory `postgresql.pg_service.conf`. And in Linux it is by default located directly in the user’s directory `~/.pg_service.conf`. 
But it doesn’t necessarily have to be there. The file can be anywhere on the system (or on a network drive) as long as you set the environment variable `PGSERVICEFILE` accordingly:
    
    export PGSERVICEFILE=/home/dave/connectionfiles/pg_service.conf 
Once you have done this, the client applications will search there first – and find it.
If the above are not set, there is also another environment variable `PGSYSCONFDIR` which is a folder which is searched for the file `pg_service.conf`.
Once you have this, the service name can be used in the client application. That means in [psql](<https://www.postgresql.org/docs/current/app-psql.html>) it would look like this:
    
    ~$ psql service=my-local-gis
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    gis=#
And in QGIS like this:
![](./image38f5.png)
If you then add a layer in QGIS, only the name of the service is written in the project file. Neither the connection parameters nor username/password are saved. In addition to the security aspect, this has various advantages, more on this below.
But you don’t have to pass all of these parameters to a service. If you only pass parts of them (e.g. without the database), then you have to pass them when the connection is called:
    
    $psql "service=my-local-gis dbname=gis"
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    gis=#
You can also override parameters. If you have a database `gis` configured in the service, but you want to connect the database web, you can specify the service and explicit the database:
    
    $psql "service=my-local-gis dbname=web"
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    web=#
Of course the same applies to QGIS.
And regarding the environment variables mentioned, you can also set a standard service.
    
    export PGSERVICE=my-local-gis
Particularly pleasant in daily work with always the same database.
    
    $ psql
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    gis=#
## **And why is it particularly cool?**
There are several reasons why such a file is useful:
  - Security: You don’t have to save the connection parameters anywhere in the client files (e.g. QGIS project files). Keep in mind that they are still plain text in the service file.
  - Decoupling: You can change the connection parameters without having to change the settings in client files (e.g. QGIS project files).
  - Multi-User: You can save the file on a network drive. As long as the environment variable of the local systems points to this file, all users can access the database with the same parameters.
  - Diversity: You can use the same project file to access different databases with the same structure if only the name of the service remains the same.


For the last reason, here are three use cases.
### **Support-Case**
Someone reports a problem in QGIS on a specific case with their database. Since the problem cannot be reproduced, they send us a DB dump of a schema and a QGIS project file. The layers in the QGIS project file are linked to a service. Now we can restore the dump on our local database and access it with our own, but same named, service. The problem can be reproduced.
### **INTERLIS**
With INTERLIS the structure of a database schema is precisely specified. If e.g. the canton has built the physical database for it and configured a supernice QGIS project, they can provide the project file to a company without also providing the database structure. The company can build the schema based on the INTERLIS model on its own PostgreSQL database and access it using its own service with the same name.
### **Test/Prod Switching**
You can access a test and a production database with the same QGIS project if you have set the environment variable for the connection service file accordingly per [QGIS profile](<https://docs.qgis.org/3.34/de/docs/user_manual/introduction/qgis_configuration.html#user-profiles>).
You create two connection service files.
The one to the test database` /home/dave/connectionfiles/test/pg_service.conf`:
    
    [my-local-gis]
    host=localhost
    port=54322
    dbname=gis-test
And the one for the production database `/home/dave/connectionfiles/prod/pg_service.conf`:
    
    [my-local-gis]
    host=localhost
    port=54322
    dbname=gis-productive
In QGIS you create two profiles “Test” and “Prod”:
![](https://lh7-us.googleusercontent.com/P5tG5kloX-sTGLtJjItVhTwQzGjhMugMEhgkUTfUfO4jblPxurVHGRdRcMkH2BGLyMrAPNZtOdaRO5OzeMvxR4CUC38gY23c9uGjXPn_65qSRRddeohzlDU4bQdPlbg5q9yGozwMjzuz9GeP-CTCPN8)
And you set the environment variable for each profile `PGSERVICEFILE` which should be used (in the menu  _Settings > Options…_ and there under  _System_ scroll down to  _Environment_
![image](https://lh7-us.googleusercontent.com/BZQzdWMsz1dbNf43syK1wkViu_uiOjitDu3a2wnJw7NElQ-OyvVwc26BR2y9rIW7ol_ocLGPOeRhfsjliIj9yWhUYqColQnwIpGfwVcMX2kPtFebDymTlFJjmbxDehH9QJ2MshLFu5TaULQfgOW-VZk)
or
![image](https://lh7-us.googleusercontent.com/1KSjiGIKgFBxD13G7FYB_6wz6BRt2XbYmNJVdsgoCzptjN9K6PoR-Q5Ttxxnf6XAKXLYjWFL6PacuroU6klaW0EZJZtPDGVkLHPYQYUA1kACMMmJz7TZkQpGp-yvRaAaqN0j3sYJsZTXT2EXQACtdIc)
If you now use the service `my-local-gis` in a QGIS layer, it connects the database `prod` in the “Prod” profile and the database `test` in the “Test” profile.
## **The authentication configuration**
Let’s have a look at the authentication. If you have the connection service file on a network drive and make it available to several users, you may not want everyone to access it with the same login. Or you generally don’t want any user information in this file. This can be elegantly combined with the authentication configuration in QGIS.
If you want to make a QGIS project file available to multiple users, you create the layers with a service. This service contains all connection parameters except the login information.
This login information is transferred using QGIS authentication.
![image](https://lh7-us.googleusercontent.com/RGByDYJr2czDGs4XKQD6SzCbsgiM318UdYav1m0z9fzX9_vQcFNjnZ5zqqg2X5hQ6HnJhwNGuszKYPpVSE5L53mxrpSTlLhGw5J8TAOB43IhTXFJlfII3ICPmX9ztbEOlR-TpJrlW5jfOy42-Dbx_Os)
You also configure this authentication per QGIS profile we mentioned above. This is done via Menu  _Settings > Options…_ and there under  _Authentication_ :
![image](https://lh7-us.googleusercontent.com/nnQe3fm9iMDFxG5QCxV_kpeBKjiUUefXx5B0dcNvMF7v0ObW_5051hXBBldC_CKSTrNPblJzwDo0zK2aQBKyz9ZM_27wIPtOY1i7srhpJLMr84VHWevuy4F1hj93ZjzJXbAKlt80gw0HuHtHaqcuigQ)
(or directly where you create the PostgreSQL connection)
If you add such a layer, the service and the ID of the authentication configuration are saved in the QGIS project file. This is in this case `mylogin`. Of course this name must be communicated to the other users so that they can also set the ID for their login to `mylogin`.
Of course, you can use multiple authentication configurations per profile.
## **QGIS Plugin**
And yes, there is now a great plugin to configure these services directly in QGIS. This means you no longer have to deal with text-based INI files. It’s called [PG service parser](<https://github.com/opengisch/qgis-pg-service-parser-plugin>):
![image](https://lh7-us.googleusercontent.com/3JNSq_fmD2g33fLls2FGklpoCRo-M4Pyuts7z4dP56wKK7_tRj3hGyakJSQHTHBxWyQNkBfJQggaPl_InrOdY58b-6GN8eGBH9oOgJYLkq6XMApgGBrboR_FQ5dZwJZFiBpZZ4_oBg2_BTNUAGiuPkk)
It finds the connection service file according to the mentioned environment variables `PGSERVICEFILE` or `PGSYSCONFDIR` or at its default location.
As well it’s super easy to create new services by duplicating existing ones.
![](https://lh7-us.googleusercontent.com/FvLhRVplNNN5EGo8OYmED9L786WKZOxxBZy98wVnJq6vywqo_Ny2wHQaKUbcMMaiyEVTD8BNKAeD0kAY_4HgmJ39NvEF9z20PPlbwPNIgVFRXwNQTYn5KgGOzJ8iUGJ4PnY7l1y0rNzOTrdOqMtbcNY)
### And for the Devs
And what would a blog post be without some geek food? The back end of this plugin is published on [PYPI](<https://pypi.org/project/pgserviceparser/>) and can be easily installed with `pip install pgserviceparser `and then be used in Python.
For example to list all the service names. 
    
    >>> import pgserviceparser
    >>> pgserviceparser.service_names()
    ['my-local-gis', 'another-local-gis', 'opengisch-demo-pg']
Optionally you can pass a config file path. Otherwise it gets it by the mentioned mechanism.
Or to receive the configuration from the given service name as a dict.
    
    >>> pgserviceparser.service_config('my-local-gis')
    {'host': 'localhost', 'port': '54322', 'dbname': 'gis', 'user': 'docker', 'password': 'docker'}
There are some more functions. Check them out here on [GitHub](<https://github.com/opengisch/pgserviceparser>) or in the [documentation](<https://opengisch.github.io/pgserviceparser/>).
## Well then
We hope you share our enthusiasm for this beautiful file – at least after reading this blog post. And if not – feel free to tell us why you don’t in the comments 🙂
### _Related_
