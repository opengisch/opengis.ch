---
title: "QGis Globe Plugin installer script – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2010-12-01T14:00:03+01:00"
lastmod: "2020-04-29T16:08:00+02:00"
categories:
  - "C++"
  - "GIS"
  - "Master Thesis"
  - "QGIS"
tags:
  - "QGis Globe"
  - "qgis.org"
source: "www.opengis.ch/it/2010/12/01/qgis-globe-plugin-installer-script/index.html"
---

Lately, thanks to ma Master Thesis, I’ve been co-working on the Globe Plugin for [QGis](<https://www.qgis.org/>)  
here my install script for a threaded version of QGis with the Globe Plugin. By now the Globe has stereo 3D support, keyboard navigation (try all the num key), mouse navigation, a gui to control the globe and datasets can be inported configuring the .earth file. Today I’ll start implementing a dialog to add data without the need of the .earth file.  
cheers Marco  
UPDATE: the script is now updated to use the new mutex trunk branch and tested on ubuntu natty  
UPDATE2: The script now uses the trunk repository of QGIS so it is actually not that usefull anymore since getting globe is just matter of compiling QGIS from source. I’ll leave it here for reference and “historic glory” 😉  
UPDATE3: Globe runs on WIN https://www.opengis.ch/2011/08/02/qgis-globe-runs-on-win/  
`#!/bin/sh  
#  
set -e  
#############################  
#######CONFIGURE HERE########  
#############################  
ROOT_DIR=~/globe  
SRC_DIR_NAME=qgis  
SRC_DIR=$ROOT_DIR/$SRC_DIR_NAME  
BUILD_DIR=$SRC_DIR/build  
INSTALL_DIR=~/apps  
GRASS_PREFIX=/usr/lib/grass64/lib  
#  
REPO='git://github.com/qgis/Quantum-GIS.git'  
DEV_REPO='git@github.com:YOURREPO/Quantum-GIS.git'  
#  
#############################  
#######END CONFIGURE#########  
#############################  
#  
echo "Downloading src to: " $SRC_DIR  
echo "Building src to: " $BUILD_DIR  
echo "Installing to: " $INSTALL_DIR  
#  
CONTINUE=n  
echo "OK? [y, n*]:"  
read CONTINUE  
CONTINUE=$(echo $CONTINUE | tr "[:lower:]" "[:upper:]")  
if [ "$CONTINUE" = "Y" ]; then  
continue  
else  
echo "Abort"  
exit  
fi  
#  
#add qgis repo needed to satisfy all dependences, we only compile qgis  
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable/  
sudo apt-get update  
sudo apt-get build-dep qgis  
sudo apt-get install cmake-curses-gui cmake-qt-gui gdal-bin libgdal1-1.8.0-grass txt2tags python-gdal git osgearth osgearth-dev openscenegraph  
#  
#get the source  
mkdir -p $ROOT_DIR  
cd $ROOT_DIR  
#  
DEV=n  
echo "Do you have write acces to the repo (have SSH key to it)? [y, n*]:"  
read DEV  
DEV=$(echo $DEV | tr "[:lower:]" "[:upper:]")  
if [ "$DEV" = "Y" ]; then  
echo "cloning $DEV_REPO"  
git clone $DEV_REPO $SRC_DIR_NAME  
else  
echo "cloning $REPO"  
git clone $REPO $SRC_DIR_NAME  
fi  
#  
cd $SRC_DIR  
git checkout master  
#  
mkdir -p $INSTALL_DIR  
mkdir -p $BUILD_DIR  
cd $BUILD_DIR  
ccmake -DCMAKE_INSTALL_PREFIX=$INSTALL_DIR -DGRASS_PREFIX=$GRASS_PREFIX -DCMAKE_BUILD_TYPE=Release -DWITH_GLOBE=ON ..  
#  
#detect cpu cores  
CORES=$(cat /proc/cpuinfo | grep processor | wc -l)  
make -j$CORES install  
#  
#run qgis  
#In some case you might need this 2 lines:  
#see https://code.google.com/p/modwsgi/wiki/InstallationIssues for details  
#LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libutil.so #use locate libutil to find the path  
#export LD_PRELOAD  
$INSTALL_DIR/bin/qgis  
`
### _Related_
