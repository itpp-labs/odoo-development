=========
 JS Tour
=========


Tour is a set of steps of possible scenario of module usage. 

Steps may be executed automatically for :doc:`testing <../qa/js/index>` purpose or by user for :ref:`demostrating <auto_launch_after_installation>` purpose.

.. contents::
   :local:

Tour Definition
===============

10.0+
-----
Example
~~~~~~~
Example from `website_sale <https://github.com/odoo/odoo/blob/10.0/addons/website_sale/static/src/js/website_sale_tour_buy.js>`_ module:

.. code-block:: js

    odoo.define('website_sale.tour', function (require) {
    'use strict';
    
    var tour = require("web_tour.tour");
    var base = require("web_editor.base");
    
    var options = {
        test: true,
        url: '/shop',
        wait_for: base.ready()
    };

    var tour_name = 'shop_buy_product';
    tour.register(tour_name, options,
        [
            {
                content: "search ipod",
                trigger: 'form input[name="search"]',
                run: "text ipod",
            },
            {
                content: "search ipod",
                trigger: 'form:has(input[name="search"]) .oe_search_button',
            },
            {
                content: "select ipod",
                trigger: '.oe_product_cart a:contains("iPod")',
            },
            {
                content: "select ipod 32GB",
                extra_trigger: '#product_detail',
                trigger: 'label:contains(32 GB) input',
            },
            {
                content: "click on add to cart",
                extra_trigger: 'label:contains(32 GB) input:propChecked',
                trigger: '#product_detail form[action^="/shop/cart/update"] .btn',
            },
            /* ... */
        ]
    );
    
    });


Options
~~~~~~~

Options (second argument of ``tour.register``):

* **test** -- only for tests
* **url** -- open link before running the tour
* **wait_for** -- wait for deffered object before running the script
* **skip_enabled** -- adds *Skip* button in tips

Step
~~~~

Each step may have following attrubutes:

* **content** -- name or title of the step
* **trigger** (mandatory) -- where to place tip. *In js tests: where to click*
* **extra_trigger** -- when this becomes visible, the tip is appeared. *In js tests: when to click*
* **timeout** -- max time to wait for conditions
* **position** -- how to show tip (left, rigth, top, bottom), default right
* **width** -- width in px of the tip when opened, default 270
* **edition** -- specify to execute in *"community"* or in *"enterprise"* only. By default empty -- execute at any edition.
* **run** -- what to do when tour runs automatically (e.g. in tests)

  * ``'text SOMETEXT'`` -- writes value in **trigger** element
  * ``'click'``
  * ``'drag_and_drop TO_SELECTOR'``
  * ``'auto'`` -- auto action (click or text)
  * ``function: (actions) { ... }`` -- actions is instance of RunningTourActionHelper -- see `tour_manager.js <https://github.com/odoo/odoo/blob/10.0/addons/web_tour/static/src/js/tour_manager.js>`_ for its methods.
* **auto** -- step is skipped in non-auto running

Predefined steps
~~~~~~~~~~~~~~~~

* ``tour.STEPS.MENU_MORE`` -- clicks on menu *More* in backend when visible
* ``tour.STEPS.TOGGLE_APPSWITCHER`` -- nagivate to Apps page when running in enterprise
* ``tour.STEPS.WEBSITE_NEW_PAGE`` -- clicks create new page button in frontend

More documentation
~~~~~~~~~~~~~~~~~~

* https://www.odoo.com/slides/slide/the-new-way-to-develop-automated-tests-beautiful-tours-440
* https://github.com/odoo/odoo/blob/10.0/addons/web_tour/static/src/js/tour_manager.js
* https://github.com/odoo/odoo/blob/10.0/addons/web_tour/static/src/js/tip.js


8.0, 9.0
--------

Example
~~~~~~~

.. code-block:: js

        {
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
        }

Tour.register
~~~~~~~~~~~~~

In odoo 8 tour defines this way::

    (function () {
    'use strict';
    var _t = openerp._t;
    openerp.Tour.register({ ...

In odoo 9 tour defines that way::

    odoo.define('account.tour_bank_statement_reconciliation', function(require) {
    'use strict';
    var core = require('web.core');
    var Tour = require('web.Tour');
    var _t = core._t;
    Tour.register({ ...

Important details:

    * **id** - need to call this tour
    * **path** - from this path tour will be started in test mode

Step
~~~~

Next step occurs when **all** conditions are satisfied and popup window will appear near (chose position in *placement*) element specified in *element*. Element must contain css selector of corresponding node.
Conditions may be:

    * **waitFor** - this step will not start if *waitFor* node absent.
    * **waitNot** - this step will not start if *waitNot* node exists.
    * **wait** - just wait some amount of milliseconds before **next** step.
    * **element** - similar to *waitFor*,  but *element* must be visible
    * **closed window** - if popup window have close button it must be closed before next step.

Opened popup window (from previous step) will close automatically and new window (next step) will be shown.

Inject JS Tour file on page::

    <template id="res_partner_mails_count_assets_backend" name="res_partner_mails_count_assets_backend" inherit_id="web.assets_backend">
        <xpath expr="." position="inside">
            <script src="/res_partner_mails_count/static/src/js/res_partner_mails_count_tour.js" type="text/javascript"></script>
        </xpath>
    </template>

More documentation
~~~~~~~~~~~~~~~~~~

Some docs is here (begin from 10 slide):
http://www.slideshare.net/openobject/how-to-develop-automated-tests
Also checkout here:
https://github.com/odoo/odoo/blob/9.0/addons/web/static/src/js/tour.js

Open backend menu
=================

9.0+
----

Some additional actions are required to work with backend menus in tours

Manifest
~~~~~~~~

Add ``web_tour`` to dependencies

.. code-block:: py

    "depends": [
        "web_tour",
    ],
    # ...
    "demo": [
        "views/assets_demo.xml",
        "views/tour_views.xml",
    ],


load_xmlid
~~~~~~~~~~

You need to set ``load_xmlid`` for *each* menu you need to open. Recommended
name for the file is ``tour_views.xml``

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <odoo>
        <!-- Make the xmlid of menus required by the tour available in webclient -->
        <record id="base.menu_administration" model="ir.ui.menu">
            <field name="load_xmlid" eval="True"/>
        </record>
    </odoo>

Tour
~~~~

Use *trigger* selector for both editions:

.. code-block:: js


    {
        trigger: '.o_app[data-menu-xmlid="base.menu_administration"], .oe_menu_toggler[data-menu-xmlid="base.menu_administration"]',
        content: _t("Configuration options are available in the Settings app."),
        position: "bottom"
    }


8.0
---

The only way to open menu is search by string, for example

.. code-block:: js

    {
        title:     "go to accounting",
        element:   '.oe_menu_toggler:contains("Accounting"):visible',
    },




Manual launching
================

10.0+
-----

* :doc:`activate developer mode <../odoo/usage/debug-mode>`.
* Click *Bug* icon (between chat *icon* and *Username* at top right-hand corner)

  * click ``Start tour``

* Click *Play* button -- it starts tour in auto mode

To run *test-only* tours (or to run tours in auto mode but with some delay) do as following:

* open browser console (F12 in Chrome)
* Type in console:

  .. code-block:: js

    odoo.__DEBUG__.services['web_tour.tour'].run('TOUR_NAME', 1000); // 1000 is delay in ms before auto action

8.0, 9.0
--------

You can launch tour by url of following format: 

``/web#/tutorial.mails_count_tour=true``

where *mails_count_tour*  is id of your tour.

.. _auto_launch_after_installation:

Auto Launch after installation
==============================

10.0+
-----

TODO

8.0, 9.0
--------

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

