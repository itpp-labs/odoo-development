=================
 POS Longpolling
=================

It is a custom odoo module made by `IT-Projects LLC, <https://it-projects.info>`__ which provides instant updates to the POS interfaces from backend.

Let take the **example** of the ``Sync Partners in POS`` module.

* On each record update (needed to be sent) in ``res.partner`` model in ``send_field_updates``  `method. <https://github.com/it-projects-llc/pos-addons/blob/907b16cc3a4ea613bf4fc81891a03739405e57a7/pos_partner_sync/models/res_partner.py#L39-L43::>`__
* It uses ``send_to_all_poses`` `method <https://github.com/it-projects-llc/pos-addons/blob/907b16cc3a4ea613bf4fc81891a03739405e57a7/pos_partner_sync/models/res_partner.py#L43>`__.

* It's defined in ``POS Longpolling`` module in the ``pos.config`` `model. <https://github.com/it-projects-llc/pos-addons/blob/28d2b00bfd3f5d09bb65d5bf3245a6b87ed1d67b/pos_longpolling/models/pos_longpolling_models.py#L49-L53>`__

* It sends some data for all opened POSes using a special channel for each kind of updates (usually one per module) to be handled separetaly.

To make those requests be handled by POS we need to create such environment in POS.

First, define the channel and `link <https://github.com/it-projects-llc/pos-addons/blob/e471b4af2f062852d256d46c200e582b0f20d0ad/pos_partner_sync/static/src/js/pos_partner_sync.js#L13-L19::>`__ a handler to it:

.. code-block:: js

    initialize: function () {
	    PosModelSuper.prototype.initialize.apply(this, arguments);
	    var self = this;
	    this.ready.then(function () {
		    self.bus.add_channel_callback("pos_partner_sync", self.on_barcode_updates, self);
	    });
    },

There after the ``PosModel`` is loaded we add a new `channel <https://github.com/it-projects-llc/pos-addons/blob/e471b4af2f062852d256d46c200e582b0f20d0ad/pos_partner_sync/static/src/js/pos_partner_sync.js#L20-L38>`__ ``pos_partner_sync`` with related handler function ``on_barcode_updates``:

.. code-block:: js

        on_barcode_updates: function(data){
            var self = this;
            if (data.message === 'update_partner_fields') {
                var def = new $.Deferred();
                if (data.action && data.action === 'unlink') {
                    this.remove_unlinked_partners(data.partner_ids);
                    def.resolve();
                } else {
                    def = self.load_new_partners(data.partner_ids);                }                return def.done(function(){
                    var opened_client_list_screen = self.gui.get_current_screen() === 'clientlist' && self.gui.screen_instances.clientlist;
                    if (opened_client_list_screen){
                       opened_client_list_screen.update_client_list_screen(data.partner_ids);
                    }
                });
            }
        },

It checks for the specific ``data.message`` to provide required handler where **data** is an object came from ``send_to_all_poses`` method, and **data.message** is some string set in ``send_field_updates`` method.

Also it's possible to send updates only for specied POS by its **config.id** using the ``_send_to_channel_by_id`` `method:
<https://github.com/it-projects-llc/pos-addons/blob/28d2b00bfd3f5d09bb65d5bf3245a6b87ed1d67b/pos_longpolling/models/pos_longpolling_models.py#L33-L38::>`__

.. code-block:: python

    @api.model
    def _send_to_channel_by_id(self, dbname, pos_id, channel_name, message = 'PONG'):
	    channel = self._get_full_channel_name_by_id(dbname, pos_id, channel_name)
    self.env['bus.bus'].sendmany([[channel, message]])
    _logger.debug('POS notifications for %s: %s', pos_id, [[channel, message]])
    return 1

But it requires a **dbname** to be able to provide updates for POSes use different, separated data bases.

It can be demonstrated with ``Sync Server for POS orders`` `module.
<https://github.com/it-projects-llc/pos-addons/blob/4b9385b71f13f5df993317196d23972b65a7c2f8/pos_multi_session_sync/models/pos_multi_session_sync_models.py#L257-L276>`__

.. code-block:: python

    @api.multi
        def broadcast_message(self, message):
	        self.ensure_one()
                notifications = []
                channel_name = "pos.multi_session"
                for pos in self.env['pos_multi_session_sync.pos'].search([('multi_session_ID', '=', self.multi_session_ID)]):
	                    message_ID = pos.multi_session_message_ID + 1
                    pos.write({
                    'multi_session_message_ID': message_ID
                    })
                    message['data']['message_ID'] = message_ID
                        self.env['pos.config']._send_to_channel_by_id(self.dbname, pos.pos_ID, channel_name, message)
                if self.env.context.get('phantomtest') == 'slowConnection':
	                _logger.info('Delayed notifications from %s: %s', self.env.user.id, notifications)
                    # commit to update values on DB
                    self.env.cr.commit()
                    time.sleep(3)
                    return 1
