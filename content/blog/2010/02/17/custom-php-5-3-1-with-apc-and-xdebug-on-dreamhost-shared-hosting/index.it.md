---
title: 'Custom PHP 5.3.1 with APC and XDEBUG on (Dreamhost) Shared Host – OPENGIS.ch'
date: 2010-02-17
slug: "custom-php-5-3-1-with-apc-and-xdebug-on-dreamhost-shared-hosting"
url: "/it/2010/02/17/custom-php-5-3-1-with-apc-and-xdebug-on-dreamhost-shared-hosting/"
source: "www.opengis.ch/it/2010/02/17/custom-php-5-3-1-with-apc-and-xdebug-on-dreamhost-shared-hosting/index.html"
---
I’ve recently been setting up my new dreamhost for symfony projects deployment and the only thing the default PHP is missing is the support for APC (alternate php cache). So after looking at the [dreamhost wiki](<https://wiki.dreamhost.com/index.php/Installing_PHP5>) I cleaned up and added some features to the [one of the install scripts](<https://wiki.dreamhost.com/index.php/Installing_PHP5#Improved_script_for_a_minimal_PHP_5.3.x_install_with_APC>). Here it is for your/mine (future) commodity.
    
    #!/bin/sh
    # update 16.2.2010
    # @author Marco Bernasocchi 
    # - Added OPENSSL LIBMCRYPT LIBTOOL and a promt for installing XDEBUG
    #   (still uses XDEBUG 2.05, which has basic PHP 5.3.1 support. 2.1.0 is on its way)
    # - removed unsupported php configure switches
    # - disabled --with-xsl, if you want to use it you'll probably need to install
    #   libxslt (https://xmlsoft.org/XSLT/) version 1.1.0 or greater.
    # - sets the ini files into the install directory instead than on cgi-bin
    # - to add more domains just copy the cgi binary to the new domain
    #   cp "$PHP_BIN_DIR/php-cgi" "$NEW_CGI_BIN_DIR/php.cgi" and modifiy the .htaccess
    #Script for a minimal PHP 5.3.x install with APC
    #
    #- Prompts for the domain to build for
    #- PHP configure line contains only valid PHP5 options
    #- Displays colourful status messages
    #- Many build messages, which aren't helpful to most people, are now suppressed
    #- Procedurised, making it cleaner and easier to follow
    #
    #The only things you may want to change in here are marked with "@todo"s
    #
    #Derived form the original PHP 5.3 install script at
    #https://wiki.dreamhost.com/Installing_PHP5
    #
    #@author Dan Bettles 
    #Exit on error
    set -e
    clear
    echo -n "Enter the domain for which you want to build PHP and press [ENTER]: "
    read DOMAIN
    echo -n "Enable XDEBUG (y|n): "
    read ENABLEXDEBUG
    #===============================================================================
    #@todo Update versions, if necessary
    M4="m4-1.4.13"
    AUTOCONF="autoconf-2.65"
    OPENSSL="openssl-0.9.8l"
    CURL="curl-7.20.0"
    LIBMCRYPT="libmcrypt-2.5.8"
    LIBTOOL="libtool-2.2.6b"
    PHP="php-5.3.1"
    APC="APC-3.1.3p1"
    XDEBUG="xdebug-2.0.5"
    #@todo Update install paths, if necessary
    WEB_ROOT="$HOME/$DOMAIN/web"
    CGI_BIN_DIR="$WEB_ROOT/cgi-bin"
    HTACCESS="$WEB_ROOT/.htaccess"
    INSTALL_DIR="$HOME/mycompiles"
    BUILD_DIR="$INSTALL_DIR/build"
    DOWNLOADS_DIR="$INSTALL_DIR/downloads"
    PHP_BASE_DIR="$INSTALL_DIR/$PHP"
    PHP_BIN_DIR="$PHP_BASE_DIR/bin"
    PHP_EXTENSIONS_DIR="$PHP_BASE_DIR/extensions"
    PHP_CONFIG_DIR="$PHP_BASE_DIR/etc/php5/config"
    PHP_INI="$PHP_CONFIG_DIR/php.ini"
    #@todo Alter features, if necessary
    PHP_FEATURES="--prefix=$PHP_BASE_DIR
     --with-config-file-path=$PHP_CONFIG_DIR
     --with-config-file-scan-dir=$PHP_CONFIG_DIR
     --bindir=$PHP_BIN_DIR
     --enable-zip
     --with-xmlrpc
     --with-freetype-dir=/usr
     --with-zlib-dir=/usr
     --with-jpeg-dir=/usr
     --with-png-dir=/usr
     --with-curl=$PHP_BASE_DIR
     --with-gd
     --enable-gd-native-ttf
     --enable-ftp
     --enable-exif
     --enable-sockets
     --enable-wddx
     --enable-sqlite-utf8
     --enable-calendar
     --enable-mbstring
     --enable-mbregex
     --enable-bcmath
     --with-mysql=/usr
     --with-mysqli
     --without-pear
     --with-gettext
     --with-pdo-mysql
     --with-openssl=$PHP_BASE_DIR
     #--with-xsl=$=$PHP_BASE_DIR
     --with-mcrypt=$PHP_BASE_DIR"
    #===============================================================================
    #@param string $1 Message
    function echoL1 () {
        echo -e "n 33[1;37;44m$1 33[0;0;0mn"
    }
    #@param string $1 Message
    function echoL2 () {
        echo -e "n 33[0;37;44m$1 33[0;0;0mn"
    }
    #@param string $1 URL
    #@param string $2 Output directory
    function downloadTo () {
        wget -c $1 --directory-prefix=$2
    }
    #@param string $1 TAR filename
    #@param string $2 Output directory
    function untarTo () {
        cd $2
        tar -xzf $1
        cd -
    }
    #@param string $1 Source directory
    #@param string $2 Output directory
    #@param string $3 configure arguments
    function configureAndMake () {
        cd $1
        COMMAND="./configure --quiet --prefix=$2 $3"
        if [ $1 = "$BUILD_DIR/$OPENSSL" ];then
          #special command for OPEN SSL
          COMMAND="./config --prefix=$2 $3"
        fi
        echo "$COMMAND"
        eval $COMMAND
        make --quiet
        cd -
    }
    #@param string $1 Source directory
    #@param string $2 Output directory
    #@param string $3 configure arguments
    function makeAndInstall () {
        configureAndMake $1 $2 "$3"
        cd $1
        make install --quiet
        cd -
    }
    #@param string $1 Directory
    function mkdirClean () {
        rm -rf $1
        mkdir -p $1
    }
    #@param string $1 Message
    function echoWarning () {
        echo -e "n 33[1;37;41m$1 33[0;0;0mn"
    }
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    export PATH="$PATH:$PHP_BIN_DIR"
    echoL1 "-> DOWNLOADING..."
    mkdirClean $BUILD_DIR
    echoL2 "--> Downloading $M4..."
    downloadTo "https://ftp.gnu.org/gnu/m4/$M4.tar.gz" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$M4.tar.gz" $BUILD_DIR
    echoL2 "--> Downloading $AUTOCONF..."
    downloadTo "https://ftp.gnu.org/gnu/autoconf/$AUTOCONF.tar.gz" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$AUTOCONF.tar.gz" $BUILD_DIR
    echoL2 "--> Downloading $OPENSSL..."
    downloadTo "https://www.openssl.org/source/$OPENSSL.tar.gz" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$OPENSSL.tar.gz" $BUILD_DIR
    echoL2 "--> Downloading $CURL..."
    downloadTo "https://curl.haxx.se/download/$CURL.tar.gz" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$CURL.tar.gz" $BUILD_DIR
    echoL2 "--> Downloading $LIBMCRYPT..."
    downloadTo "https://easynews.dl.sourceforge.net/sourceforge/mcrypt/$LIBMCRYPT.tar.gz" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$LIBMCRYPT.tar.gz" $BUILD_DIR
    echoL2 "--> Downloading $LIBTOOL..."
    downloadTo "https://ftp.gnu.org/gnu/libtool/$LIBTOOL.tar.gz" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$LIBTOOL.tar.gz" $BUILD_DIR
    echoL2 "--> Downloading $PHP..."
    downloadTo "https://www.php.net/get/$PHP.tar.gz/from/this/mirror" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$PHP.tar.gz" $BUILD_DIR
    echoL2 "--> Downloading $APC..."
    downloadTo "https://pecl.php.net/get/$APC.tgz" $DOWNLOADS_DIR
    untarTo "$DOWNLOADS_DIR/$APC.tgz" $BUILD_DIR
    if [ $ENABLEXDEBUG = "y" ]; then
      echoL2 "--> Downloading $XDEBUG..."
      downloadTo "https://xdebug.org/files/$XDEBUG.tgz" $DOWNLOADS_DIR
      untarTo "$DOWNLOADS_DIR/$XDEBUG.tgz" $BUILD_DIR
    fi
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    echoL1 "-> BUILDING..."
    mkdir -p $PHP_BASE_DIR
    echoL2 "--> Building $M4..."
    makeAndInstall "$BUILD_DIR/$M4" $PHP_BASE_DIR
    echoL2 "--> Building $AUTOCONF..."
    makeAndInstall "$BUILD_DIR/$AUTOCONF" $PHP_BASE_DIR
    echoL2 "--> Building $OPENSSL..."
    makeAndInstall "$BUILD_DIR/$OPENSSL" $PHP_BASE_DIR
    echoL2 "--> Building $CURL..."
    makeAndInstall "$BUILD_DIR/$CURL" $PHP_BASE_DIR "--enable-ipv6 --enable-cookies
     --enable-crypto-auth --with-ssl"
    echoL2 "--> Building $LIBMCRYPT..."
    makeAndInstall "$BUILD_DIR/$LIBMCRYPT" $PHP_BASE_DIR "--disable-posix-threads"
    echoL2 "--> Building $LIBTOOL..."
    makeAndInstall "$BUILD_DIR/$LIBTOOL" $PHP_BASE_DIR
    echoL2 "--> Building $PHP..."
    #Fixes compile error
    export EXTRA_LIBS="-lresolv"
    makeAndInstall "$BUILD_DIR/$PHP" $PHP_BASE_DIR "$PHP_FEATURES"
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    echoL1 "-> INSTALLING PHP..."
    mkdir -p -m 0755 $CGI_BIN_DIR
    mkdir -p -m 0755 $PHP_CONFIG_DIR
    cp "$PHP_BIN_DIR/php-cgi" "$CGI_BIN_DIR/php.cgi"
    cp "$BUILD_DIR/$PHP/php.ini-production" $PHP_INI
    mkdir -p $PHP_EXTENSIONS_DIR
    echoL2 "--> Building $APC..."
    APC_SOURCE_DIR="$BUILD_DIR/$APC"
    cd $APC_SOURCE_DIR
    $PHP_BIN_DIR/phpize
    configureAndMake $APC_SOURCE_DIR $PHP_BASE_DIR "--enable-apc --enable-apc-mmap
     --with-php-config=$PHP_BIN_DIR/php-config"
    cp modules/apc.so $PHP_EXTENSIONS_DIR
    echo "extension=$PHP_EXTENSIONS_DIR/apc.so" > $PHP_CONFIG_DIR/apc.ini
    cd -
    if [ $ENABLEXDEBUG = "y" ]; then
      echoL2 "--> Building $XDEBUG..."
      XDEBUG_SOURCE_DIR="$BUILD_DIR/$XDEBUG"
      cd $XDEBUG_SOURCE_DIR
      $PHP_BIN_DIR/phpize
      configureAndMake $XDEBUG_SOURCE_DIR $PHP_BASE_DIR "--enable-xdebug
       --with-php-config=$PHP_BIN_DIR/php-config"
      cp modules/xdebug.so $PHP_EXTENSIONS_DIR
      echo "zend_extension=$PHP_EXTENSIONS_DIR/xdebug.so" > $PHP_CONFIG_DIR/xdebug.ini
      cd -
    fi
    #-------------------------------------------------------------------------------
    if [ -f $HTACCESS ]; then
        HTACCESS_NEW="$HTACCESS.old"
        cp $HTACCESS $HTACCESS_NEW
        echoWarning "--> Copied $HTACCESS to $HTACCESS_NEW"
    fi
    #The backslash prevents a newline being inserted at the start
    HTACCESS_CONTENT="
    Options +ExecCGI
    AddHandler php-cgi .php
    Action php-cgi /cgi-bin/php.cgi
    #Deny access to the PHP CGI executable and config files
    
        Order Deny,Allow
        Deny from All
        Allow from env=REDIRECT_STATUS
    "
    #Preserve newlines in the content by quoting the variable name
    echo "#######ADDED BY installPHP script" >> $HTACCESS
    echo "$HTACCESS_CONTENT" >> $HTACCESS
    echoL2 "--> Created $PHP_INI"
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    rm -rf $BUILD_DIR
    echo -n "Delete the downloads directory? (y/n): "
    read DELETE_DOWNLOADS_DIR
    if [ $DELETE_DOWNLOADS_DIR = "y" ]; then
        rm -rf $DOWNLOADS_DIR
    fi
    echoL1 "DONE"
    exit 0
    
### _Related_
