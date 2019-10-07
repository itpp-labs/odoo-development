=======================
 ``12.0-`` → ``13.0+``
=======================

New API
=======

.. code-block:: sh

    # @api.multi is deleted
    # https://github.com/odoo/odoo/commit/a8767716cfd14abc7f87204d4d180811f663b648
    find . -type f -name '*.py' | xargs perl -i -pe 's/    \@api.multi\n//g'
    
    # view_type is deleted:
    # https://github.com/odoo/odoo/commit/3cd7ed07a29c89ddf193796c20a812b9bf21e284
    find . -type f -name '*.xml' | xargs perl -i -pe 's/\s*\<field name="view_type"\>form\<\/field\>\n//g'
    # TODO: script for python files
    
    
    # serialize_exception was move from odoo/http.py
    # https://github.com/odoo/odoo/commit/0d1407a715901ea06e9a7211c0e3dbe09fadb785
    # Following command fixes only partly. You need to do manually:
    # * delete imports
    # * replace TODO with self.env or request.registry
    find . -type f -name '*.py' | xargs sed -i "s/serialize_exception/TODO ['ir.http'].serialize_exception/g"
    
    # pycompat: support for python2 is deleted:
    # https://github.com/odoo/odoo/commit/758382b3a73da024d6e1dc04a474d2868223767a
    # You may need:
    # * delete pycompat importing manually
    find . -type f -name '*.py' | xargs sed -i "s/pycompat.text_type/str/g"
    find . -type f -name '*.py' | xargs sed -i "s/text_type/str/g"


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
