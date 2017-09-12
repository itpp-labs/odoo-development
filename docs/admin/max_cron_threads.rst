========================
 ``--max-cron-threads``
========================

Here is definition from ``odoo/tools/config.py``

.. code-block:: py

        group.add_option("--max-cron-threads", dest="max_cron_threads", my_default=2,
                         help="Maximum number of threads processing concurrently cron jobs (default 2).",
                         type="int")
