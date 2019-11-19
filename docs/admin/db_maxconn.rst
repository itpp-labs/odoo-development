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

    File "/opt/odoo/vendor/odoo/cc/odoo/service/wsgi_server.py", line 128, in application
        return application_unproxied(environ, start_response)
    File "/opt/odoo/vendor/odoo/cc/odoo/service/wsgi_server.py", line 117, in application_unproxied
        result = odoo.http.root(environ, start_response)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 1331, in __call__
        return self.dispatch(environ, start_response)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 1300, in __call__
        return self.app(environ, start_wrapped)
    File "/opt/odoo/.local/lib/python3.7/site-packages/werkzeug/wsgi.py", line 766, in __call__
        return self.app(environ, start_response)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 1501, in dispatch
        result = ir_http._dispatch()
    File "/opt/odoo/vendor/odoo/cc/addons/auth_signup/models/ir_http.py", line 19, in _dispatch
        return super(Http, cls)._dispatch()
    File "/opt/odoo/vendor/odoo/cc/addons/web_editor/models/ir_http.py", line 22, in _dispatch
        return super(IrHttp, cls)._dispatch()
    File "/opt/odoo/vendor/odoo/cc/odoo/addons/base/models/ir_http.py", line 207, in _dispatch
        return cls._handle_exception(e)
    File "/opt/odoo/vendor/odoo/cc/odoo/addons/base/models/ir_http.py", line 174, in _handle_exception
        raise exception
    File "/opt/odoo/vendor/odoo/cc/odoo/addons/base/models/ir_http.py", line 203, in _dispatch
        result = request.dispatch()
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 840, in dispatch
        r = self._call_function(**self.params)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 351, in _call_function
        return checked_call(self.db, *args, **kwargs)
    File "/opt/odoo/vendor/odoo/cc/odoo/service/model.py", line 97, in wrapper
        return f(dbname, *args, **kwargs)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 344, in checked_call
        result = self.endpoint(*a, **kw)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 946, in __call__
        return self.method(*args, **kw)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 524, in response_wrap
        response = f(*args, **kw)
    File "/opt/odoo/vendor/odoo/cc/addons/auth_signup/controllers/main.py", line 21, in web_login
        response = super(AuthSignupHome, self).web_login(*args, **kw)
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 524, in response_wrap
        response = f(*args, **kw)
    File "/opt/odoo/vendor/odoo/cc/addons/web/controllers/main.py", line 484, in web_login
        values['databases'] = http.db_list()
    File "/opt/odoo/vendor/odoo/cc/odoo/http.py", line 1517, in db_list
        dbs = odoo.service.db.list_dbs(force)
    File "/opt/odoo/vendor/odoo/cc/odoo/service/db.py", line 379, in list_dbs
        with closing(db.cursor()) as cr:
    File "/opt/odoo/vendor/odoo/cc/odoo/sql_db.py", line 657, in cursor
        return Cursor(self.__pool, self.dbname, self.dsn, serialized=serialized)
    File "/opt/odoo/vendor/odoo/cc/odoo/sql_db.py", line 171, in __init__
        self._cnx = pool.borrow(dsn)
    File "/opt/odoo/vendor/odoo/cc/odoo/sql_db.py", line 540, in _locked
        return fun(self, *args, **kwargs)
    File "/opt/odoo/vendor/odoo/cc/odoo/sql_db.py", line 608, in borrow
        **connection_info)
    File "/usr/local/lib/python3.7/site-packages/psycopg2/__init__.py", line 130, in connect
        conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
    psycopg2.OperationalError: FATAL: sorry, too many clients already


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
