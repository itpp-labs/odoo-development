=================
 POS Longpolling
=================

It is a custom odoo `module <https://github.com/it-projects-llc/pos-addons/tree/12.0/pos_longpolling>`__ made by `IT-Projects LLC, <https://it-projects.info>`__ which allows sending instant updates to the POS interfaces from backend.

It provides following methods in *Backend side*:

* ``self.env['pos.config].send_to_all_poses(channel_name, data)``:broadcasts messages to all opened POSes  (see `example <https://github.com/it-projects-llc/pos-addons/blob/28d2b00bfd3f5d09bb65d5bf3245a6b87ed1d67b/pos_longpolling/models/pos_longpolling_models.py#L49-L53>`__)

* ``pos_set._send_to_channel(channel_name, data)``:broadcasts message to the POSes in ``pos_set`` (see `example <https://github.com/it-projects-llc/pos-addons/blob/28d2b00bfd3f5d09bb65d5bf3245a6b87ed1d67b/pos_longpolling/models/pos_longpolling_models.py#L22-L31>`__)

* ``_send_to_channel_by_id(self, dbname, pos_id, channel_name)``:sends message to exact POS ``pos_id``, uses data base name ``dbname`` , ``channel_name``, ``message='PONG'`` (see `example <https://github.com/it-projects-llc/pos-addons/blob/28d2b00bfd3f5d09bb65d5bf3245a6b87ed1d67b/pos_longpolling/models/pos_longpolling_models.py#L34-L38>`__)

.. note::

    POS will get notification only if it's subscribed to the specified ``channel_name``.

For *Client side* the methods are:

* **add_bus(key, sync_server)**: allows to create additional Bus to sync data with another Sync Server (see `example <https://github.com/it-projects-llc/pos-addons/blob/4b9385b71f13f5df993317196d23972b65a7c2f8/pos_multi_session/static/src/js/pos_multi_session.js#L146>`__ in **pos_multi_session** - it gets data from local server to speed up synchronization).

.. note::

    You don't need to use ``add_bus`` if you connect with your regular odoo server.

* ``add_channel_callback: function(channel_name, callback, thisArg)``:subscribes to specific channel (see `example <https://github.com/it-projects-llc/pos-addons/blob/28d2b00bfd3f5d09bb65d5bf3245a6b87ed1d67b/pos_longpolling/static/src/js/pos_longpolling.js#L97>`__)

Let's check  example of usage taking as a basis ``Sync Partners in POS`` module:

Sync Partners in POS module
============================

This `module <https://github.com/it-projects-llc/pos-addons/blob/907b16cc3a4ea613bf4fc81891a03739405e57a7/pos_partner_sync/>`__ on each partner update (in Backend) notifies POSes to update partner data.

Here you can see how it uses ``pos_longpolling``:

BACKEND
-------

* On partner update ``send_field_updates``  `method. <https://github.com/it-projects-llc/pos-addons/blob/907b16cc3a4ea613bf4fc81891a03739405e57a7/pos_partner_sync/models/res_partner.py#L39-L43::>`__ is called:

.. code-block:: python

    @api.model
    def send_field_updates(self, partner_ids, action=''):
        channel_name = "pos_partner_sync"
        data = {'message': 'update_partner_fields', 'action': action, 'partner_ids': partner_ids}
        self.env['pos.config'].send_to_all_poses(channel_name, data)

* It uses ``send_to_all_poses`` method.

CLIENT
------

* On POS starting it's subscribed to `channel <https://github.com/it-projects-llc/pos-addons/blob/e471b4af2f062852d256d46c200e582b0f20d0ad/pos_partner_sync/static/src/js/pos_partner_sync.js#L13-L19::>`__ ``pos_partner_sync``.

.. code-block:: js

    initialize: function () {
      PosModelSuper.prototype.initialize.apply(this, arguments);
      var self = this;
      this.ready.then(function () {
        self.bus.add_channel_callback("pos_partner_sync", self.on_barcode_updates, self);
        });
    },

* On notification `on_barcode_updates <https://github.com/it-projects-llc/pos-addons/blob/e471b4af2f062852d256d46c200e582b0f20d0ad/pos_partner_sync/static/src/js/pos_partner_sync.js#L20-L38>`__ is called, which reloads partner data:

.. code-block:: js

    on_barcode_updates: function(data){
      var self = this;
      if (data.message === 'update_partner_fields') {
        var def = new $.Deferred();
        if (data.action && data.action === 'unlink') {
        // partner is deleted. Make necessary updates in UI
          this.remove_unlinked_partners(data.partner_ids);
          def.resolve();
        } else {
        // reload partner data
            def = self.load_new_partners(data.partner_ids);
          }
        return def.done(function(){
          var opened_client_list_screen = self.gui.get_current_screen() === 'clientlist' && self.gui.screen_instances.clientlist;
          if (opened_client_list_screen){
            // rerender partner list
            opened_client_list_screen.update_client_list_screen(data.partner_ids);
          }
        });
      }
    },

