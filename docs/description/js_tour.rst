JS Tour
=======

Used to demonstrate module capabilities step by step with popup windows. It may be launched automatically or manually.

Creating Tour
-------------

Tour is a simple JS file with some determined structure.
Example::

        id: 'mails_count_tour',
        name: _t("Mails count Tour"),
        mode: 'test',
        path: '/web#id=3&model=res.partner',
        steps: [
            {
                title:     _t("Mails count tutorial"),
                content:   _t("Let's see how mails count work."),
                popover:   { next: _t("Start Tutorial"), end: _t("Skip") },
            },
            {
                title:     _t("New fields"),
                content:   _t("Here is new fields with mails counters. Press one of it."),
                element:   '.mails_to',
            },
            {
                waitNot:   '.mails_to:visible',
                title:     _t("Send message from here"),
                placement: 'left',
                content:   _t("Now you can see corresponding mails. You can send mail to this partner right from here. Press <em>'Send a mesage'</em>."),
                element:   '.oe_mail_wall .oe_msg.oe_msg_composer_compact>div>.oe_compose_post',
            },
        ]

What you do here is describing steps that got to be proceeded by user or phantom (phantomjs).

Important details:

    * **id** - need to call this tour
    * **path** - from this path tour will be started. Used in test mode only!

Next step occurs when **all** conditions are satisfied and popup window will appear near (chose position in *placement*) element specified in *element*. Element must contain css selector of corresponding node.
Conditions may be:

    * **waitFor** - this step will not start if *waitFor* node absent.
    * **waitNot** - this step will not start if *waitNot* node exists.
    * **wait** - just wait some amount of milliseconds before **next** step.
    * **element** - wait for element.
    * **closed window** - if popup window have close button it must be closed before next step.

Opened popup window (from previous step) will close automatically and new window (next step) will be shown.

Inject JS Tour file on page::

    <template id="res_partner_mails_count_assets_backend" name="res_partner_mails_count_assets_backend" inherit_id="web.assets_backend">
        <xpath expr="." position="inside">
            <script src="/res_partner_mails_count/static/src/js/res_partner_mails_count_tour.js" type="text/javascript"></script>
        </xpath>
    </template>

Some docs is here (begin from 10 slide):
http://www.slideshare.net/openobject/how-to-develop-automated-tests
Also checkout here:
https://github.com/odoo/odoo/blob/9.0/addons/web/static/src/js/tour.js

You can launch tour by entering in browser address like this mydatabase/web#/tutorial.mails_count_tour=true where after tutorial. is id of your tour.

Automatic tour launch
---------------------
To run tour after module installation do next steps.

    * Create *ToDo*
    * Create *Action*


ToDo is some queued web actions that may call *Action* like this::

    <record id="base.open_menu" model="ir.actions.todo">
        <field name="action_id" ref="action_website_tutorial"/>
        <field name="state">open</field>
    </record>

Action is like this::

    <record id="res_partner_mails_count_tutorial" model="ir.actions.act_url">
        <field name="name">res_partner_mails_count Tutorial</field>
        <field name="url">/web#id=3&amp;model=res.partner&amp;/#tutorial_extra.mails_count_tour=true</field>
        <field name="target">self</field>
    </record>

Here tutorial_extra.**mails_count_tour** is tour id.

Use eval to compute some python code if needed::

    <field name="url" eval="'/web?debug=1&amp;res_partner_mails_count=tutorial#id='+str(ref('base.partner_root'))+'&amp;view_type=form&amp;model=res.partner&amp;/#tutorial_extra.mails_count_tour=true'"/>

