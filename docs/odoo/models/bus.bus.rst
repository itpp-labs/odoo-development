=======
bus.bus
=======

Bus
===

Module for instant notifications via longpolling. Add it to dependencies list:

.. code-block:: shell

    'depends': ['bus']

Mail module in odoo 9.0 is already depended on module bus.

What is longpolling
===================

`About longpolling <https://odoo-development.readthedocs.io/en/latest/admin/about_longpolling.html>`_

`Longpolling configuration <https://odoo-development.readthedocs.io/en/latest/admin/longpolling.html>`_

How it works
============

**Operating principle**

First, you create a subscription and specify the subscription ID. Then you need to connect "notification" object in the js file. It is waiting for a notification from the server with the specified subscription identifier. On the server side at some point generates and sends a notification with a specific ID. If these identifiers match, then the js object responds to it. It receives notification data and performs certain actions.

**What is a subscription**

Subscription - is a channel, which stores (passes through himself) notifications from server to client. The client can subscribe to this feed and receive notifications that are sent from the server.

**What can be a channel identifiers**

Identifier - is a way to distinguish one channel from another. Identifiers can be a string, tuple, list. But the most commonly used triple:

.. code-block:: py

    channels.append((request.db, 'module.name', request.uid))

If the subscription is done via js, then the identifier can only be a string. And, respectively in python you have to send string too.

.. code-block:: js

    var channel = JSON.stringify([dbname, 'model.name', uid]);
    bus.add_channel(channel);

**How to subscribe to a channel**

You can create a subscription in two ways: on the server side via the controllers or in js file using the method ``bus.add_channel()``.

With controllers:

.. code-block:: py

    # If odoo 8.0:
    import openerp.addons.bus.bus.Controller as BusController
    # If odoo 9.0:
    import openerp.addons.bus.controllers.main.BusController

    class Controller(BusController):
        def _poll(self, dbname, channels, last, options):
            if request.session.uid:
                registry, cr, uid, context = request.registry, request.cr, request.session.uid, request.context
                new_channel = (request.db, 'module.name', request.uid)
                channels.append(new_channel)
            return super(Controller, self)._poll(dbname, channels, last, options)

In the js file:


*For odoo 8.0*

TODO

*For odoo 9.0*

.. code-block:: js

    var bus = require('bus.bus').bus;
    ...
    bus.add_channel(new_channel);
    // If not called earlier in the stack only
    bus.start_polling();


To start receiving notifications do as follows:

*For odoo 8.0*

.. code-block:: js

    this.bus = openerp.bus.bus;
    this.bus.on("notification", this, this.on_notification);
    this.bus.start_polling();

*For odoo 9.0*

.. code-block:: js

    var bus = require('bus.bus').bus;
    ...
    bus.on("notification", this, this.on_notification);
    bus.start_polling();

``bus.start_polling();`` can not write if it was already called earlier in the stack.

Request /longpolling/poll it is expectation messages that will be sent to any of the channels that has a subscription.

**How to send a message to the channel**

Send messages only through a python. If you want to through the client send something (e.g. via `controllers <http://odoo-development.readthedocs.io/en/latest/dev/py/controllers.html>`_), and then through the server to send the following:

.. code-block:: py

    self.env['bus.bus'].sendmany(notifications)
    # or
    self.env['bus.bus'].sendone(new_channel, notification)

The below function will intercept form the client the request ``/send/`` and will process this request:

.. code-block:: py

    @http.route('/send/', type="json", auth="public")
    def message_send(self, message):
        /* message processing */
        request.env["model.name"].broadcast(message)
        return True

``broadcast`` function creates the notice and sends the its result (in this case, to all users except for current)

.. code-block:: py

    @api.model
    def broadcast(self, message):
        notifications = []
        for ps in self.env['res.users'].search([('id', '!=', self.env.user.id)]):
            notifications.append([(self._cr.dbname, 'model.name', ps.id), message])
            self.env['bus.bus'].sendmany(notifications)
        return 1

**Who will get this message**

After sending message, function ``this.on_notification`` accepts the message.

``this.on_notification`` – is response for accepting of server messages
Notification, which was sent from the server, includes channel and message.
Put to the corresponding variable values from ``notification``. Notification handler receives the message. You can do whatever you you need with received message.

.. code-block:: js

    on_notification: function (notifications) {
        var self = this;
        // Old versions passes single notification item here. Fix it.
        if (typeof notification[0][0] === 'string') {
            notification = [notification]
        }
        for (var i = 0; i < notification.length; i++) {
            var channel = notification[i][0];
            var message = notification[i][1];
            this.on_notification_do(channel, message);
        }
    },

Examples
========
**pos_multi_session:**

* `add channel (python) <https://github.com/it-projects-llc/pos-addons/blob/9.0/pos_multi_session/controllers/pos_multi_session.py#L18>`_

* `subscribe <https://github.com/it-projects-llc/pos-addons/blob/9.0/pos_multi_session/static/src/js/pos_multi_session.js#L411>`_

* `send <https://github.com/it-projects-llc/pos-addons/blob/9.0/pos_multi_session/pos_multi_session_models.py#L25>`_

**chess:**

* `add channel (js) <https://github.com/GabbasovDinar/addons-dev/blob/website-addons-8.0-chess/chess/static/js/chesschat.js#L11-L14>`_

* `subscribe <https://github.com/GabbasovDinar/addons-dev/blob/website-addons-8.0-chess/chess/models/chess.py#L282-L288>`_

* `send <https://github.com/GabbasovDinar/addons-dev/blob/website-addons-8.0-chess/chess/static/js/chesschat.js#L134-L145>`_

**mail_move_message:**

* `add channel (python) <https://github.com/x620/mail-addons/blob/9.0-mail_move_message/mail_move_message/controllers/main.py#L15>`_

* `subscribe <https://github.com/x620/mail-addons/blob/9.0-mail_move_message/mail_base/static/src/js/base.js#L1150-L1152>`_

* `send <https://github.com/x620/mail-addons/blob/9.0-mail_move_message/mail_move_message/mail_move_message_models.py#L312>`_
