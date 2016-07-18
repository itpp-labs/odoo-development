Basic python tests
==================

This tests runs with ``-d [my_db] -u [module_to_be_tested] --test-enable`` key.
You can create records and call module methods and do some assertions.

To make some tests do next steps:

   * Create folder named **tests**
   * Add __init__.py file
   * Create file that name begins from **test_**
   * Add test methods that names start from **test_**

Example (will result testing error)::

    from openerp.tests.common import TransactionCase
    class test_message_count(TransactionCase):
        post_install = True
        def test_count(self):
            self.assertEqual(1, 0)

