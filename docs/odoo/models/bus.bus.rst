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

Subscription - is a channel, which stores (passes through himself) notifications from server to client. The client can subscribe to this feed and receive notifications that are sent from the server. You can create a subscription in two ways: on the server side via the controllers or in js file using the method ``bus.add channel()``.


With controllers:

*For odoo 8.0*

.. code-block:: py

    class Controller(openerp.addons.bus.bus.Controller):
        def _poll(self, dbname, channels, last, options):
            if request.session.uid:
                registry, cr, uid, context = request.registry, request.cr, request.session.uid, request.context
                channels.append((request.db, 'module.name', request.uid))
            return super(Controller, self)._poll(dbname, channels, last, options)


*For odoo 9.0*

.. code-block:: py

    class Controller(openerp.addons.bus.controllers.main.BusController):
        def _poll(self, dbname, channels, last, options):
            if request.session.uid:
                registry, cr, uid, context = request.registry, request.cr, request.session.uid, request.context
                channels.append((request.db, 'module.name', request.uid))
            return super(Controller, self)._poll(dbname, channels, last, options)

In the js file:

.. code-block:: js

    var bus = require('bus.bus').bus;
    ...
    bus.add_channel(channel.uuid);
    bus.start_polling();

**What can be a channel identifier**

Identifier - is a way to distinguish one channel from another. Identifiers can be a string, tuple, list. But the most commonly used triple:

.. code-block:: py

    channels.append((request.db, 'module.name', request.uid))

**How to subscribe to a channel**

To subscribe to the channel, the client must be connected as follows:

*For odoo 8.0*

.. code-block:: js

    var MyModule = openerp.MyModule = {};
    MyModule.ConversationManager = openerp.Widget.extend({
        init: function () {
            this.bus = openerp.bus.bus;
            this.bus.on("notification", this, this.on_notification);
            this.bus.start_polling();
        },

*For odoo 9.0*

.. code-block:: js

    var bus = require('bus.bus').bus;
    ...
    var MyModule.ConversationManager = Widget.extend({
        init: function () {
            bus.on("notification", this, this.on_notification);
            bus.start_polling();
        },


**How to send a message to the channel**

You can send message to the server in separate widget.
Create new widget and find ``session`` for requests (sending of message and the work of ``bus``). Create the object of widget, where ``bus`` connection and message processing are made.
Write the following for the message sending:

.. code-block:: js

    MyModule.Conversation = openerp.Widget.extend({
        init: function(){
            this.openerp.session = new openerp.Session();
            this.c_manager = new openerp.ChessChat.ConversationManager(null, channel);
            this.send_message();
        },

``send_message()`` function sends messaged though the request ``JSON``.

.. code-block:: js

    send_message: function() {
        var message = ‘’;
        // Creating messages
        this.openerp.session ("/send/", {message: message})
    }

Create an object for widget work:

.. code-block:: js

    var my_module = new MyModule.Conversation(this);

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

After sending message , function ``this.on_notification`` accepts the message.

``this.on_notification`` – is response for accepting of server messages
Notification, which was sent from the server, includes channel and message.
Put to the corresponding variable values from ``notification``

.. code-block:: js

    on_notification: function (notification) {
        var self = this;
        if (typeof notification[0][0] === 'string') {
            notification = [notification]
        }
        for (var i = 0; i < notification.length; i++) {
            var channel = notification[i][0];
            var message = notification[i][1];
            this.on_notification_do(channel, message);
        }
    },

You should check if there are coincidences with the name of the model, from which the server's response comes.

If everything is good, write your process in the on_notification_do():

.. code-block:: js

    on_notification_do: function (channel, message) {
        // your process
    }
