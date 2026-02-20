---
title: "Installing Redmine on (bluehost) shared hosting – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2009-07-02T06:56:07+02:00"
lastmod: "2020-04-29T16:08:00+02:00"
categories:
  - "Web Development"
tags:
  - "qgis.org"
source: "www.opengis.ch/it/2009/07/02/installing-redmine-on-bluehost-shared-hosting/index.html"
---

Hi, here a script to install readmine 0.8.4 ([www.readmine.org](<https://redmine.org/>)) on a shared host that offers ruby on rails. enjoy
    
    #automatic install of redmine 0.8.4 (https://www.redmine.org/) on a shared server (tested on bluehost)
    #
    #AUTHOR: Marco Bernasocchi (https://www.bernawebdesign.ch)
    #LICENSE: https://www.gnu.org/licenses/gpl-3.0.html
    #
    #BEFORE starting:
    # - create an empty DB (using cpanel) and a DB user with full permissions on the db
    # - create a mail user used to send out mails (quota can be set to 1Mb since you just need to send mails with it)
    # - cd into the dir you want to install to. (for example /home/username/railsApps/redmine)
    #
    #AFTER (not mandatory):
    # - create a subdomain (in cpanel) for redmine and link it to the public folder in redmine
    # example:
    # 	delete the default created folder
    # 	rm -rf /home/username/public_html/redmine/
    #	create symlink to the public folder
    # 	ln -s /home/username/railsApps/redmine/public /home/username/public_html/redmine
    # now redmine is located at https://yoursubdomain.example.com
    # login: admin
    # passw: admin
    #set this vars
    #
    MY_DB="dbName"
    MY_DB_USER="dbUser"
    MY_DB_PASSW="dbPassw"
    MY_DOMAIN="example.com"
    MY_MAIL_SUBDOMAIN="mail."
    MY_MAIL_PORT="26"
    MY_MAILER="user+example.com"
    MY_MAILER_PASSW="mailPassw"
    #
    #get redmine 0.8.4
    wget https://rubyforge.org/frs/download.php/56909/redmine-0.8.4.tar.gz
    tar zxvf redmine-0.8.4.tar.gz
    rm redmine-0.8.4.tar.gz
    mv redmine-0.8.4/* .
    rmdir redmine-0.8.4
    #
    #use fastCGI dispatcher
    mv public/dispatch.fcgi.example public/dispatch.fcgi
    #
    #set some permissions
    chmod 700 public/dispatch.fcgi
    chmod 700 tmp
    chmod 700 log
    #
    #force production environnement
    sed 's|# ENV[|ENV[|g' config/environment.rb > TMPFILE && mv TMPFILE config/environment.rb
    #
    #create config/database.yml
    echo 'production:' > config/database.yml
    echo ' adapter: mysql' >> config/database.yml
    echo ' database: '$MY_DB >> config/database.yml
    echo ' host: localhost' >> config/database.yml
    echo ' username: '$MY_DB_USER >> config/database.yml
    echo ' password: '$MY_DB_PASSW >> config/database.yml
    echo ' encoding: utf8' >> config/database.yml
    #
    #create config/email.yml
    echo '# Outgoing email settings' > config/email.yml
    echo 'production:' >> config/email.yml
    echo '  delivery_method: :smtp' >> config/email.yml
    echo '  smtp_settings:' >> config/email.yml
    echo '    address: '$MY_MAIL_SUBDOMAIN$MY_DOMAIN >> config/email.yml
    echo '    port: '$MY_MAIL_PORT >> config/email.yml
    echo '    domain: '$MY_DOMAIN >> config/email.yml
    echo '    authentication: :login' >> config/email.yml
    echo '    user_name: '$MY_MAILER >> config/email.yml
    echo '    password: '$MY_MAILER_PASSW >> config/email.yml
    #
    #create app
    rake db:migrate RAILS_ENV="production"
    rake redmine:load_default_data RAILS_ENV="production"
    
If you plan to integrate with a repository don’t forget to check the settings>repositories tab, where it says “Fixing keywords”, it is a very cool function that allows you to automatically change the issue status by using keywords in the commit message.
### _Related_
