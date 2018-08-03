=================
 ``--db-filter``
=================

The main purpose of ``--db-filter`` is to avoid asking user which database he needs to use (he may not know it). This is implemented by checking HOST address, which was used.

For example, you have two independent websites, say ``shop1.example.com`` and ``shop2.example.com``, that point to the same odoo server with two databases. By using ``--db-filter``  you can configure odoo to use corresponding database depending on used host address. Check the documentation links below or jump to examples to find out how to do it.

Docs
====

Official documentation: https://www.odoo.com/documentation/master/setup/deploy.html#dbfilter

Core code: https://github.com/odoo/odoo/search?l=Python&q=%22def+db_monodb%22

Additional option: https://github.com/OCA/server-tools/tree/11.0/dbfilter_from_header

Examples
========

Single database
---------------

If you have a single database, you may set default filter::

    --db-filter=.*


Ignoring other databases
------------------------

To force odoo always use only one database, say ``mydb``, use following filter::

    --db-filter=^mydb$

Database names equal to hostname
--------------------------------
::

    --db-filter=^%h$

To use filter above, you must name databases equal to host address, for example:

* ``shop1.example.com`` -- name of the first database
* ``shop2.example.com`` -- name of the second database
* ``www.super-shop.example.com`` -- name of the third database
* ``it-projects.info`` -- name of the fourth database

.. warning:: this filter cannot work with and without ``www`` prefix at the same time

Database names equal to subdomain
---------------------------------
::

    --db-filter=^%d$

To use filter above, you must name databases equal to subdomain, for example if database name is ``shop``, then the filter will use it for any of following requests:

* ``shop.example.com``
* ``www.shop.example.com``
* ``shop.yourbrand.example``
* ``www.shop.yourbrand.example``
