---
title: "Porting QGIS plugins to API v3 – Strategy and tools – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2018-04-13T11:20:43+02:00"
lastmod: "2020-04-29T16:05:12+02:00"
categories:
  - "Featured"
  - "PyQt"
  - "Python"
  - "QGIS"
tags:
  - "qgis.org"
source: "www.opengis.ch/it/2018/04/13/porting-qgis-plugins-to-api-v3-strategy-and-tools/index.html"
---

The Release of QGIS 3.0 was a great success and with the first LTR (3.4) scheduled for release this fall, it is now the perfect time to port your plugins to the new API.  
QGIS 3.0 is the first major release since September 2013 when QGIS 2.0 was released. During the release cycles of all 2.x releases, the QGIS Python API remained stable. This means that a plugin or script meant to be used in QGIS 2.0 is still working in QGIS 2.18.  
The need for a new major release was principally motivated by the update to newer core libraries such as Qt 5 and Python 3. But it also offered a unique opportunity to the development team to tackle long-standing issues and limitations which could not be fixed during the 2.x life cycle. Inevitably, this introduced multiple backward incompatibilities making scripts and plugins unusable in QGIS 3.  
In this post, I’d like to share some notes from my latest ports. Obviously, if you need professional help for porting your plugins, don’t hesitate [to contact us](<../../../../../contact/index.html>).
# Step 0 – Unit tests
You should already have your code covered by unit tests, but I know, the world is not perfect and at times we have to cut edges and, unfortunately, often unit tests are the ones getting cut.  
Porting to a new API version is a great moment to go write unit tests helping to make sure that your plugin will keep on working as before the port.
# Step 1 – fix * imports
Before going on, please go and remove all your * imports (like from PyQt4.QtGui import *). They are bad and qgis2to3 cannot handle them. There is no need to already change them to the PyQ5 version, just remove them and add the propper PyQt4 imports. We’ll handle moving to PyQt5 in a later step.
> From PEP8: Wildcard imports (from  import *) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools.
# Step 2 – Versioning strategy
Since having a source code repository is a mandatory requirement for publishing a plugin on [plugins.qgis.org](<https://plugins.qgis.org/plugins/>), I assume you already know what code versioning is and [why you absolutely should be using it](<https://www.git-tower.com/learn/git/ebook/en/desktop-gui/basics/why-use-version-control>).
## APIv2 branch
Unless you absolutely want to make your code run on both API 2 and 3 (which _might_ be possible) I strongly suggest to create a branch or your current version called qgis2, API2 or legacy or whatever you want to call it. From now on this branch will be responsible for all your future (probably mainly bugfixes) releases for the 2.x series of QGIS. Remember to edit the metadata.txt file and add your minimum and maximum version (not mandatory but nice for clarity):
    
    qgisMinimumVersion=2.14
    qgisMaximumVersion=2.18
    
## Master branch
From now on your master branch will be where all your future development for the 3.x series will happen. Remember to edit the metadata.txt file and add your minimum version:
    
    qgisMinimumVersion=3.0
    
# Step 3 – install the helpers
We created a repository with two dedicated tools to help you migrate your QGIS 2 plugins to QGIS 3: `qgis2to3` and `qgis2apifinder`. Both tools are distributed as a single Python package installable via
    
    pip install qgis2to3
    
Please note that often for system-wide installation you need sudo.  
All the sources and more information can be found at <https://github.com/opengisch/qgis_2to3>
# Step 4 – Python 2 to Python 3 and PyQt4 to PyQt5
The `qgis2to3` tool is a copy of the files found in [QGIS scripts](<https://github.com/qgis/QGIS/tree/master/scripts>) to allow for quick downloading and simple installation without the need of downloading the whole QGIS repository. This is a set of fixers for the python `2to3` command that will update your Python 2 code to Python 3. The additional fixers will also take care of the PyQt4 to PyQt5 porting as well as some other things.  
Running the `qgis2to3` command will show a number of changes required. These changes can be applied with `-w` flag
    
    qgis2to3 -w /path/to/your/plugin
    
# Step 5 – Check for API v2 usages
The `qgisapi2finder` tool helps you find usages of the QGIS API version 2 and gives hints about potential required changes for API version 3.  
It is based on a machine parsing of <https://qgis.org/api/api_break.html> so the results are as good as the information there.  
Also, being a simple text parser, it just gives a hint where to look at. It is by no means a complete tool to find all the possible API incompatibility.  
Methods are matched using only their names and not their classes, so there might be various false positives. Also, if the same keyword has been edited in various classes, `qgisapi2finder` will show you all the available suggestions for that keyword.  
You can run `qgis2apifinder` to get hints on the existence of obsolete code requiring manual porting and suggestions on how to actually deal with it. Please note that `qgis2apifinder` does hide some very frequent words like [‘layout’, ‘layer’, ‘fields’] from the analysis. You can show those with the `--all` flag.
    
    qgis2apifinder --all /path/to/plugin
    qgis2apifinder --all /path/to/plugin/file.py
    
# Step 6 – update your code
From here on it is all looking at each hint, updating the code and rerunning your tests. A properly configured IDE (stay tuned) could also help in the process.  
Some more information can be found at [github.com/qgis/QGIS/wiki/Plugin-migration-to-QGIS-3](<https://github.com/qgis/QGIS/wiki/Plugin-migration-to-QGIS-3>)  
Also, take a look at the PyQGIS API documentation now online at [python.qgis.org/master](<https://python.qgis.org/master>).  
I hope this post and tool can help you porting your plugins to QGIS3 and again if you need professional help for porting your plugins, don’t hesitate [to contact us](<../../../../../contact/index.html>).
### _Related_
