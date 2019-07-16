.. note:: This article is obsolete and will be removed soon

===================
 Odoo installation
===================

.. contents::

.. note:: This article covers development installation only. For production installation follow https://github.com/it-projects-llc/install-odoo

Docker installation
===================

Install docker
--------------

Follow https://docs.docker.com/engine/installation/

Clone repositories
------------------

.. code-block:: shell

   cd /some/work/path

   ## Settings
   ODOO_BRANCHES=(11.0 10.0 9.0 8.0)  # update if needed
   GITHUB_USER=yelizariev  # change it to your user

   ## Common functions
   function init_repo {
     MAIN=$1
     NAME=$2
     if [ ! -d $NAME ]; then
       # clone
       git clone https://github.com/${MAIN}/${NAME}.git $NAME
       # rename
       git -C $NAME remote rename origin upstream
     fi

     # NAME origin over ssh
     git -C $NAME remote add origin git@github.com:${GITHUB_USER}/${NAME}.git

     for b in "${ODOO_BRANCHES[@]}"
     do
       DEST=odoo-$b/$NAME

       if [ ! -d $DEST ]; then
         # copy
         cp -r $NAME $DEST
         # checkout to branch
         git -C $DEST checkout upstream/$b
       fi
     done

     # clean up
     rm -rf $NAME
   }


   ## Create folder odoo-$b for each branch
   for b in "${ODOO_BRANCHES[@]}"
   do
     mkdir -p odoo-$b
   done

   ## Clone odoo
   init_repo odoo odoo

   ## Clone IT_PROJECTS_LLC_REPOS
   IT_PROJECTS_LLC_REPOS=(
   "pos-addons"
   "access-addons"
   "website-addons"
   "misc-addons"
   "mail-addons"
   "odoo-saas-tools"
   "odoo-telegram"
   )

   for r in "${IT_PROJECTS_LLC_REPOS[@]}"
   do
     init_repo it-projects-llc $r
   done

   ## Clone addons-dev
   init_repo it-projects-llc addons-dev
   for b in "${ODOO_BRANCHES[@]}"
   do
     git -C odoo-$b/addons-dev/ remote add misc-addons       https://github.com/it-projects-llc/misc-addons.git
     git -C odoo-$b/addons-dev/ remote add pos-addons        https://github.com/it-projects-llc/pos-addons.git
     git -C odoo-$b/addons-dev/ remote add mail-addons       https://github.com/it-projects-llc/mail-addons.git
     git -C odoo-$b/addons-dev/ remote add access-addons     https://github.com/it-projects-llc/access-addons.git
     git -C odoo-$b/addons-dev/ remote add website-addons    https://github.com/it-projects-llc/website-addons.git
     git -C odoo-$b/addons-dev/ remote add l10n-addons       https://github.com/it-projects-llc/l10n-addons.git
   done
    
Create dockers
--------------

.. code-block:: shell

   # Create postgres docker container. 
   # You create one per each odoo version or one per each project / module
   DB_CONTAINER=db-odoo-10
   docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo --name $DB_CONTAINER postgres:9.5

   ODOO_CONTAINER=some-container-name-for-odoo-10
   ODOO_BRANCH=10.0

   # Create docker without adding folders from host machine. 
   # Usually for demostration and testing, not for development.
   docker run \
   -p 8069:8069 \
   -p 8072:8072 \
   -e ODOO_MASTER_PASS=admin \
   --name $ODOO_CONTAINER \
   --link $DB_CONTAINER:db \
   -t itprojectsllc/install-odoo:$ODOO_BRANCH

   # Attach folder from host to make updates there (example for misc-addons).
   # It also runs odoo with "-d" and "--db-filter" parameters to work only with one database named "misc". 
   # It prevents running cron task on all available databases
   # In this example you need to add misc.local to /etc/hosts and open odoo via http://misc.local
   docker run \
   -p 8069:8069 \
   -p 8072:8072 \
   -e ODOO_MASTER_PASS=admin \
   -v /some/path/at/host-machine/with/clone-of-misc-addons-or-addons-dev/:/mnt/addons/it-projects-llc/misc-addons/ \
   --name $ODOO_CONTAINER \
   --link $DB_CONTAINER:db \
   -t itprojectsllc/install-odoo:$ODOO_BRANCH -- -d misc --db-filter ^%d$


   # Update all repos
   docker exec -t $ODOO_CONTAINER /bin/bash -c "export GIT_PULL=yes; bash /install-odoo-saas.sh"

   # Update odoo only
   docker exec -t $ODOO_CONTAINER git -C /mnt/odoo-source/ pull

   # Update misc-addons only
   docker exec -t $ODOO_CONTAINER git -C /mnt/addons/it-projects-llc/misc-addons pull

Control dockers
---------------

.. code-block:: shell

   # open docker terminal as odoo
   docker exec -i -t $ODOO_CONTAINER /bin/bash

   # open docker terminal as root
   docker exec -i -u root -t $ODOO_CONTAINER /bin/bash

   # watch logs
   docker attach $ODOO_CONTAINER

   # stop container
   docker stop $ODOO_CONTAINER

   # start container
   docker start $ODOO_CONTAINER

   # remove container (if you don't need one anymore or want to recreate it)
   docker rm $ODOO_CONTAINER

Straightforward installation
============================

.. warning:: This way is not recommended and script may be obsolete

.. code-block:: shell

   sudo apt-get update
   sudo apt-get install git python-pip htop moreutils tree nginx gimp wmctrl postgresql-server-dev-all
   sudo apt-get upgrade

   ###################  Github
   # configure ssh keys: https://help.github.com/articles/generating-ssh-keys/

   ###################  Odoo
   # download odoo from git:
   cd /some/dir/
   git clone https://github.com/odoo/odoo.git

   # install dependencies:
   wget http://nightly.odoo.com/9.0/nightly/deb/odoo_9.0.latest_all.deb
   sudo dpkg -i odoo_9.0.latest_all.deb  # shows errors -- just ignore them and execute next command:
   sudo apt-get -f install
   sudo apt-get remove odoo

   # install wkhtmltox
   cd /usr/local/src
   lsb_release -a
   uname -i
   # check version of your OS and download appropriate package
   # http://wkhtmltopdf.org/downloads.html
   # e.g.
   apt-get install xfonts-base xfonts-75dpi
   apt-get -f install
   wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb
   dpkg -i wkhtmltox-*.deb

   # requirements.txt
   cd /path/to/odoo
   sudo pip install -r requirements.txt
   sudo pip install watchdog

   # fix error with jpeg (if you get it)
   # uninstall PIL
   sudo pip uninstall PIL
   # install libjpeg-dev with apt
   sudo apt-get install libjpeg-dev
   # reinstall pillow
   pip install -I pillow
   # (from here https://github.com/odoo/odoo/issues/612 )

   # fix issue with lessc
   # install Less CSS via nodejs according to this instruction:
   # https://www.odoo.com/documentation/8.0/setup/install.html

   # create postgres user:
   sudo su - postgres -c "createuser -s $USER"

   # Create new config file if you don't have it yet:
   cd /path/to/odoo
   ./openerp-server --save

   # then edit it, e.g. via emacs
   emacs -nw ~/.openerp_serverrc
   # set dbfilter = ^%h$
   # set workers = 2 # to make longpolling\bus\im work

   # create different versions of conf file:
   cp ~/.openerp_serverrc ~/.openerp_serverrc-9
   cp ~/.openerp_serverrc ~/.openerp_serverrc-8


   ################### /etc/hosts
   # /etc/hosts must contains domains you use, e.g:
   sudo bash -c "echo '127.0.0.1 8_0-project1.local'  >> /etc/hosts"
   sudo bash -c "echo '127.0.0.1 8_0-project2.local'  >> /etc/hosts"
   sudo bash -c "echo '127.0.0.1 9_0-project1.local'  >> /etc/hosts"

   ################### nginx
   # put nginx_odoo.conf to /etc/nginx/sites-enabled/
   # delete default configuration:
   cd /etc/nginx/sites-enabled/
   rm default
   # restart nginx
   sudo /etc/init.d/nginx restart

   ################### run Odoo
   cd /path/to/odoo
   git checkout somebranch-or-revision
   git tag 8_0-honduras.local
   # everytime run odoo this way:
   git checkout 8_0-client1.local && ./odoo.py --config=/path/to/.openerp_serverrc-8
   # or
   git checkout 8_0-project1.local && ./odoo.py --config=/path/to/.openerp_serverrc-8 --auto-reload
   # or
   git checkout 9_0-project1.local && ./odoo.py --config=/path/to/.openerp_serverrc-9 --dev
   # etc.
   # then open database you need, e.g. (type http:// explicitly, because browser could understand it as search request)
   # http://8_0-client1.local/
   # (database name should be 8_0-client1.local )


Nginx configuration
===================

Working via nginx is recommended for any type of installation

.. code-block:: shell

    server {
           listen 80 default_server;
           server_name .local;

           proxy_buffers 16 64k;
           proxy_buffer_size 128k;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
           #proxy_redirect http:// https://;
           proxy_read_timeout 600s;
           client_max_body_size 100m;

           location /longpolling {
               proxy_pass http://127.0.0.1:8072;
           }

           location / {
               proxy_pass http://127.0.0.1:8069;
           }
   }
