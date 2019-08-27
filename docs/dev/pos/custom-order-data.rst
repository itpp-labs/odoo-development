======================================
 Custom order data in browser storage
======================================

Before the payment orders in POS are kept in browser storage. Thereby if we again open POS module (should not be confused with the closing of the session) the system automatically retrieves data from the storage.

If your model adds data (of the field), then you need to make additional data processing in order to save this data among reopenings.

Because of the browser storage (*localStorage*) allows saving data only with the type String POS converts the ``Order`` object to the String and inversely.

For this purpose following methods are used:

* ``init_from_JSON``: function reads parameters of the order from the *json-String* and saves to the current object (see realization of the Orderline `here <https://github.com/odoo/odoo/blob/8d7ee3921384ce070d3333cbc4073ffc4f8febc4/addons/point_of_sale/static/src/js/models.js#L1365-L1383>`__ and for the Model `there <https://github.com/odoo/odoo/blob/8d7ee3921384ce070d3333cbc4073ffc4f8febc4/addons/point_of_sale/static/src/js/models.js#L2024-L2082>`__)

* ``export_as_JSON``: function converts the current object to *json-String* (see realization of the Orderline `here <https://github.com/odoo/odoo/blob/8d7ee3921384ce070d3333cbc4073ffc4f8febc4/addons/point_of_sale/static/src/js/models.js#L2083-L2110>`__ and for the Model `there <https://github.com/odoo/odoo/blob/8d7ee3921384ce070d3333cbc4073ffc4f8febc4/addons/point_of_sale/static/src/js/models.js#L1558-L1576>`__)

When order is updated ``export_as_JSON`` is called and data are saved to browser storage.

Now, if you close page and reopen, then at some point ``init_from_JSON`` is called to restore order from *json string*.

Let's take the example:

``POS Advanced Order Notes`` module
===================================

This `module <https://github.com/it-projects-llc/pos-addons/blob/12.0/pos_order_note/static/src/js/order_note.js#L88-L102>`__ allows adding notes to the entire order, to use already predefined notes and to speed up the process of creating orders by specifying products also via notes, which can be automatically applied further.

.. code-block:: js

    export_as_JSON: function () {
      var data = _super_order.export_as_JSON.apply(this, arguments);
      data.note = this.note;
      return data;
    },
    init_from_JSON: function (json) {
      this.note = json.note;
      _super_order.init_from_JSON.call(this, json);
    },

When you add the note to your Order, the trigger which calls ``export_as_JSON`` launches to convert data of current order into string (including notes) and save it in browser storage.

While loading POS in order to get saved notes from the browser storage, you need to extend ``init_from_JSON`` function.

Without this code, your module will work, but if you reload POS, your notes will not be presented (because they are not saved).
