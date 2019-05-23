=============
 Inheritance
=============

POS has two types of classes: Models, Widget. Extending those classes are slightly different.

.. note::

    Not all classes has easy way to get them to inherit.
    Some tricks are available `here <https://odoo-development.readthedocs.io/en/latest/dev/pos/gui.html>`__ .

Model
=====

Model classes work with data only and don't work with UI directly.

To extend that kind of class, you need to use ``extend`` method. It creates a copy of class with redefined method. Normally, you need to override original class with updated one. Also, to call original method, put original class to a variable.

Here is an `example <https://github.com/it-projects-llc/pos-addons/blob/fb8b072/pos_debt_notebook/static/src/js/pos.js#L23-L33>`__:

.. code-block:: js

    odoo.define('pos_debt_notebook.pos', function (require) {
        "use strict";

        var models = require('point_of_sale.models');

        // save original class
        var _super_posmodel = models.PosModel.prototype;
        // override original class with extended one
        models.PosModel = models.PosModel.extend({
            initialize: function (session, attributes) {
                var self = this;
                // some new code in this method
                models.load_fields('product.product',['credit_product']);
                // call original method via "apply"
                _super_posmodel.initialize.apply(this, arguments);
        },
    })

Widget
======

Widget classes work with UI.

Widget extend is much easier than Model extending: just use ``include`` and ``_super``.

Here is an `example <https://github.com/it-projects-llc/pos-addons/blob/fb8b072/pos_debt_notebook/static/src/js/pos.js#L379-L385>`__:

.. code-block:: js

    odoo.define('pos_debt_notebook.pos', function (require) {
    "use strict";
    var screens = require('point_of_sale.screens');

    // "include" updates original method
        screens.PaymentScreenWidget.include({
            init: function(parent, options) {
            // call super in a easy way
            this._super(parent, options);
            // add some new code
            this.pos.on('updateDebtHistory', function(partner_ids){
                this.update_debt_history(partner_ids);
            }, this);
        },
    })
    })
