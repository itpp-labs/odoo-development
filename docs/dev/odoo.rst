Module structue
==========
__openerp__ file atributes
------------------------------------

Dependencies
^^^^^^^^^^^^

Check if some python library exists::

  external_dependencies': {'python' : ['openid']}


Check if some sytem application exists::

  external_dependencies': {'bin' : ['libreoffice']}

Odoo database
----------------------

Many to many
^^^^^^^^^
For every *many to many* field odoo creating new relations table for example *pos_multi_rel* with *_rel* postfix. 
