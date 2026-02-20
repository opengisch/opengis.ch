---
title: "Creating non-versioned shared libraries for android – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2011-11-23T14:17:48+01:00"
lastmod: "2020-04-29T16:06:56+02:00"
categories:
  - "C++"
  - "GIS"
  - "QGIS"
tags:
  - "Android"
  - "Android NDK"
  - "Android Qt"
  - "qgis.org"
source: "www.opengis.ch/fr/2011/11/23/creating-non-versioned-shared-libraries-for-android/index.html"
---

While porting [QGIS](<https://android.qgis.org/> "QGIS for android") to android using necessitas I encountered the problem of versioned libs. Android does not support versioned libs and it is [not going to](<https://groups.google.com/forum/#!topic/android-ndk/_UhNpRJlA1k>). In the first vesions I used rpl -R -e libqgis_core.so.1.9.90 « libqgis_core.sox00x00x00x00x00x00x00 » $APK_LIBS_DIR and similar hacks to remove the version from the libs. But it was rather hacky. Then I found this [post by Tom Russo](<https://groups.google.com/d/topic/android-qt/zmtqbUz7KmI/discussion>) where he mentioned how he changed his build process to force non versioned libs. I wrote him with some questions and finally, thanks to his hints, I managed to create a fairly general patch for libtool to make it generate android compatible configure scripts. I sent the patch to libtool and we’ll see what they think.
    
    diff --git a/m4/libtool.m4 b/m4/libtool.m4
    index a9e20cf..a5cc8eb 100644
    --- a/m4/libtool.m4
    +++ b/m4/libtool.m4
    @@ -2642,8 +2642,17 @@ linux* | k*bsd*-gnu | kopensolaris*-gnu)
    version_type=linux # correct to gnu/linux during the next big refactor
    need_lib_prefix=no
    need_version=no
    - library_names_spec='${libname}${release}${shared_ext}$versuffix ${libname}${release}${shared_ext}$major $libname${shared_ext}'
    - soname_spec='${libname}${release}${shared_ext}$major'
    + case $host_os in
    + # This must be Linux Android ELF which has no support for versioned libs.
    + linux-android*)
    + library_names_spec='$libname${shared_ext}'
    + soname_spec='${libname}${shared_ext}'
    + ;;
    + *)
    + library_names_spec='${libname}${release}${shared_ext}$versuffix ${libname}${release}${shared_ext}$major $libname${shared_ext}'
    + soname_spec='${libname}${release}${shared_ext}$major'
    + ;;
    + esac
    finish_cmds='PATH="$PATH:/sbin" ldconfig -n $libdir'
    shlibpath_var=LD_LIBRARY_PATH
    shlibpath_overrides_runpath=no
Now, the problem is that this patch fixes libtool.m4 which is the file that is used when a project manager creates a configure script. So it will take time until libtool includes the patch, your project manager updates the configure script and so on. But, no problem, mean while you can just look for something similar in your configure file (I was very lucky using « this must be linux ELF » as search criteria) and replace it accordingly and reconfigure passing –host=arm-linux-androideabi (as you probably already do if you are reading this). I managed to crosscompile expat, gdal, geos, gsl, proj, libiconv and libcharset without version.  
QGIS uses libpq (postgres client) to connect to some services, but there is no hint in the configure script about soname_spec and library_names_spec, so I searched for SO_VERSION and found it set in Makefile.shlib and adapted it accordingly. Bottom line is that you need to search creatively for anything related to soname, SO_VERSION and similar.  
QGIS uses as well QWT, which is QMAKE based, in this case to generate non versioned libs it’s enough to add CONFIG += plugin to the .pro or .pri file.  
Finally, in CMAKE you need
    
    IF (NOT ANDROID)
      SET_TARGET_PROPERTIES(qgis_core PROPERTIES
        VERSION ${COMPLETE_VERSION}
        SOVERSION ${COMPLETE_VERSION}
      )
    ENDIF (NOT ANDROID)
    
in your CMakeList.txt and call cmake with -DANDROID  
Hope this helps and that more and more people port cool libs to android.  
Ciao Marco
### _Related_
