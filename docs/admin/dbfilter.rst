=================
 ``--db-filter``
=================

Official documentation: https://www.odoo.com/documentation/master/setup/deploy.html#dbfilter

Additional option: https://github.com/OCA/server-tools/tree/11.0/dbfilter_from_header

Video Lessons:

* `Multi-database installation (TODO) <https://www.youtube.com/watch?v=TODO>`__ (Russian)

Tips
====

To force odoo to always use only one database, say ``mydb``, use following filter::

    --db-filter=^mydb$
