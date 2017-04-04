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
   ODOO_BRANCHES=(10.0 9.0 8.0)  # update if needed
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

   ## Clone odoo (fork odoo repo before executing: https://github.com/odoo/odoo )
   init_repo odoo odoo

   ## Clone IT_PROJECTS_LLC_REPOS
   # be sure that you have forks for repos below
   IT_PROJECTS_LLC_REPOS=(
   "pos-addons"
   "access-addons"
   "website-addons"
   "misc-addons"
   "mail-addons"
   "odoo-saas-tools"
   )

   for r in "${IT_PROJECTS_LLC_REPOS[@]}"
   do
     init_repo it-projects-llc $r
   done

   ## Clone addons-dev
   init_repo it-projects-llc addons-dev


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
