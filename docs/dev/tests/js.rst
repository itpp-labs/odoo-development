JS Testing
==========

Regular phantom JS tests
------------------------

For automatic web tests odoo uses phantom_js.
You can test you module web mechanics behavior using phantom js.

What you need is:

    * Install phantom. *sudo apt-get install phantomjs*
    * Create folder named **tests**
    * Add __init__.py file
    * Create file that name begins from **test_**
    * Add test methods than names start from **test_**

Example::

    import openerp.tests

    @openerp.tests.common.at_install(False)
    @openerp.tests.common.post_install(True)
    class TestUi(openerp.tests.HttpCase):
        def test_01_mail_sent(self):
            # wait till page loaded and then click and wait again
            code = """
                setTimeout(function () {
                $(".mail_sent").click();
                if (location.href.indexOf('channel_sent')!=-1) {
                    throw new Error('Already on channel_sent.');
                }
                setTimeout(function () {
                     if (location.href.indexOf('channel_sent')==-1) {
                         throw new Error('End page is not channel_sent.');
                     }
                    console.log('ok');
                }, 3000);
            }, 1000);
            """
            link = '/web#action=%s' % self.ref('mail.mail_channel_action_client_chat')
            self.phantom_js(link, code, "odoo.__DEBUG__.services['mail_sent.sent']", login="demo")

You need to call phantom_js and give to it arguments:

    * Starting url
    * JS code intended for execution
    * Ready criteria. Some JS object that indicates preparedness of web page. In 9.0 it may be odoo.define('**mail_archives.archives**' ...
    * User name

Use throw new Error('Error text'); for errors handling.

JS phantom tests using Tours
----------------------------

It is possible to run js phantom tests using Tour as JS testing code.
To run test automatically after installing module you will need:

    * Install phantomjs if dont have yet
    * Inject *JS Tour* file on web page
    * Create test as described higher
    * Call tour

Call tour example::

    class TestUi(openerp.tests.HttpCase):
        def test_01_res_partner_mails_to_count(self):
            self.phantom_js('/',  "openerp.Tour.run('mails_count_tour', 'test')", "openerp.Tour.tours.mails_count_tour", login="admin")

Also odoo must be started with **-d** , **--test-enable** and without **db-filter** , **workers**.
If assumes ti run test only on install or update use **-i** or **-u**.
Werkzeug must be 0.11.5 or higher.

Look up js tour page for details.
