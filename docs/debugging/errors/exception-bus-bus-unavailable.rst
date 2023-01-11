================================
 Exception: bus.Bus unavailable
================================

::

    Traceback (most recent call last):
    File "/odoo/odoo-server/odoo/http.py", line 650, in _handle_exception
      return super(JsonRequest, self)._handle_exception(exception)
    File "/odoo/odoo-server/odoo/http.py", line 310, in _handle_exception
      raise pycompat.reraise(type(exception), exception, sys.exc_info()[2])
    File "/odoo/odoo-server/odoo/tools/pycompat.py", line 87, in reraise
      raise value
    File "/odoo/odoo-server/odoo/http.py", line 692, in dispatch
      result = self._call_function(**self.params)
    File "/odoo/odoo-server/odoo/http.py", line 342, in _call_function
      return checked_call(self.db, *args, **kwargs)
    File "/odoo/odoo-server/odoo/service/model.py", line 97, in wrapper
      return f(dbname, *args, **kwargs)
    File "/odoo/odoo-server/odoo/http.py", line 335, in checked_call
      result = self.endpoint(*a, **kw)
    File "/odoo/odoo-server/odoo/http.py", line 936, in __call__
      return self.method(*args, **kw)
    File "/odoo/odoo-server/odoo/http.py", line 515, in response_wrap
      response = f(*args, **kw)
    File "/odoo/odoo-server/addons/bus/controllers/main.py", line 37, in poll
      raise Exception("bus.Bus unavailable")
    Exception: bus.Bus unavailable

Error above means you haven't configured :doc:`longpolling <../../admin/about_longpolling>` properly. Longpolling is
used for instant notifications and updates when multiple workers is enabled i.e number of workers set in the configuration file is greather than one. If you are sure that you don't need
it, you can ignore the error.

To fix the error check following page: :doc:`How to enable Longpolling in odoo <../../admin/longpolling>` 
