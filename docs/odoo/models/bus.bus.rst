=======
bus.bus
=======

Bus
===

Bus is a module for instant notifications via longpolling. Add it to dependencies list:

.. code-block:: python

    'depends': ['bus']

.. note:: Mail module in odoo 9.0 is already depended on module bus.

.. warning:: Don't mistake longpolling bus with :doc:`core.bus <../../dev/js/core.bus>` which is client-side only and part of ``web`` module.

What is longpolling
===================

* :doc:`About longpolling <../../admin/about_longpolling>`

* :doc:`How to enable Longpolling in odoo <../../admin/longpolling>`

How to implement longpolling
============================

.. contents::
   :local:

Scheme of work
--------------

* Specify channels that current client is listening
* Bind notification event to your handler
* Start polling
* Send notification to some channel via python code

Channel identifier
------------------

Channel identifier - is a way to distinguish one channel from another. In the main, channel contains dbname, some string and some id.

Added via js identifiers can be string only.

.. code-block:: js

    var channel = JSON.stringify([dbname, 'model.name', uid]);

Added via python identifiers can be a string or any data structure. 

.. code-block:: py

    # tuple
    channel = (request.db, 'model.name', request.uid)
    # or a string
    channel = '["%s","%s","%s"]' % (request.db, 'model.name', request.uid)


.. warning:: JSON.stringify in js and json.dumps in python could give a different result.

Listened channels
-----------------

You can add channels in two ways: either on the server side via ``_poll`` function in bus controller or in js file using the method ``bus.add_channel()``.

With controllers:

.. code-block:: py

    # In odoo 8.0:
    import openerp.addons.bus.bus.Controller as BusController

    # In odoo 9.0:
    import openerp.addons.bus.controllers.main.BusController

    class Controller(BusController):
        def _poll(self, dbname, channels, last, options):
            if request.session.uid:
                registry, cr, uid, context = request.registry, request.cr, request.session.uid, request.context
                new_channel = (request.db, 'module.name', request.uid)
                channels.append(new_channel)
            return super(Controller, self)._poll(dbname, channels, last, options)

In the js file:

.. code-block:: js

    // 8.0
    var bus = openerp.bus.bus;
    // 9.0+
    var bus = require('bus.bus').bus;

    var channel = JSON.stringify([dbname, 'model.name', uid]);
    bus.add_channel(new_channel);

Binding notification event
--------------------------

In js file:

.. code-block:: js

    bus.on("notification", this, this.on_notification);

Start polling
-------------

In js file:

.. code-block:: js

    bus.start_polling();

.. note:: You don't need to call ``bus.start_polling();`` if it was already started by other module.

When polling starts, request ``/longpolling/poll`` is sent, so you can find and check it via Network tool in your browser

Sending notification
--------------------

You can send notification only through a python. If you need to do it through the client send a signal to server in a usual way first (e.g. via `controllers <http://odoo-development.readthedocs.io/en/latest/dev/py/controllers.html>`_).

.. code-block:: py

    self.env['bus.bus'].sendmany([(channel1, message1), (channel2, message2), ...])
    # or
    self.env['bus.bus'].sendone(channel, message)

Handling notifications
----------------------

.. code-block:: js

    on_notification: function (notifications) {
        // Old versions passes single notification item here. Convert it to the latest format.
        if (typeof notification[0][0] === 'string') {
            notification = [notification]
        }
        for (var i = 0; i < notification.length; i++) {
            var channel = notification[i][0];
            var message = notification[i][1];

            // proceed a message as you need
            // ...
        }
    },

Examples
========
**pos_multi_session:**

* `add channel (python) <https://github.com/it-projects-llc/pos-addons/blob/9.0/pos_multi_session/controllers/pos_multi_session.py#L18>`__

* `bind event <https://github.com/it-projects-llc/pos-addons/blob/9.0/pos_multi_session/static/src/js/pos_multi_session.js#L411>`__

* `send notification <https://github.com/it-projects-llc/pos-addons/blob/9.0/pos_multi_session/pos_multi_session_models.py#L25>`__

**chess:**

* `add channel (js) <https://github.com/GabbasovDinar/addons-dev/blob/website-addons-8.0-chess/chess/static/js/chesschat.js#L11-L14>`__

* `bind event <https://github.com/GabbasovDinar/addons-dev/blob/website-addons-8.0-chess/chess/models/chess.py#L282-L288>`__

* `send notification <https://github.com/GabbasovDinar/addons-dev/blob/website-addons-8.0-chess/chess/static/js/chesschat.js#L134-L145>`__

**mail_move_message:**

* `add channel (python) <https://github.com/x620/mail-addons/blob/9.0-mail_move_message/mail_move_message/controllers/main.py#L15>`__

* `bind event <https://github.com/x620/mail-addons/blob/9.0-mail_move_message/mail_base/static/src/js/base.js#L1150-L1152>`__

* `send notification <https://github.com/x620/mail-addons/blob/9.0-mail_move_message/mail_move_message/mail_move_message_models.py#L312>`__
