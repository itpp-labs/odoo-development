============
 JS Testing
============

Regular phantom JS tests
========================

For automatic web tests odoo uses `phantomjs <http://phantomjs.org>`_.

How to write automatic js tests:

* Follow instruction for `python tests <./python.html#docker-users>`_
* In test method make call ``self.phantom_js``


self.phantom_js()
-----------------

From `odoo/tests/common.py <https://github.com/odoo/odoo/blob/10.0/odoo/tests/common.py>`_:

.. code-block:: py

    def phantom_js(self, url_path, code, ready="window", login=None, timeout=60, **kw):
        """ Test js code running in the browser
        - optionnally log as 'login'
        - load page given by url_path
        - wait for ready object to be available
        - eval(code) inside the page
        To signal success test do:
        console.log('ok')
        To signal failure do:
        console.log('error')
        If neither are done before timeout test fails.
        """

i.e.

* odoo first loads ``url_path`` as user ``login`` (e.g. ``'admin'``, ``'demo'`` etc.) or as non-authed user
* then waits for ``ready`` condition, i.e. when some js variable (e.g. ``window``) become `truthy <https://developer.mozilla.org/en-US/docs/Glossary/Truthy>`_
* then executes js ``code``
* then wait for one of condition:

  * someone prints ``console.log('ok')`` -- test passed
  * someone prints ``console.log('error')`` -- test failed
  * ``timeout`` seconds are passed -- test failed

Example
-------

Example from `mail_sent <https://github.com/it-projects-llc/mail-addons/blob/10.0/mail_sent/tests/test_js.py/>`_:

.. code-block:: py

    # -*- coding: utf-8 -*-
    import odoo.tests
    
    
    @odoo.tests.common.at_install(False)
    @odoo.tests.common.post_install(True)
    class TestUi(odoo.tests.HttpCase):
    
        def test_01_mail_sent(self):
            # wait till page loaded and then click and wait again
            code = """
                setTimeout(function () {
                    $(".mail_sent").click();
                    setTimeout(function () {console.log('ok');}, 3000);
                }, 1000);
            """
            link = '/web#action=%s' % self.ref('mail.mail_channel_action_client_chat')
            self.phantom_js(link, code, "odoo.__DEBUG__.services['mail_sent.sent'].is_ready", login="demo")

In this test:

* odoo first loads ``/web#action=...`` page
* then waits for ``odoo.__DEBUG__.services['mail_sent.sent'].is_ready``

  * ``odoo.__DEBUG__.services['mail_sent.sent']`` is similar to ``require('mail_sent.sent')``
  * ``is_ready`` is a variable in `sent.js <https://github.com/it-projects-llc/mail-addons/blob/10.0/mail_sent/static/src/js/sent.js>`_ 

* then executes js ``code``:

  .. code-block:: js

        setTimeout(function () {
            $(".mail_sent").click();
            setTimeout(function () {console.log('ok');}, 3000);
        }, 1000);


  which clicks on ``Sent`` menu and gives to the page 3 seconds to load it.

  This code neither throws errors (e.g. via ``throw new Error('Some error description')`` nor log ``console.log('error')``, but you can add ones to your code to catch failed cases you need.

* then if everything is ok, odoo get message ``console.log('ok')``

JS tests via Tours
==================

It is possible to run js phantom tests using :doc:`odoo tours<../../description/js_tour>` as JS testing code.

How to run tour in unittests
----------------------------

* :doc:`Create tour<../../description/js_tour>` via js file
* Follow instruction for `python tests <./python.html#docker-users>`_
* run tour via phantom js

  * 10.0+:

    .. code-block:: python

        class CLASS_NAME(...):
        def test_NAME(self):

            self.phantom_js(
                URL_PATH,

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".run('TOUR_NAME')",

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".tours.TOUR_NAME.ready",

                login=LOGIN_OR_NONE
            )

  * 8.0, 9.0:

    .. code-block:: python

        class CLASS_NAME(...):
            def test_NAME(self):

                self.phantom_js(
                    URL_PATH,

                    "odoo.__DEBUG__.services['web.Tour']"
                    ".run('TOUR_NAME', 'test')",

                    "odoo.__DEBUG__.services['web.Tour']"
                    ".tours.TOUR_NAME",

                    login=LOGIN_OR_NONE
                )

How js tour works via phantomjs
-------------------------------

The order is as following:

* OPEN *url_path* from python ``phantom_js`` method
* WAIT *ready* condition (Truthy or Falsy) from python ``phantom_js`` method
* OPEN *url* from tour's options in js file 
* WAIT *wait_for* (deferred object) from tour's options in js file
* DO first step from js tour

  * WAIT when *trigger* becomes visible
  * WAIT when *extra_trigger*  becomes visible (if extra_trigger* is presented)
  * EXECUTE action (*run* or click on *trigger*)

* DO NEXT step

  * ...

* STOP Running when:

  * error happens:

    * thrown via ``raise``
    * reported via ``console.log('error', ...)``
    * reported via ``console.error(...)``, etc.
    * reported by tour system if step takes more than 10 seconds (can be increased by value of *step_delay* in ``run`` js method)

  * ``'ok'`` is reported via ``console.log('ok')``

    * directly by code 
    * indirectly by tour system when all steps are done

  * timeout from python ``phantom_js`` method is occured (default is 60 sec)
  

How to run js tests
===================

Additionally to `general requirements <./python.html#how-to-run-tests>`_, to run odoo with phantomjs tests:

* `Install phantomjs <http://phantomjs.org/download.html>`_ or use `dockers <./python.html#docker-users>`_.
* use ``--db-filter=.*``

.. TODO: Why?
.. * werkzeug must be 0.11.5 or higher

Phantom_js + python tests
=========================
If you need you run some python code before or after calling ``phantom_js`` you shall not use ``self.env`` and you need to create new env instead::

    phantom_env = api.Environment(self.registry.test_cr, self.uid, {}) 

This is because ``HttpCase`` uses special cursor and using regular cursor via ``self.env`` leads to deadlocks or different values in database.
