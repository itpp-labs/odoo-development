res.config.settings
===================

*Based on* https://github.com/odoo/odoo/blob/9.0/openerp/addons/base/res/res_config.py

``res.config.settings`` is a base configuration wizard for application settings.  It provides support for setting
default values, assigning groups to employee users, and installing modules.
To make such a 'settings' wizard, define a model like::

    class my_config_wizard(osv.osv_memory):
        _name = 'my.settings'
        _inherit = 'res.config.settings'
        _columns = {
            'default_foo': fields.type(..., default_model='my.model'),
            'group_bar': fields.boolean(..., group='base.group_user', implied_group='my.group'),
            'module_baz': fields.boolean(...),
            'other_field': fields.type(...),
        }

The method ``execute`` (*Apply* button) provides some support based on a naming convention:

*   For a field like ``default_XXX``, ``execute`` sets the (global) default value of
    the field ``XXX`` in the model named by ``default_model`` to the field's value.

*   For a boolean field like ``group_XXX``, ``execute`` adds/removes 'implied_group'
    to/from the implied groups of 'group', depending on the field's value.
    By default 'group' is the group Employee.  Groups are given by their xml id.
    The attribute 'group' may contain several xml ids, separated by commas.

*   For a boolean field like ``module_XXX``, ``execute`` triggers the immediate
    installation of the module named ``XXX`` if the field has value ``True``.

*   For the other fields, the method ``execute`` invokes all methods with a name
    that starts with ``set_``; such methods can be defined to implement the effect
    of those fields.

The method ``default_get`` retrieves values that reflect the current status of the
fields like ``default_XXX``, ``group_XXX`` and ``module_XXX``.  It also invokes all methods
with a name that starts with ``get_default_``; such methods can be defined to provide
current values for other fields.

Example
-------
This for website.config.settings but it is similar to res.config.settings::

    class website_config_settings(models.TransientModel):
        _inherit = 'website.config.settings'
        nobill_noship = fields_new_api.Boolean("Pickup and pay at store")
        #When you press Apply
        def set_nobill_noship(self, cr, uid, ids, context=None):
            config_parameters = self.pool.get("ir.config_parameter")
            for record in self.browse(cr, uid, ids, context=context):
                config_parameters.set_param(cr, uid, "website_sale_checkout_store.nobill_noship", record.nobill_noship or '', context=context)
        #When page loads
        def get_default_nobill_noship(self, cr, uid, ids, context=None):
            nobill_noship = self.pool.get("ir.config_parameter").get_param(cr, uid, "website_sale_checkout_store.nobill_noship", default=False, context=context)
            return {'nobill_noship': nobill_noship}
    #website_sale_checkout_store - is your module


Update settings on module install
=================================

If you want config parameters, which are depended on the ``res.config.settings`` model will ba recomputed
after install some module you have to implement the following conditions:

default_XXX
-----------

TODO

group_XXX
---------

Create a record of the ``res.groups`` model, which is adds group(s) from "implied_group" parameter in the
``res.config.settings`` model to the "implied_ids" field in the group which is defined in the "group" parameter.

    <record model="res.groups" id="base.group_user">
        <field name="implied_ids" eval="[
            (4, ref('stock.group_production_lot')),
            (4, ref('product.group_uom'))
        ]"/>
    </record>

module_XXX
----------

Add module_name to the "depends" parameter in the ``__openerp__.py`` file
