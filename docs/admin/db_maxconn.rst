==================
 ``--db_maxconn``
==================

Here is definition from ``odoo/tools/config.py``

.. code-block:: py

        group.add_option("--db_maxconn", dest="db_maxconn", type='int', my_default=64,
                         help="specify the the maximum number of physical connections to posgresql")


More accurate explanantion of this option is as following:

   ``db_maxconn`` -- specify the the maximum number of physical connections to posgresql **per odoo process, but for all databases**

**How much process odoo runs?**

* :doc:`longpolling <longpolling>` -- no more than 1 process
* :doc:`workers <workers>`
* :doc:`max_cron_threads <max_cron_threads>`


**What it means practically?**

If you have deployment with big number of databases or simultaneous users you may face following error::

    2017-09-11 14:01:14,876 8676 ERROR ? odoo.service.server: Worker (8676) Exception occured, exiting...
    Traceback (most recent call last):
      File "/opt/odoo/10/odoo/service/server.py", line 721, in run
        self.process_work()
      File "/opt/odoo/10/odoo/service/server.py", line 791, in process_work
        db_names = self._db_list()
      File "/opt/odoo/10/odoo/service/server.py", line 784, in _db_list
        db_names = odoo.service.db.list_dbs(True)
      File "/opt/odoo/10/odoo/service/db.py", line 325, in list_dbs
        with closing(db.cursor()) as cr:
      File "/opt/odoo/10/odoo/sql_db.py", line 622, in cursor
        return Cursor(self.__pool, self.dbname, self.dsn, serialized=serialized)
      File "/opt/odoo/10/odoo/sql_db.py", line 164, in __init__
        self._cnx = pool.borrow(dsn)
      File "/opt/odoo/10/odoo/sql_db.py", line 505, in _locked
        return fun(self, *args, **kwargs)
      File "/opt/odoo/10/odoo/sql_db.py", line 573, in borrow
        **connection_info)
      File "/usr/local/lib/python2.7/dist-packages/psycopg2/__init__.py", line 164, in connect
        conn = _connect(dsn, connection_factory=connection_factory, async=async)
    OperationalError: FATAL:  remaining connection slots are reserved for non-replication superuser connections


To resolve it you need configure following parameters:

* In odoo

  * ``db_maxconn``
  * :doc:`workers <workers>`
  * :doc:`max_cron_threads <max_cron_threads>`

* In posgresql

  * `max_connections <https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-MAX-CONNECTIONS>`_

Those parameters must satisfy following condition:


.. code-block:: py

    (1 + workers + max_cron_threads) * db_maxconn < max_connections


For example, if you have following values:

* workers = 1 (minimal value to make longpolling work)
* max_cron_threads = 2 (default)
* db_maxconn = 64 (default)
* max_connections = 100 (default)

then ``(1 + 1 + 2) * 64 = 256 > 100``, i.e. the condition is not satisfied and such deployment may face the error described above.
