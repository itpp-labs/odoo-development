==============
 JS Autotests
==============

For automatic web tests odoo uses `phantomjs <http://phantomjs.org>`_.

**How to write automatic js tests:**

* Follow instruction for `python tests <../python/test-enable.html#docker-users>`_
* In test method make call `self.phantom_js() <../python/unittest>`_

**Documentation:**

.. toctree::
   :maxdepth: 3

   tests-via-tours
   phantom_js
   urls-and-waits-in-js-tours
   phantom_js-test_cr
   phantomjs-screenshots
