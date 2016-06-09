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

`Longpolling configuration <https://odoo-development.readthedocs.io/en/latest/admin/longpolling.html>`_

`About longpolling <https://odoo-development.readthedocs.io/en/latest/admin/about_longpolling.html>`_

How it works
============

    **Operating principle**

    **What is a subscription (channel)**

    **What can be a channel identifier**

    **How to subscribe to a channel**

    **How to send a message to the channel**

    **Who will get this message**

=====================================================================================================

**Use in own modules**

General settings:

In odoo longpolling appears in module ``bus``.  You should write the following for use it in your own modules:

.. code-block:: shell

    'depends': ['bus']

**Backend**


``Bus`` can be  connected in the client’s part (js) as follows:

.. code-block:: js

    varMyModule = openerp.MyModule = {};
    MyModule.ConversationManager = openerp.Widget.extend({
        init: function () {
            this.bus = openerp.bus.bus;
            this.bus.on("notification", this, this.on_notification);
            this.bus.start_polling();
        },

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

If everything is good, write to ``this.received_message();`` the following:

.. code-block:: js

    on_notification_do: function (channel, message) {
        // your process
    }

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

For the work in the server write the following:

.. code-block:: py

    class Controller(openerp.addons.bus.bus.Controller):
        def _poll(self, dbname, channels, last, options):
            if request.session.uid:
                registry, cr, uid, context = request.registry, request.cr, request.session.uid, request.context
                channels.append((request.db, 'module.name', request.uid))
            return super(Controller, self)._poll(dbname, channels, last, options)

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

After sending message , function ``this.on_notification`` accepts the message. 

