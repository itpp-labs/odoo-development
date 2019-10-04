=======================
 ``12.0-`` → ``13.0+``
=======================

web_settings_dashboard
======================

``web_settings_dashboard`` is merged to ``base_setup`` https://github.com/odoo/odoo/commit/78565b1dc933692abba46a73f2298b7ea8e03c88

* ``[[ Settings ]] >> Dashboard`` is deleted!

Automatic update
----------------

.. code-block:: sh

    # update dependencies
    find . -type f -name __openerp__.py  -or -name __manifest__.py | xargs sed -i "s/web_settings_dashboard/base_setup/"

Processing old js file
----------------------

.. code-block:: sh

    # check for js files that like have to be deleted
    find . -type f -name "*.js" | xargs grep "require.*web_settings_dashboard"

If the code above gives non-empty output, you may need to do following updates:

* get rid of that js
* Move missed configuration to Settings menu (``res.config``)
