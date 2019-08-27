==========================
 at_install, post_install
==========================

By default, odoo runs test with paramaters::

        at_install = True
        post_install = False

at_install 
==========
* runs tests right after loading module's files. It runs only in demo mode.
* runs as if other not loaded yet modules are not installed at all
* runs before marking module as installed, which also leads to not loading module's qweb without `fixing it manually <https://github.com/odoo/odoo/blob/48dafd5/addons/point_of_sale/tests/test_frontend.py#L306-L311>`__ (don't forget to use :doc:`special environment <../js/phantom_js-test_cr>` in odoo before version 12) . 

post_install
============
* runs after installing all modules in current installation set
* runs after calling ``registry.setup_models(cr)``
* runs after calling ``model._register_hook(cr)``
