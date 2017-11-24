==================
 How to run tests
==================

This tests runs with following parameters:

*  ``-d $DB_CONTAINER``
*  ``-i $MODULE``
*  ``--test-enable``
*  ``--workers=0``


js tests
========

To run odoo with phantomjs tests you additionally you need:

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

* use a db which contains required modules (if you haven't got such db run new container with the key ``-i`` instead of ``-u``. ``-i`` installs required module with its dependencies, whereas ``-u`` update already installed module)
* OPTIONAL: stop main odoo container, but keep db container
* run new container, e.g.::

      docker run --rm --link $DB_CONTAINER:db \
      -v /something/at/host:/something/at/container \
      itprojectsllc/install-odoo:$ODOO_BRANCH-dev \
      -- -d $DATABASE_NAME -u $MODULE --test-enable --workers=0 --stop-after-init
