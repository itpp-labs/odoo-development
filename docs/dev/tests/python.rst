====================
 Basic python tests
====================

This tests runs with ``-d [my_db] -u [module_to_be_tested] --test-enable`` key. Also, you can add ``--stop-after-init --xmlrpc-port 8888`` to run tests simultaneously with usual (non-test) running.

To make some tests do next steps:

   * Create folder named **tests**
   * Add __init__.py file
   * Create file that name begins from **test_**
   * Add test methods that names start from **test_**

Example (will result testing error)::

    from openerp.tests.common import TransactionCase
    class TestMessage(TransactionCase):
        at_install = False
        post_install = True
        def test_count(self):
            self.assertEqual(1, 0)

Test class
==========

From `openerp/tests/common.py <https://github.com/odoo/odoo/blob/master/openerp/tests/common.py>`_::

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

        at_install = False
        post_install = True

``at_install`` - run tests right after loading module's files. It runs only in demo mode.

``post_install`` - run test after full installation process. It differs from ``at_install``, because 

* it runs after calling ``registry.setup_models(cr)``
* it runs after calling ``model._register_hook(cr)``

Assert Methods
==============
https://docs.python.org/2.7/library/unittest.html#assert-methods
