============================================================
 ValueError: External ID not found in the system: web.login
============================================================

::

    2019-05-28 08:51:28,012 13 INFO pr11 werkzeug: 172.17.0.1 - - [28/May/2019 08:51:28] "GET /web/login HTTP/1.0" 500 -
    2019-05-28 08:51:28,024 13 ERROR pr11 werkzeug: Error on request:
    Traceback (most recent call last):
      File "/usr/local/lib/python3.5/dist-packages/werkzeug/serving.py", line 205, in run_wsgi
        execute(self.server.app)
      File "/usr/local/lib/python3.5/dist-packages/werkzeug/serving.py", line 193, in execute
        application_iter = app(environ, start_response)
      File "/mnt/odoo-source/odoo/service/wsgi_server.py", line 166, in application
        return application_unproxied(environ, start_response)
      File "/mnt/odoo-source/odoo/service/wsgi_server.py", line 154, in application_unproxied
        result = handler(environ, start_response)
      File "/mnt/odoo-source/odoo/http.py", line 1319, in __call__
        return self.dispatch(environ, start_response)
      File "/mnt/odoo-source/odoo/http.py", line 1293, in __call__
        return self.app(environ, start_wrapped)
      File "/usr/local/lib/python3.5/dist-packages/werkzeug/wsgi.py", line 599, in __call__
        return self.app(environ, start_response)
      File "/mnt/odoo-source/odoo/http.py", line 1491, in dispatch
        result = ir_http._dispatch()
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_http.py", line 212, in _dispatch
        return cls._handle_exception(e)
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_http.py", line 182, in _handle_exception
        return request._handle_exception(exception)
      File "/mnt/odoo-source/odoo/http.py", line 771, in _handle_exception
        return super(HttpRequest, self)._handle_exception(exception)
      File "/mnt/odoo-source/odoo/http.py", line 310, in _handle_exception
        raise pycompat.reraise(type(exception), exception, sys.exc_info()[2])
      File "/mnt/odoo-source/odoo/tools/pycompat.py", line 87, in reraise
        raise value
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_http.py", line 208, in _dispatch
        result = request.dispatch()
      File "/mnt/odoo-source/odoo/http.py", line 830, in dispatch
        r = self._call_function(**self.params)
      File "/mnt/odoo-source/odoo/http.py", line 342, in _call_function
        return checked_call(self.db, *args, **kwargs)
      File "/mnt/odoo-source/odoo/service/model.py", line 97, in wrapper
        return f(dbname, *args, **kwargs)
      File "/mnt/odoo-source/odoo/http.py", line 338, in checked_call
        result.flatten()
      File "/mnt/odoo-source/odoo/http.py", line 1270, in flatten
        self.response.append(self.render())
      File "/mnt/odoo-source/odoo/http.py", line 1263, in render
        return env["ir.ui.view"].render_template(self.template, self.qcontext)
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_ui_view.py", line 1211, in render_template
        return self.browse(self.get_view_id(template)).render(values, engine)
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_ui_view.py", line 1118, in get_view_id
        return self.env['ir.model.data'].xmlid_to_res_id(template, raise_if_not_found=True)
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_model.py", line 1358, in xmlid_to_res_id
        return self.xmlid_to_res_model_res_id(xmlid, raise_if_not_found)[1]
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_model.py", line 1349, in xmlid_to_res_model_res_id
        return self.xmlid_lookup(xmlid)[1:3]
      File "<decorator-gen-21>", line 2, in xmlid_lookup
        
      File "/mnt/odoo-source/odoo/tools/cache.py", line 89, in lookup
        value = d[key] = self.method(*args, **kwargs)
      File "/mnt/odoo-source/odoo/addons/base/ir/ir_model.py", line 1338, in xmlid_lookup
        raise ValueError('External ID not found in the system: %s' % xmlid)
    ValueError: External ID not found in the system: web.login


The error above usually means that there was another problem on database initialization. So, if you got such error in test database, just drop the database, start database creation again and pay attention on logs for errors.

If you got such error in production database, then it could be difficult to fix that. Sorry ¯ \\ _ (ツ) _ / ¯
