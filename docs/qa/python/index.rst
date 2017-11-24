==================
 Python Autotests
==================


**To add tests you need:**

* Create folder named **tests**
* Add ``__init__.py`` file
* Create file that name starts with **test_**
* Add test methods that names start from **test_**

.. warning:: you shall NOT import ``tests`` in module folder, i.e. do NOT add ``from . import tests`` to main ``__init__.py`` file

**Example**::

    from odoo.tests.common import TransactionCase

    class TestMessage(TransactionCase):
        at_install = True
        post_install = True

        def test_count(self):
            expected_value = self.do_something()
            actual_value = self.get_value()
            self.assertEqual(expected_value, actual_value)

        def do_something(self):

            ...

**Documentation:**

.. toctree::
   :maxdepth: 3

   test-enable
   unittest
   at_install-post_install
