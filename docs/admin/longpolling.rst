=============
 Longpolling
=============

`Longpolling <https://www.google.com/#q=longpolling>`_ is a way to deliver instant notification to web client (e.g. in chats).

To activate longpolling:

* install dependencies

  * odoo 11.0 ::

       python -c "import gevent" || sudo pip3 install gevent

  * odoo 10.0 ::

       python -c "import gevent" || sudo pip install gevent
       python -c "import psycogreen" || sudo pip install psycogreen

* set non-zero value for :doc:`workers <workers>` parameter
* configure nginx ::

    location /longpolling {
        proxy_pass http://127.0.0.1:8072;
    }
    location / {
        proxy_pass http://127.0.0.1:8069;
    }

* if you install odoo 9.0 via deb package, then you have to restore openerp-gevent file (see `#10207 <https://github.com/odoo/odoo/pull/10207>`_): ::

    cd /usr/bin/
    wget https://raw.githubusercontent.com/odoo/odoo/9.0/openerp-gevent
    chmod +x openerp-gevent


`Read more about longpolling <https://odoo-development.readthedocs.io/en/latest/admin/about_longpolling.html>`_

