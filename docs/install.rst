Odoo installation
=================


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
   wget http://nightly.odoo.com/8.0/nightly/deb/odoo_8.0.latest_all.deb
   sudo dpkg -i odoo_8.0.latest_all.deb  # shows errors -- just ignore them and execute next command:
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
   ./openerp-server --save
   emacs -nw ~/.openerp_serverrc
   # set dbfilter = ^%h$
   # create different versions of conf file:
   cp ~/.openerp_serverrc ~/.openerp_serverrc-9
   cp ~/.openerp_serverrc ~/.openerp_serverrc-8
