==================
 Superuser rights
==================

Administrator, i.e. user with id 1 (``SUPERUSER_ID``), has exceptions about access rights.

ir.model.access
===============

If some model doesn't have records in :doc:`ir.model.access (Access Rules)<../../odoo/models/ir.model.access>`, then only Administrator has access to that model.

.. note:: Official documentation `states <https://www.odoo.com/documentation/9.0/reference/security.html>`_ "record rules do not apply to the Administrator user although **access rules do**" seems to be **wrong**. Access Rules don't to apply to Administrator too. See the source: `8.0 <https://github.com/odoo/odoo/blob/8.0/openerp/addons/base/ir/ir_model.py#L713>`_, `9.0 <https://github.com/odoo/odoo/blob/9.0/openerp/addons/base/ir/ir_model.py#L814>`_, `10.0 <https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/ir/ir_model.py#L892>`_, `11.0 <https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/ir/ir_model.py#L1139>`_
