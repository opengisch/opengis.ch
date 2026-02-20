---
title: "SpaceMouse in Ubuntu 15.04 – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2015-10-14T14:59:46+02:00"
lastmod: "2020-04-29T16:05:41+02:00"
categories:
  - "3D"
  - "tech toys"
tags:
  - "qgis.org"
source: "www.opengis.ch/it/2015/10/14/spacemouse-in-ubuntu-15-04/index.html"
---

While preparing some 3D scenes for an exibition I discovered the SpaceMouse by 3dconnexion. A neat device we plan on installing in front of a projected globe.  
To get it to run in Ubuntu first get the drivers from [www.3dconnexion.eu/service/drivers.html](<https://www.3dconnexion.eu/service/drivers.html>)  
then  
`  
sudo apt-get install libmotif3  
mkdir -p /tmp/3D3dxware-linux  
cd /tmp/3D3dxware-linux  
cp ~/Downloads/3dxware-linux-v1-8-0.x86_64.tar.gz /tmp/3D3dxware-linux  
tar -xf 3dxware-linux-v1-8-0.x86_64.tar.gz  
sudo ./install-3dxunix.sh  
`  
answer yes, 4, yes.  
That’s it, you might get an error saying: “Red Hat EL 7 currently not supported for automatic driver startup.”. This is not a big deal as we can start the daemon by doing:  
`  
sudo /etc/3DxWare/daemon/3dxsrv -d usb &  
`  
to test if all works, launch  
`  
/tmp/xcube  
`  
I’ll play around more to see how it goes.  
For further, a bit older information, see [this post](<https://blog.philippklaus.de/2012/01/3dconnexion-spacemouse-pro-with-ubuntu-11-10/>)
### _Related_
