===============
 Odoo unittest
===============

.. contents::
   :local:


Test classes
============

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
