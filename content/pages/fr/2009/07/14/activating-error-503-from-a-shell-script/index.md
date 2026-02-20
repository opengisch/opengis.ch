---
title: "Activating error 503 from a shell script – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2009-07-14T14:19:15+02:00"
lastmod: "2020-04-29T16:08:00+02:00"
categories:
  - "Web Development"
tags:
  - "qgis.org"
source: "www.opengis.ch/fr/2009/07/14/activating-error-503-from-a-shell-script/index.html"
---

During deployment of a new version of a website you might want to have your server returning an error 503 (temporarily unavailable). You can easily do this by pointing your web folder to a php page that contains this:
    
    //server_down.php
    header("HTTP/1.1 503 Service Unavailable");
    echo "We are deploying a new version of NoSoapNoBubbles, the server is going to be down for a minute.";
if your webfolder is linked to another folder with a symlink (as I explained in my previous post [symfony project on bluehost shared hosting](<../../10/symfony-project-on-bluehost-shared-hosting/index.html>)) then you can just remove the link and add a new one pointing to the folder containing server_down.php. Remember to rename server_down.php index.php or to create an .htaccess file containing 
    
    DirectoryIndex server_down.php
so that server_down.php is shown as directory index.
This solution is more than fine, but I needed to access some files during deployment so I decided to use a combination of the approach above and .htaccess. When the web directory (of our dev site) is being wiped out, then I redirect using the link, when the directory is filled but I’m running DB tasks I redirect using .htaccess.
Since our deploy tasks are fully automated (happen on svn commit) here how to edit the .htaccess file using SED (stream editor).  
Activate redirection:
    
    if [ "$#" != "1" ]; then
      echo Invalid number of arguments, must be 1. >&2
      exit 1
    fi
    #
    HTACCESSPATH=$1 #path to the .htaccess file
    cp  $HTACCESSPATH/.htaccess $HTACCESSPATH/.htaccessTMP
    sed 's|#*RewriteCond %{REQUEST_URI} !server_down.php$|RewriteCond %{REQUEST_URI} !server_down.php$|' $HTACCESSPATH/.htaccessTMP > TMPFILE && mv TMPFILE $HTACCESSPATH/.htaccessTMP
    sed 's|#*RewriteCond %{REQUEST_URI} !always_available.php$|RewriteCond %{REQUEST_URI} !always_available.php$|' $HTACCESSPATH/.htaccessTMP > TMPFILE && mv TMPFILE $HTACCESSPATH/.htaccessTMP
    sed 's|#*RewriteRule ^(.*)$ /server_down.php [L]|RewriteRule ^(.*)$ /server_down.php [L]|' $HTACCESSPATH/.htaccessTMP > TMPFILE && mv TMPFILE $HTACCESSPATH/.htaccessTMP
    mv $HTACCESSPATH/.htaccessTMP $HTACCESSPATH/.htaccess
    Deactivate redirection:if [ "$#" != "1" ]; then
      echo Invalid number of arguments, must be 1. >&2
      exit 1
    fi
    #
    HTACCESSPATH=$1
    cp  $HTACCESSPATH/.htaccess $HTACCESSPATH/.htaccessTMP
    sed 's|RewriteCond %{REQUEST_URI} !server_down.php$|#RewriteCond %{REQUEST_URI} !server_down.php$|' $HTACCESSPATH/.htaccessTMP > TMPFILE && mv TMPFILE $HTACCESSPATH/.htaccessTMP
    sed 's|RewriteCond %{REQUEST_URI} !always_available.php$|#RewriteCond %{REQUEST_URI} !always_available.php$|' $HTACCESSPATH/.htaccessTMP > TMPFILE && mv TMPFILE $HTACCESSPATH/.htaccessTMP
    sed 's|RewriteRule ^(.*)$ /server_down.php [L]|#RewriteRule ^(.*)$ /server_down.php [L]|' $HTACCESSPATH/.htaccessTMP > TMPFILE && mv TMPFILE $HTACCESSPATH/.htaccessTMP
    mv $HTACCESSPATH/.htaccessTMP $HTACCESSPATH/.htaccess
### _Related_
