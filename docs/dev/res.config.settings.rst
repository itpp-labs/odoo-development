res.config.settings
===================

From odoo/openerp/addons/base/res/res_config.py

    """ Base configuration wizard for application settings.  It provides support for setting
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

        The method ``execute`` provides some support based on a naming convention:

        *   For a field like 'default_XXX', ``execute`` sets the (global) default value of
            the field 'XXX' in the model named by ``default_model`` to the field's value.

        *   For a boolean field like 'group_XXX', ``execute`` adds/removes 'implied_group'
            to/from the implied groups of 'group', depending on the field's value.
            By default 'group' is the group Employee.  Groups are given by their xml id.
            The attribute 'group' may contain several xml ids, separated by commas.

        *   For a boolean field like 'module_XXX', ``execute`` triggers the immediate
            installation of the module named 'XXX' if the field has value ``True``.

        *   For the other fields, the method ``execute`` invokes all methods with a name
            that starts with 'set_'; such methods can be defined to implement the effect
            of those fields.

        The method ``default_get`` retrieves values that reflect the current status of the
        fields like 'default_XXX', 'group_XXX' and 'module_XXX'.  It also invokes all methods
        with a name that starts with 'get_default_'; such methods can be defined to provide
        current values for other fields.
    """


