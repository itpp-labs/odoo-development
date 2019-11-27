=======================
 ``12.0-`` → ``13.0+``
=======================

New API
=======

.. code-block:: sh

    # @api.multi is deleted
    # https://github.com/odoo/odoo/commit/a8767716cfd14abc7f87204d4d180811f663b648
    find . -type f -name '*.py' | xargs sed -i '/@api.multi/d'
    
    # remove deprecated decorators
    # https://github.com/odoo/odoo/commit/c552fb7a618afe2feea2e0358ead9eb6ebff0c94
    find . -type f -name '*.py' | xargs sed -i '/@api.model_cr/d'
    find . -type f -name '*.py' | xargs sed -i '/@api.v8/d'
    find . -type f -name '*.py' | xargs sed -i '/@api.model_cr_context/d'
    find . -type f -name '*.py' | xargs sed -i '/@api.noguess/d'
    
    # view_type is deleted:
    # https://github.com/odoo/odoo/commit/3cd7ed07a29c89ddf193796c20a812b9bf21e284
    find . -type f -name '*.xml' | xargs perl -i -pe 's/\s*\<field name="view_type"\>form\<\/field\>\n//g'
    find . -type f -name '*.xml' | xargs perl -i -pe 's/view_type="form"//g'
    # TODO: script for python files
    
    # key2 is deleted, src_model is renamed
    # https://github.com/odoo/odoo/commit/10f1a1a0c45
    find . -type f -name '*.xml' | xargs sed -i 's/src_model="\([^"]*\)"/binding_model="\1"/g'
    find . -type f -name '*.xml' | xargs sed -i 's/key2="client_action_multi"//g'
    
    # ControlPanelMixin is deleted
    # https://github.com/odoo/odoo/commit/40dd1219385
    # delete line with require('web.ControlPanelMixin');
    find . -type f -name '*.js' | xargs sed -i '/web.ControlPanelMixin/d'
    find . -type f -name '*.js' | xargs perl -i -p0e 's/ControlPanelMixin, \{\n\s*template/{\n    hasControlPanel: true,\n    contentTemplate/g'
    
    
    
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
    find . -type f -name '*.py' | xargs sed -i "s/odoo.tools.pycompat.text_type/str/g"
    find . -type f -name '*.py' | xargs sed -i "s/tools.pycompat.text_type/str/g"
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

nvd3
====

The library is deleted: https://github.com/odoo/odoo/commit/596206cdf6d

Here are examples how to update code:

* Switch to Chart.js:

  * https://github.com/odoo/odoo/commit/3ab3082a326

external_dependencies
=====================

This manifest's attribute `should use pypi name <https://github.com/odoo/odoo/commit/795c7b0a9415d04a777e1a5d48921adbd72f38cf>`__, instead of python package. Which is the name you use on installing via ``pip install ...``, and not the name in python code like ``import ...`` 

company_ids in res.users
========================

The field ``company_ids`` is mandatory: https://github.com/odoo/odoo/commit/4205cb2728041487bd026bf5c6bac590e0ace1e9
