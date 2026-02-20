---
title: "qgis.org – Page 9 – OPENGIS.ch"
date: "2018-04-16T08:09:41+02:00"
lastmod: "2020-04-29T16:05:12+02:00"
source: "www.opengis.ch/fr/tag/qgis-org-fr/page/9/index.html"
---

## [Marco becomes QGIS.org Co-chair](<../../../../2018/04/16/marco-becomes-qgis-org-co-chair/index.html> "Marco becomes QGIS.org Co-chair")
We are very proud to announce that one of our founders and directors Marco Bernasocchi was elected as QGIS.org project steering committee (PSC) co-chair. With over 10 years of involvement with QGIS (he started working with QGIS 0.6) Marco will serve for the next two years as one of the[ Read more](<../../../../2018/04/16/marco-becomes-qgis-org-co-chair/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [8 ans ago](<../../../../2018/04/16/marco-becomes-qgis-org-co-chair/index.html>) 2020-04-29
## [Porting QGIS plugins to API v3 – Strategy and tools](<../../../../2018/04/13/porting-qgis-plugins-to-api-v3-strategy-and-tools/index.html> "Porting QGIS plugins to API v3 – Strategy and tools")
The Release of QGIS 3.0 was a great success and with the first LTR (3.4) scheduled for release this fall, it is now the perfect time to port your plugins to the new API. QGIS 3.0 is the first major release since September 2013 when QGIS 2.0 was released. During[ Read more](<../../../../2018/04/13/porting-qgis-plugins-to-api-v3-strategy-and-tools/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [8 ans ago](<../../../../2018/04/13/porting-qgis-plugins-to-api-v3-strategy-and-tools/index.html>) 2020-04-29
## [PostgreSQL back end solution for quality assurance and data archive](<../../../../2018/01/08/postgresql-back-end-solution-for-quality-assurance-and-data-archive/index.html> "PostgreSQL back end solution for quality assurance and data archive")
Did you know that the possibilities to make a full QGIS back end solution for quality assurance and archiving in PostgreSQL are immense? SQL has it’s well known limitations, but with a little bit creativity you can make quite nice solutions just using triggers and rules. In this post I’ll[ Read more](<../../../../2018/01/08/postgresql-back-end-solution-for-quality-assurance-and-data-archive/index.html>)
By [**Dave Signer**](<../../../../author/signedav/index.html> "Dave Signer"), [8 ans ago](<../../../../2018/01/08/postgresql-back-end-solution-for-quality-assurance-and-data-archive/index.html>) 2024-03-06
## [Interlis translation](<../../../../2017/12/01/interlis-translation/index.html> "Interlis translation")
Lately, I have been confronted with the need of translating Interlis files (from French to German) to use queries originally developed for German data. I decided to create an automated convertor for Interlis (version 1) Transfer Format files (.ITF) based on the existing cadastral data model from the Swiss confederation[ Read more](<../../../../2017/12/01/interlis-translation/index.html>)
By [**Mario Baranzini**](<../../../../author/marioba/index.html> "Mario Baranzini"), [8 ans ago](<../../../../2017/12/01/interlis-translation/index.html>) 2020-04-29
## [Best practices for writing Python QGIS Expression Functions](<../../../../2017/05/10/best-practices-for-writing-python-qgis-expression-functions/index.html> "Best practices for writing Python QGIS Expression Functions")
Recently there have been some questions and discussions about python based expression functions and how parameters like usesGeometry need to be used. So I thought I’d quickly write down how this works. There is some intelligence If the geometry or a column is passed in as a parameter you do not[ Read more](<../../../../2017/05/10/best-practices-for-writing-python-qgis-expression-functions/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [9 ans ago](<../../../../2017/05/10/best-practices-for-writing-python-qgis-expression-functions/index.html>) 2020-04-29
## [QGIS Expressions Engine: Performance boost](<../../../../2017/05/02/qgis-expressions-engine-performance-boost/index.html> "QGIS Expressions Engine: Performance boost")
Expressions in QGIS are more and more widely used for all kinds of purposes. For example the recently introduced geometry generators allow drawing awesome effects with modified feature geometries on the fly. The last days at the QGIS developer meeting 2017, I spent some time looking into and improving the[ Read more](<../../../../2017/05/02/qgis-expressions-engine-performance-boost/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [9 ans ago](<../../../../2017/05/02/qgis-expressions-engine-performance-boost/index.html>) 2020-04-29
## [QGIS2 compatibility plugin](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html> "QGIS2 compatibility plugin")
Lately I’ve been spending time porting a bigger plugin from QGIS 2.8 to 3 while maintaining 2.8 compatibility. You can find it at https://github.com/opengisch/qgis2compat/ and https://plugins.qgis.org/plugins/qgis2compat/ One code to rule them all. My target was to have to edit the source code as little as possible to simulate a lazy[ Read more](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 ans ago](<../../../../2016/09/19/qgis2-compatibility-plugin/index.html>) 2020-04-29
## [Updating PyQt signals that use lambda in QGIS with 2to3](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html> "Updating PyQt signals that use lambda in QGIS with 2to3")
Just for the sake of documenting things, when running qgis 2to3 on a plugin I encountered a tricky situation regarding signals. MYQGISDIR/scripts/2to3 -f signals -w my/plugin/path The original code: extra_arg = « my test argument » QObject.connect( action, SIGNAL( « triggered() »), lambda extra_arg=my_arg: show_extra_arg(extra_arg)) def do_load_project(extra_arg): print extra_arg # « my test argument » The[ Read more](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>)
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 ans ago](<../../../../2016/09/11/updating-pyqt-signals-that-use-lambda-in-qgis-with-2to3/index.html>) 2020-04-29
## [Using threads in QGIS python plugins](<../../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html> "Using threads in QGIS python plugins")
Here an example on how to work with threads in a consistent and clean manner in QGIS python plugins
By [**Marco Bernasocchi**](<../../../../author/mbernasocchi/index.html> "Marco Bernasocchi"), [9 ans ago](<../../../../2016/09/07/using-threads-in-qgis-python-plugins/index.html>) 2020-04-29
## [QGIS: Qt5 and Python3 migration, current state](<../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html> "QGIS: Qt5 and Python3 migration, current state")
Behind the scenes a lot has happened to get ready for Qt5 and Python3. On the same codebase that is becoming the next release QGIS 2.16. This is really a great thing since we can focus work on a single master branch and I’m very happy that we got so[ Read more](<../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>)
By [**Matthias Kuhn**](<../../../../author/mkuhn/index.html> "Matthias Kuhn"), [10 ans ago](<../../../../2016/05/04/qgis-qt5-and-python3-migration-current-state/index.html>) 2020-04-29
## Pagination des publications
[Précédent](<../8/index.html>) [1](<../../index.html>) … [8](<../8/index.html>) 9 [10](<../10/index.html>) … [19](<../19/index.html>) [Suivant](<../10/index.html>)
