===================
 self.phantom_js()
===================


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
=======

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
