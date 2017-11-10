====================
 Basic python tests
====================

How to run tests
================
This tests runs with ``-d $DB_CONTAINER -u $MODULE --test-enable --workers=0`` parameters. 

Docker users
------------
You don't need to remove docker container to run test. You can run it in a separate container 

* don't worry about name for new container -- just use ``--rm`` arg
* No need to expose ports

So, to run tests with docker:

* use a db which contains required modules (if you haven't got such db run new container with the key ``-i`` instead of ``-u``. ``-i`` installs required module with its dependencies, whereas ``-u`` update already installed module)
* stop main odoo container, but keep db container
* run new container, e.g.::

      docker run --rm --link $DB_CONTAINER:db \
      -v /something/at/host:/something/at/container itprojectsllc/install-odoo:$ODOO_BRANCH-dev \
      -- -d $DATABASE_NAME -u $MODULE --test-enable --workers=0 --stop-after-init

How to make tests
=================

To make some tests do next steps:

* Create folder named **tests**
* Add __init__.py file
* Create file that name begins from **test_**
* Add test methods that names start from **test_**

.. warning:: you shall NOT import ``tests`` in module folder, i.e. do NOT add ``from . import tests`` to main ``__init__.py`` file

Example (will result testing error)::

    from odoo.tests.common import TransactionCase
    class TestMessage(TransactionCase):
        at_install = True
        post_install = True
        def test_count(self):
            self.assertEqual(1, 0)

Test class
==========

From `odoo/tests/common.py <https://github.com/odoo/odoo/blob/master/odoo/tests/common.py>`_::

    class BaseCase(unittest.TestCase):
        """
        Subclass of TestCase for common OpenERP-specific code.
        
        This class is abstract and expects self.registry, self.cr and self.uid to be
        initialized by subclasses.
        """
    
    class TransactionCase(BaseCase):
        """ TestCase in which each test method is run in its own transaction,
        and with its own cursor. The transaction is rolled back and the cursor
        is closed after each test.
        """
    
    class SingleTransactionCase(BaseCase):
        """ TestCase in which all test methods are run in the same transaction,
        the transaction is started with the first test method and rolled back at
        the end of the last.
        """
    
    class SavepointCase(SingleTransactionCase):
        """ Similar to :class:`SingleTransactionCase` in that all test methods
        are run in a single transaction *but* each test case is run inside a
        rollbacked savepoint (sub-transaction).
    
        Useful for test cases containing fast tests but with significant database
        setup common to all cases (complex in-db test data): :meth:`~.setUpClass`
        can be used to generate db test data once, then all test cases use the
        same data without influencing one another but without having to recreate
        the test data either.
        """
    
    class HttpCase(TransactionCase):
        """ Transactional HTTP TestCase with url_open and phantomjs helpers.
        """

at_install, post_install
========================
By default, odoo runs test with paramaters::

        at_install = True
        post_install = False

at_install 
----------
* runs tests right after loading module's files. It runs only in demo mode.
* runs as if other not loaded yet modules are not installed at all

post_install
------------
* runs after installing all modules in current installation set
* runs after calling ``registry.setup_models(cr)``
* runs after calling ``model._register_hook(cr)``

setUp and other methods
=======================

For more information see https://docs.python.org/2.7/library/unittest.html#test-cases

* ``setUp()`` -- Method called to prepare the test fixture. This is called immediately before calling the test method. It's recommended to use in ``TransactionCase`` and ``HttpCase`` classes
* ``setUpClass()`` -- A class method called before tests in an individual class run. setUpClass is called with the class as the only argument and must be decorated as a ``classmethod()``. It's recommended to use in ``SingleTransactionCase`` and ``SavepointCase`` classes

  .. code-block:: py

    @classmethod
    def setUpClass(cls):
        ...
* ``tearDown()``, ``tearDownClass`` -- are called *after* test(s). Usually are not used in odoo tests 

Assert Methods
==============
https://docs.python.org/2.7/library/unittest.html#assert-methods
