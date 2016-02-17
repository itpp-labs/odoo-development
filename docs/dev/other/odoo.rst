Module structue
===============

__openerp__ file atributes
--------------------------

Dependencies
^^^^^^^^^^^^

Check if some python library exists::

  external_dependencies': {'python' : ['openid']}


Check if some sytem application exists::

  external_dependencies': {'bin' : ['libreoffice']}

Odoo database
=============

Many to many
^^^^^^^^^^^^

For every *many to many* field odoo creating new relations table for example *pos_multi_rel* with *_rel* postfix. 

Odoo way of shaman
==================

What to do if something not work but should to
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Refresh page
#. Update module
#. Check openerp file **depends**, **demo** and other important fields
#. Check odoo config you use to run odoo. Especially adons paths
#. Uninstall and install again modules in depends
#. Clean browser cache
#. Carefully check logs. Look up if needed files loaded or not. May be some errors.
#. Create new base and install all modules.

Importan stuff
^^^^^^^^^^^^^^

If some java dont work add --workers=2 to your odoo launch script.
