==============
 JS Autotests
==============

For automatic web tests odoo uses `phantomjs <http://phantomjs.org>`_.

**How to write automatic js tests:**

* Follow instruction for :doc:`python tests <../python/index>`
* If you have to make several steps in UI to test something:

  * Create :doc:`tour <../../description/js_tour>`
  * :doc:`Run tour via self.phantom_js() <tests-via-tours>`

* If just one step is enough:

  * Run you js code via :doc:`self.phantom_js() <phantom_js>`

**Documentation:**

.. toctree::
   :maxdepth: 3

   phantom_js
   tests-via-tours
   urls-and-waits-in-js-tours
   phantom_js-test_cr
   phantomjs-screenshots
   unittest-longpolling
