bus.bus
=======


`About longpolling <https://odoo-development.readthedocs.io/en/latest/admin/longpolling.html>`_

**Use in own modules**


General settings:

In odoolongpolling appears in module ``bus``.  You should write the following for use it in your own modules:

.. code-block:: shell

    'depends': ['bus']

**Back-end**


``Bus`` can be  connected in the client’s part (js) as follows:

.. code-block:: shell

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

.. code-block:: shell

    on_notification: function (notification) {
        var self = this;
        if (typeof notification[0][0] === 'string') {
            notification = [notification]
        }
        for (vari = 0; i<notification.length; i++) {
            var channel = notification[i][0];
            var message = notification[i][1];
            this.on_notification_do(channel, message);
        }
    },

You should check if there are coincidences with the name of the model, from which the server's response comes

If everything is good, write to ``this.received_message();`` the following:

.. code-block:: shell

    on_notification_do: function (channel, message) {
        // your process
    }

You can send message to the server in separate widget. 
Create new widget and find ``session`` for requests (sending of message and the work of ``bus``). Create the object of widget, where ``bus`` connection and message processing are made. 
Write the following for the message sending:

.. code-block:: shell

    MyModule.Conversation = openerp.Widget.extend({
        init: function(){
        this.openerp.session = new openerp.Session();
        this.c_manager = new openerp.ChessChat.ConversationManager(null, channel);
	this.send_message();
    },

``send_message()`` function sends messaged though the request ``JSON``.

.. code-block:: shell

    send_message: function() {
	var message = ‘’;
	// Creating messages
        this.openerp.session ("/send/", {message: message})
    }

Create an object for widget work:

.. code-block:: shell

    var my_module = new MyModule.Conversation(this)

For the work in the server write the following:

.. code-block:: shell

    class Controller(openerp.addons.bus.bus.Controller):
	def _poll(self, dbname, channels, last, options):
	if request.session.uid:
		registry, cr, uid, context = request.registry, request.cr, request.session.uid, request.context
		channels.append((request.db, 'module.name', request.uid))
	return super(Controller, self)._poll(dbname, channels, last, options)

The below function will intercept form the clien the request ``/send/`` and will process this request:

.. code-block:: shell

    @http.route('/send/', type="json", auth="public")
	de fmessage_send(self, message):
	/* message processing */
	request.env["model.name"].broadcast(message)
	return True

``broadcast`` function creates the notice and sends the its result (in this case, to all users except for current)

.. code-block:: shell

    @api.model
    def broadcast(self, message):
	notifications = []
	forps in self.env['res.users'].search([('id', '!=', self.env.user.id)]):
	notifications.append([(self._cr.dbname, 'model.name', ps.id), message])
	self.env['bus.bus'].sendmany(notifications)
        return 1

After sending message , function ``this.on_notification`` accepts the message. 

