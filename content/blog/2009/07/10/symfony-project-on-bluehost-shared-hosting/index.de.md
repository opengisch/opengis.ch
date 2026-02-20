---
title: 'Symfony project on (bluehost) shared hosting – OPENGIS.ch'
date: 2009-07-10
slug: "symfony-project-on-bluehost-shared-hosting"
url: "/de/2009/07/10/symfony-project-on-bluehost-shared-hosting/"
source: "www.opengis.ch/de/2009/07/10/symfony-project-on-bluehost-shared-hosting/index.html"
---
So, I finally made it, set up a working [Symfony](<https://www.symfony-project.org/>) project (with SVN) on my bluehost shared hosting plan, this tutorial should work for other hosters with minor changes. What I wanted was to be able of using my account as a development server for a small group of developers that would automatically show the last revision of the SVN repository. I pushed the solution further and created on the same account two more subdomains for the staging and production server. Please note that this last point is not the best thing to do, but I did it since we don’t know yet where we will put our production server when the application will really go live. As well, small budget apps could be set up this way if you really want 3 environments and you can’t afford a better hosting solution. Finally I installed [Redmine](<https://www.redmine.org/>) so that we’ve a fully integrated development server with issues tracking, road-map, wiki, documentation and repository browsing.  
Please note that bluehost uses something that looks like chroot jails, but read [here](<https://trac.symfony-project.org/wiki/SharedHostingNotSecure>) for some concerns about symfony on shared hosts. Furthermore, i never use https in this tutorial, since I m using this as a test platform. As well this solution symlinks a www available folder to a folder outside public_html which could have some security implications. So remember security is as strong as the weakest link and YOU need to take care of it.
Since setting up the whole thing it was a bit of an hassle, here how I did it (you need ssh acces to your account):
  - Setup subdomains and working folders
  - Install Subversion (SVN)
  - Setup Subversion (SVN)
  - Setup Symfony (with doctrine ORM)
  - Cloning ./symfony for use over http
  - SVN post-commit hook
  - Install Redmine (not mandatory)


### Setup subdomains and working folders
I decided to have the following structure:
  - /home/YOURACCOUNT/DEDICATEDFOLDER/dev/ (dev.domain.com)
  - /home/YOURACCOUNT/DEDICATEDFOLDER/stage/ (stage.domain.com)
  - /home/YOURACCOUNT/DEDICATEDFOLDER/prod/ (domain.com)


each of this folders will be the root of the relative environment of the symfony project. This folders are NOT accessible from the web, we will create symlinks later for that purpose.
  - /home/YOURACCOUNT/public_html/dev/web
  - /home/YOURACCOUNT/public_html/stage/web
  - /home/YOURACCOUNT/public_html/addonDOMAIN_web (nb no prod)


In cpanel create the two subdomains (dev and stage) and point them to the relative folders in public_html (NB, I worked with an add-on domain so when i created it I just pointed it to addonDOMAIN_web, if you want to do it with your main domain, you should be able to do so with a redirection or so). Now we need to delete this folders and create the symlinks (remember you CAN point a symlink to a folder that does not exist [yet]).
    
    cd /home/YOURACCOUNT/public_html/
    rm -rf dev/web/ stage/web web/
    ln -s /home/YOURACCOUNT/DEDICATEDFOLDER/dev/web/ dev/web
    ln -s /home/YOURACCOUNT/DEDICATEDFOLDER/stage/web/ stage/web
    ln -s /home/YOURACCOUNT/DEDICATEDFOLDER/prod/web/ addonDOMAIN_web
    
You are done, now your (sub)domains point to the web folder of the symfony project. The free bite is that you can control the access to the /home/YOURACCOUNT/public_html/dev or stage folder with .htacces files so that your dev and stage environment are accessible only to who you want. 
### Install Subversion (SVN)
well, I had done this a while ago and I don’t recall exactly each step I did, but I successfully installed SVN 1.5.4. Just google for installing SVN on bluehost and there are plenty of blogs/forums discussing it. For example [here](<https://www.bluehostforum.com/showpost.php?p=67753&postcount=25>).
### Setup Subversion (SVN)
Once you have installed SVN, you are ready to go. Create a folder for your repos in your home and then your repository
    
    cd
    mkdir svnRepositories
    cd svnRepositories
    svnadmin create yourRepo
    
now your repo is accessible to you at 
    
    svn+ssh://YOURACCOUNT@domain.com/home/YOURACCOUNT/svnRepositories/yourRepo
To access this you will be prompted for your account password, which (of course) you don’t want to type every time nor give to other developer. Luckily enough SSH keys come handy.  
To avoid typing the password every time you want to connect to your account just set up a key pair for yourself and upload the public key to the server (this can be done very easily in cpanel or by coping the .pub file in .ssh on you account and by coping the key in the .ssh/authorized_keys AND .ssh/authorized_keys2 file – ervey key a new line).
Now, you could do the same for the other developers but this would mean granting them the full access to your account. Again, SSH comes very handy, do the same as above for each new developer BUT prepend this to their public key in the .ssh/authorized_keys AND .ssh/authorized_keys2 file:
    
    command="/home/YOURACCOUNT/bin/svnserve -t -r /home/YOURACCOUNT/svnRepositories/yourRepo --tunnel-user=DEVNAME",no-port-forwarding,no-agent-forwarding,no-X11-forwarding,no-pty
this will authorize the key only for svnserve (which is what we need to use svn) and specifies the svn username of the developer (if you plan on installing redmine, you will be able to map this to a redmine username).  
so, the .ssh/authorized_keys AND .ssh/authorized_keys2 file would look like this:
    
    ssh-rsa AAAB3NzaC1yc2EAAAABIwAAAQEA6mrAlzDrYE3xQTK/G0IzQGYvW0prZuKEgPlpc3iCuLmkUF20UVcixem45W7u5A3nJR2N953jNc3t0z93PK5bL2UsaLdQAy33XjovxhCdJjtXDaNUpIesh/n5po7XJ9DWH2gdIJGedtNiTLYTmpQzL9GM/30yEE4XXOjJGAxObsceNUt0lBINKOERYXoJFxvqSoU9Prs7dpRX9sEsAIX98rkDkEVEZIYNMbYOPiWNVbcnbMXLVEYwIxoz+8cbqeaiaWHL3k5pKjTeUzCd4a+YJ2zYQYREK8cNeanuCL6kvFv55nv1kf4KoWw7L8kvf3lLqZXnpShTKcHPfWI0cETd3Q== my id_rsa.pub
    command="/home/YOURACCOUNT/bin/svnserve -t -r /home/YOURACCOUNT/svnRepositories/yourRepo --tunnel-user=jonnyDev",no-port-forwarding,no-agent-forwarding,no-X11-forwarding,no-pty ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2qCnsU3zC0FN4fMXqd4hQbwc31Q3EGZk6ruWGEv/IyA+e2bnQJhR1pjCruQ3OeB9ZG3BlBNKXPcDZ9sRYbBjQ/Hs5FLTd/IhMUcrfZGB3mN0yQeAhFvbD4IXEfGsqVD8sO79S7LH5IPsHpJWthZxZ8fUPXi7u6OmbX/LS/xlXBf60uttlTuPBFAhpNoGeR75FSAFg0ZhW6NFhbBVplB2jrD3amEJBbSfD88GMmUngwtvGn5Lr7v/dEhXiAMa25BorA6086hn11aDFLTaGJnz7Ne/jdPwCeEobi40X5ZHmHW7/eyACpYmcoVBEph7wV5W+uJ09ZoLl//n/PLPYEpTpw== jonnyDev jonnyDev.pub
    
After this, you can access your account without password and the other developers can do the same but only for SVN purposes. The only difference is that the developers will have to use
    
    svn+ssh://YOURACCOUNT@domain.com/
to checkout and commit to the repository.
Now you should initialize your repository for example by creating the standard folders „trunk, branches, tags“.  
locally (not on the server) do:
    
    mkdir ~/tmp/
    cd ~/tmp/
    mkdir trunk branches tags
    svn checkout svn+ssh://YOURACCOUNT@domain.com/home/YOURACCOUNT/svnRepositories/yourRepo
    svn add *
    svn commit -m"initialize folder structure"
    rm ~/tmp/
Your repository is ready and you can tell your developers to check out the trunk (or whatever you want) with 
    
    svn co svn+ssh://YOURACCOUNT@domain.com/trunk localDir
### Setup Symfony (with doctrine ORM)
based on [Symfony tutorial](<https://www.symfony-project.org/jobeet/1_2/Doctrine/en/01>) and [this blog entry](<https://stereointeractive.com/blog/2008/12/10/starting-a-new-symfony-project/>)
Checkout the repository (probably only the trunk) to the folder you want your application to reside into, and cd into the trunk. All following comands will be performed from the root of the trunk directory (the root of our new symfony application).
    
    cd ~/symApps/trunk
    svn mkdir lib
    svn mkdir lib/vendor
    svn propedit svn:externals lib/vendor
after the propedit comand, an editor will open, enter 
    
    symfony https://svn.symfony-project.com/tags/RELEASE_1_2_7/
    #or the most uptodate tagged version
    #or symfony https://svn.symfony-project.com/branches/1.2/ if you want the DEV version
now commit your changes
    
    svn commit -m "added symfony as external in lib/vendor"
    svn update lib/vendor
Now check if symfony works:
    
    php lib/vendor/symfony/data/bin/check_configuration.php
    php lib/vendor/symfony/data/bin/symfony -V
this should print out some information on your configuration and the symfony version.
You are now ready to create the project 
    
    php lib/vendor/symfony/data/bin/symfony generate:project yourproject
and to create the frontend application
    
    symfony generate:app --escaping-strategy=on --csrf-secret=UniqueSecret frontend
For better portability, change the absolute path to the symfony installation to a relative one:
    
    // config/ProjectConfiguration.class.php
    require_once dirname(__FILE__).'/../lib/vendor/symfony/lib/autoload/sfCoreAutoload.class.php';
Now we put the project into SVN:
    
    rm -rf cache/*
    rm -rf log/*
    chmod 777 cache
    chmod 777 log
    svn add *
    svn propedit svn:ignore log #enter * in the editor
    svn propedit svn:ignore cache #enter * in the editor
    svn ci -m "creating project structure"
### Cloning ./symfony for use over http
Unfortunately, bluehost has no PDO on its CLI PHP, which means that we CAN’T run any doctrine tasks using the comand line… pretty annoying (how could reset the dev DB after each commit). To be able to perform this tasks we need to be able to call symfony using wget (or curl). To do so we create a symfony_dev.php file in the web folder of our project (like a controller, i suggest calling it *_dev.php so it won’t be deployed to the prod server by the deploy task) and a copy of ./symfony (named for example symfony.php) in the root of the project. To avoid an erro page to be displayed you need to add a line with an echo statement to Symfony.php like this:
    
    echo "CLI output: n";
    chdir(dirname(__FILE__));
    require_once(dirname(__FILE__).'/config/ProjectConfiguration.class.php');
    include(sfCoreAutoload::getInstance()->getBaseDir().'/command/cli.php');
The web/symfony_dev.php should look like that:

### SVN post-commit hook (or putting it all together)
The goal was to have a fresh snapshot of the dev site every time a commit is performed, that means that we need to customize our post-commit hook, so open up /home/YOURACCOUNT/svnRepositories/yourRepo/hooks/post-commit and add the following code:
    
    #!/bin/sh
    # POST-COMMIT HOOK
    REPOS="$1"
    REV="$2"
    #export the dev version of the site
    rm -rf /home/YOURACCOUNT/DEDICATEDFOLDER/dev/
    /home/YOURACCOUNT/bin/svn export file:///home/YOURACCOUNT/svnRepositories/yourRepo/trunk/ /home/YOURACCOUNT/DEDICATEDFOLDER/dev/
    #update the redmine(issues tracker) DB
    #ruby /home/YOURACCOUNT/railsApps/redmine/script/runner "Repository.fetch_changesets" -e production
    #move into dev project root
    cd /home/YOURACCOUNT/DEDICATEDFOLDER/dev/
    #initiate log.txt
    echo -e "###NEW COMMIT "$REPOS" rev:"$REV" "$(date -u +"%F_%T %Z")"n" > log.txt
    #reset application DB
    #calls the http version of ./symfony doctrine:build-all-reload --env=dev --no-confirmation
    wget -o log.tmp -O CLI_output.tmp --user=HTTPUSER_dev --password=PASSW https://dev.domain.com/symfony_dev.php?cmd=doctrine:build-all-reload%20--env=dev%20--no-confirmation
    cat log.tmp	>> log.txt
    cat CLI_output.tmp	>> log.txt
    rm -f log.tmp CLI_output.tmp
    echo -e "n" >> log.txt
    #clear symfony cache
    ./symfony cc >> log.txt
    #commit-email.pl "$REPOS" "$REV" commit-watchers@example.org
    #log-commit.py --repository "$REPOS" --revision "$REV"
    cat log.txt >> ../logs/dev/symfonyCommitlog.txt
    #cat log.txt
    rm -f log.txt
### Install Redmine (not mandatory)
Finally, to install redmine follow my [previous post](</02/installing-redmine-on-bluehost-shared-hosting/index.html>), disable the „autofetch commits“ option in the administration page (settings?tab=repositories) and uncomment the following line to your post-commit hook:
    
    ruby /home/fotolion/railsApps/redmine/script/runner "Repository.fetch_changesets" -e production
this will trigger the update of redmine’s DB after each commit. On the same page you can map redmine usersnames to svn usernames to have tight coupling even at this level.
### Conclusion
I’ve shown how to create a symfony development environment on a shared hosting where PDO is not available on the command line PHP. Furthermore I shown how to add it to subversion and how to integrate everything together thanks to redmine.  
now you are ready to do some „rock solid development on a shoestring“ 🙂  
enjoy Marco
### _Related_
