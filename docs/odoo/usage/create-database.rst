========================
 How to create database
========================

From UI
=======

To create new database open ``/web/database/manager``

8.0-
----

Database with dots
^^^^^^^^^^^^^^^^^^

Early version of odoo doesn't allow to create databases with dots. You can remove this restriction in two ways:

1. Updates sources::

    cd path/to/odoo
    sed -i 's/matches="[^"]*"//g' addons/web/static/src/xml/base.xml

2. update html code via *Inspect Element* tool

   TODO screenshot

From terminal
=============

9.0+
----

To create new database simple add ``-d`` parameter when you run odoo, e.g.::

    ./openerp-server -d database1

-- will create new database with name ``database1``


