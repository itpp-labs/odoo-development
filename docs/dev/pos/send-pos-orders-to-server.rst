==============================
 Sending POS Orders to Server
==============================

This article describes the process of sending POS Orders to odoo server and demonstrates possible usage of extending it.


The general process is as follows:

Client side:

* ``export_as_JSON``: combines *order data* to send to the server

* then *order* is saved to browser cache

* then POS tries to send data to server


Backend side:

* ``create_from_ui``: data come to POS (see `here <https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/models/pos_order.py#L722-L751>`__)

* ``_process_order``: process order json (created records in database, etc. see `here <https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/models/pos_order.py#L116-L155>`__)

* ``_order_fields``: prepare dictionary for create method (see `how <https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/models/pos_order.py#L34-L50>`__)

So, in order to pass additional information and handle it on server we need:

* extend ``export_as_JSON`` in client side
* extend ``_process_order`` in server side

Let's check it on example:

``Saving removed products of POS order`` module
===============================================

The module allows to add a reason on canceling order or orderline in POS.

In order to do it we:

* extend ``export_as_JSON`` in client side (see `here <https://github.com/it-projects-llc/pos-addons/blob/c5539c847d0656f6885087e27e497b8d985f1e31/pos_order_cancel/static/src/js/models.js#L138-L144>`__)

.. code-block:: js

    export_as_JSON: function() {
      var data = _super_order.export_as_JSON.apply(this, arguments);
      /* canceled_lines is used only on the client side
      to cache those data in order to prevent misbehavior
      in case the page was refreshed
      */
      data.canceled_lines = this.canceled_lines || [];
      // updata data to be sent to the server
      data.reason = this.reason;
      data.is_cancelled = this.is_cancelled;
      return data;
    },


* extend ``_process_order`` in server side (see `here <https://github.com/it-projects-llc/pos-addons/blob/c5539c847d0656f6885087e27e497b8d985f1e31/pos_order_cancel/models/models.py#L56-L62>`__)

.. code-block:: python

    @api.model
    def _process_order(self, pos_order):
        order = super(PosOrder, self)._process_order(pos_order)
        if 'is_cancelled' in pos_order and pos_order['is_cancelled'] is True:
            if pos_order['reason']:
                 order.cancellation_reason = pos_order['reason'].encode('utf-8')
            order.is_cancelled = True
        return order
