===========================
 Phantom_js + python tests
===========================

If you need you run some python code before or after calling ``phantom_js`` you shall not use ``self.env`` and you need to create new env instead::

    phantom_env = api.Environment(self.registry.test_cr, self.uid, {}) 

This is because ``HttpCase`` uses special cursor and using regular cursor via ``self.env`` leads to deadlocks or different values in database.
