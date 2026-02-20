---
title: "Blog – Pagina 22 – OPENGIS.ch"
date: "2011-02-22T01:52:18+01:00"
lastmod: "2020-04-29T16:08:00+02:00"
source: "www.opengis.ch/it/blog/page/22/index.html"
---

## [PyQT signals with arguments](<../../../2011/02/22/pyqt-signals-with-arguments/index.html> "PyQT signals with arguments")
so , here a snippet on how to use the different types of signals in PyQt: connect a signal from C++ QObject.connect(self.sender, SIGNAL(“signalName( Arg1TYPE, Arg2TYPE )”), self.slot) connect a signal from Python QObject.connect(self.sender, SIGNAL(“signalName” ), self.slot ) emit a signal in Python self.emit( SIGNAL( “signalName” ), arg1, arg2 ) emit a signal in c++ emit signalName( arg1, arg2 ); more: https://www.eurion.net/python-snippets/snippet/Connecting%20signals%20and%20slots.html
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../2011/02/22/pyqt-signals-with-arguments/index.html>) 2020-04-29
## [Qgis plugins starter plugin](<../../../2010/12/06/qgis-plugins-starter-plugin/index.html> "Qgis plugins starter plugin")
Today I published my first QGis Python plugin. It does allow to configure a list of available plugins actions to execute in one click. It is published in pyqgis contributed repository and the source is developed on My GitHub Cheers Marco
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../2010/12/06/qgis-plugins-starter-plugin/index.html>) 2020-04-29
## [QGis Globe Plugin installer script](<../../../2010/12/01/qgis-globe-plugin-installer-script/index.html> "QGis Globe Plugin installer script")
Lately, thanks to ma Master Thesis, I’ve been co-working on the Globe Plugin for QGis here my install script for a threaded version of QGis with the Globe Plugin. By now the Globe has stereo 3D support, keyboard navigation (try all the num key), mouse navigation, a gui to control the globe and datasets can be inported configuring the .earth file. Today I’ll start implementing a dialog to add data without the need of the[ Read more](<../../../2010/12/01/qgis-globe-plugin-installer-script/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../2010/12/01/qgis-globe-plugin-installer-script/index.html>) 2020-04-29
## [Ubuntu 10.10 maverick meerkat on eeepc 1005 HA](<../../../2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/index.html> "Ubuntu 10.10 maverick meerkat on eeepc 1005 HA")
WOW, today I realized that Ubuntu 10.10 maverick meerkat was out and that I missed it by couple of days… bad me!!! (btw you have to select “normal updates” instead of “long term release” in your update manager’s settings). After the update my little eeepc lookt great, and everything worked out of the box without installing a tray control (including wifi, webcam, sound, hotkeys, performance modes, ecc)!!! Great Job guys and the new unity theme[ Read more](<../../../2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/index.html>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [15 anni ago](<../../../2010/10/14/ubuntu-10-10-maverick-meerkat-on-eeepc-1005-ha/index.html>) 2020-04-29
## [Shell snippets](<../../../2010/03/23/shell-snippets/index.html> "Shell snippets")
for my reference: Find files containing some text: grep -lir “some text” /path/to/dir/*
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [16 anni ago](<../../../2010/03/23/shell-snippets/index.html>) 2020-04-29
## [Custom PHP 5.3.1 with APC and XDEBUG on (Dreamhost) Shared Host](<../../../2010/02/17/custom-php-5-3-1-with-apc-and-xdebug-on-dreamhost-shared-hosting/index.html> "Custom PHP 5.3.1 with APC and XDEBUG on \(Dreamhost\) Shared Host")
I’ve recently been setting up my new dreamhost for symfony projects deployment and the only thing the default PHP is missing is the support for APC (alternate php cache). [(altro…)](<../../../2010/02/17/custom-php-5-3-1-with-apc-and-xdebug-on-dreamhost-shared-hosting/index.html#more-116>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [16 anni ago](<../../../2010/02/17/custom-php-5-3-1-with-apc-and-xdebug-on-dreamhost-shared-hosting/index.html>) 2020-04-29
## [MySql World Database as YAML fixture](<../../../2009/10/10/mysql-world-database-as-yaml-fixture/index.html> "MySql World Database as YAML fixture")
For Symfony application I’m developing I needed all the Region separated by continent (7 continents model). I converted the MySql World Database (https://dev.mysql.com/doc/world-setup/en/world-setup.html) to a YAML NestedSet fixture file. I just had to make 4 minor changes to it: – rename the 3 continents that had region with the same name name (North America, South America, Antarctica) – rename the Micronesia/Caribbean region to Micronesia-Caribbean. thats’ all, enjoy the file Region.yml Marco
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [16 anni ago](<../../../2009/10/10/mysql-world-database-as-yaml-fixture/index.html>) 2020-04-29
## [eeepc 1005HA-H on its way](<../../../2009/09/17/eeepc-1005ha-h-on-its-way/index.html> "eeepc 1005HA-H on its way")
Yesterday I ordered a netbook, the asus eeepc 1005HA-H, today it arrived at my girlfriend’s place and she will bring it to Borneo (hence to me) next week. As soon as I get it i’ll get rid of the installed WinXp and install UNR (Ubuntu Netbook Remix). I’ll post the results here… ciao UPDATE: it works like a charm with 9.10
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [16 anni ago](<../../../2009/09/17/eeepc-1005ha-h-on-its-way/index.html>) 2020-04-29
## [Adapting doctrineexport.grt.lua to symfony standards](<../../../2009/09/17/adapting-doctrineexport-grt-lua-to-symfony-standards/index.html> "Adapting doctrineexport.grt.lua to symfony standards")
Using Mysql workbench to visually design a data model for a symfony application is pretty cool. Thanks to the guys of <https://code.google.com/p/mysql-workbench-doctrine-plugin/> you can export the model to a YAML file ready for Doctrine. [(altro…)](<../../../2009/09/17/adapting-doctrineexport-grt-lua-to-symfony-standards/index.html#more-99>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [16 anni ago](<../../../2009/09/17/adapting-doctrineexport-grt-lua-to-symfony-standards/index.html>) 2020-04-29
## [migrating wordpress from gengo to wpml](<../../../2009/08/15/migrating-wordpress-from-gengo-to-wpml/index.html> "migrating wordpress from gengo to wpml")
A client of mine used to have a multilingual blog using the Gengo plugin, which I consider by now unfortunatly dead. Fortunately, the guys at https://www.wpml.org did a great job creating a new plugin that works like a charm. [(altro…)](<../../../2009/08/15/migrating-wordpress-from-gengo-to-wpml/index.html#more-94>)
By [**Marco Bernasocchi**](<../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [16 anni ago](<../../../2009/08/15/migrating-wordpress-from-gengo-to-wpml/index.html>) 2020-04-29
## Paginazione degli articoli
[Precedenti](<../21/index.html>) [1](<../../index.html>) … [21](<../21/index.html>) 22 [23](<../23/index.html>) [Successivi](<../23/index.html>)
