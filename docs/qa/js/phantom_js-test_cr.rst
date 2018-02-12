===========================
 Phantom_js + python tests
===========================

Odoo 12.0+
==========

Since `Odoo 12.0 <https://github.com/odoo/odoo/commit/7ea4f13f16671b4361a42d668fb81c941a552468>`__ there is no any problem with mixing calling phantom_js and python code

Odoo 11.0-
==========

If you need you run some python code before or after calling ``phantom_js`` you shall not use ``self.env`` and you need to create new env instead::

    phantom_env = api.Environment(self.registry.test_cr, self.uid, {}) 

This is because ``HttpCase`` uses special cursor and using regular cursor via ``self.env`` leads to deadlocks or different values in database.
