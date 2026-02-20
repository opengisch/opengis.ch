---
title: "Sharing internet connection – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2011-10-01T03:39:43+02:00"
lastmod: "2020-04-29T16:06:56+02:00"
categories:
  - "Scripts"
tags:
  - "qgis.org"
source: "www.opengis.ch/fr/2011/10/01/sharing-internet-connection/index.html"
---

Today, for some bizarre reasons only my android phone was connecting to a WiFi. So I decided to use it as a tethered modem. The problem was that my friend Bruno could not use the net either, so since networkmanager ad-hoc networks were not working and it is our day off climbing we decided to keep our fingers trained on the keyboard.  
Here are two little scripts to create an adhoc Wifi and forward internet connection over it.  
enjoy Marco (and Bruno)  
Server:  
`#!/bin/sh  
WIFINAME=bernaadhocwifi  
KEY=keyneedtobe13 #key needs to be 5, 13 or 29 chars  
GWIP=192.168.0.1  
INTERFACE=wlan0  
INTERFACETOSHARE=usb0  
#  
#Uncomment get ip from android phone or anything you need  
#sudo ifconfig $INTERFACETOSHARE up  
#sudo dhclient $INTERFACETOSHARE  
#END CONFIG  
#  
sudo ifconfig $INTERFACE down  
sudo iwconfig $INTERFACE mode ad-hoc  
sudo iwconfig $INTERFACE essid $WIFINAME key s:$KEY  
sudo ifconfig $INTERFACE $GWIP netmask 255.255.255.0 up  
#Follow the above steps for another wireless card and set IP address in same subnet, say 192.168.0.2, and ping each other.  
#  
#Now to share the internet over wireless,  
sudo iptables -t nat -A POSTROUTING -o $INTERFACETOSHARE -j MASQUERADE  
#where usb0 is the connection you want to share  
#You also need to enable IP forwarding:  
sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"  
#Or, to enable permanently add the following line to /etc/sysctl.conf  
#net.ipv4.ip_forward=1  
#Some ISPs might limit the TTL so that you wont be able to share the internet. Fix:  
#sudo iptables -t mangle -A PREROUTING -j TTL --ttl-inc 1`  
Client  
`#!/bin/sh  
WIFINAME=bernaadhocwifi  
KEY=keyneedtobe13 #key needs to be 5, 13 or 29 chars  
IP=192.168.0.2  
GWIP=192.168.0.1  
INTERFACE=wlan0  
#END CONFIG  
#  
#Using the shared internet (in Linux)  
sudo ifconfig $INTERFACE down  
sudo iwconfig $INTERFACE mode ad-hoc  
sudo iwconfig $INTERFACE essid $WIFINAME key s:$KEY  
sudo ifconfig $INTERFACE $IP netmask 255.255.255.0 up  
#  
#Now to use the shared internet on another computer, set it to ad-hoc mode and assign IP address in the same subnet as described above and perform the following:  
#  
#Set the IP of computer sharing internet as gateway  
sudo route add default gw $GWIP  
#Set DNS server. We're using Google's DNS.  
sudo sh -c "echo 'nameserver 8.8.8.8' >> /etc/resolv.conf"`
### _Related_
