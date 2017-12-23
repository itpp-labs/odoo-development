===============
 Terminal logs
===============

**Logs** from **terminal** *(in development environment)* or **log file** *(in production environment)* are primary source to find the reason of a problem.

To control output level use :doc:`- - log-handler <../admin/log-handler>`

Output format
=============

`Default format <https://github.com/odoo/odoo/blob/11.0/odoo/netsvc.py#L98>`__ is as following::

    %(asctime)s %(pid)s %(levelname)s %(dbname)s %(name)s: %(message)s

::

   2017-12-23 10:32:59,388 13  INFO  point_of_sale-10 werkzeug: 172.17.0.1 - - [23/Dec/2017 10:32:59] "POST /web/webclient/translations HTTP/1.0" 200 -
   asctime________________ PID LEVEL DB_NAME_________ NAME____  MESSAGE________________________________________________________________________________


Name
----

*Name* is argument of creation ``_logger`` object. Usually it's equal to
::

    _logger = logging.getLogger(__name__)

i.e. equal to package name

PID
---

*PID* is a process ID. E.g. ID of one of :doc:`worker <../admin/workers>` or :doc:`cron process <../admin/max_cron_threads>`

Message
-------

*Message* is anything passing to one of logging method, e.g. ``_logger.info(Message)``

