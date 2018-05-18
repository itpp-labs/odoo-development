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
* runs before marking module as installed, which also leads to not loading module's qweb without :doc:`fixing it manually <../js/phantom_js-test_cr>` (only for odoo before version 12). 

post_install
============
* runs after installing all modules in current installation set
* runs after calling ``registry.setup_models(cr)``
* runs after calling ``model._register_hook(cr)``
