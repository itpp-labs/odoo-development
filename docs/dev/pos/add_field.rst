Add new field in the model of POS module
========================================

To add new field in POS modules necessary in models.js override PosModel in the parent models which we take from **point_of_sale.models**.

For example:

.. code-block:: js

    var models = require('point_of_sale.models');
    var _super_posmodel = models.PosModel.prototype;

    models.PosModel = models.PosModel.extend({
        initialize: function (session, attributes) {
            // New code
            var partner_model = _.find(this.models, function(model){
                return model.model === 'product.product';
            });
            partner_model.fields.push('qty_available');

            // Inheritance
            return _super_posmodel.initialize.call(this, session, attributes);
        },
    });