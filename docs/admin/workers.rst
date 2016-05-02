===============
 ``--workers``
===============

Non-zero values for ``--workers`` activates Multiprocessing.

Multiprocessing increases stability, makes somewhat better use of computing resources and can be better monitored and resource-restricted.

* Number of workers should be based on the number of cores in the machine (possibly with some room for cron workers depending on how much cron work is predicted)
* Worker limits can be configured based on the hardware configuration to avoid
  resources exhaustion

.. warning:: multiprocessing mode currently isn't available on Windows

Longpolling
===========

Hidden feature of Multiprocessing is automatic run gevent process for longpolling support.

Longpolling is an extra proccess, i.e. if you have ``--workers=2`` then you will get 2 worker processes and 1 gevent process
