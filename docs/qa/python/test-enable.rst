==================
 How to run tests
==================

Use following parameters when you start odoo:

*  ``--test-enable``
*  ``-d $DB_CONTAINER``
*  ``-i $MODULE``
*  ``--workers=0``


js tests
========

To run tests with phantomjs tests you also need:

* `Install phantomjs <http://phantomjs.org/download.html>`_ or use dockers (see below)
* use ``--db-filter=.*``

.. TODO: Why?
.. * werkzeug must be 0.11.5 or higher


Docker users
============

You don't need to remove docker container to run test. You can run it in a separate container 

* don't worry about name for new container -- just use ``--rm`` arg
* No need to expose ports

So, to run tests with docker:

* use an odoo database which has required modules installed (otherwise it will test all dependencies too)
* OPTIONAL: stop main odoo container, but keep db container
* run new container, e.g.::

      docker run --rm --link $DB_CONTAINER:db \
      -v /something/at/host:/something/at/container \
      itprojectsllc/install-odoo:$ODOO_BRANCH-dev \
      -- \
      --test-enable \
      --workers=0 \
      --stop-after-init
      -d $DATABASE_NAME \
      -i $MODULE
