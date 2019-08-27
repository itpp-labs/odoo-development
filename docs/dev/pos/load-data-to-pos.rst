=====================
 Loading data to POS
=====================

By default POS uploads next models:

``res.users``, ``res.company``, ``decimal.precision``, ``uom.uom``, ``res.partner``, ``res.country``, ``account.tax``, ``pos.session``, ``pos.config``, ``res.users``, ``stock.location``, ``product.pricelist``, ``product.pricelist.item``, ``product.category``, ``res.currency``, ``pos.category``, ``product.product``, ``account.bank.statement``, ``account.journal``, ``account.fiscal.position``, ``account.fiscal.position.tax``.

If we've added a new field in the backend and want them to be presented in the POS we can use **load_fields method** inside the ``PosModel`` **initialize function**.

In the next example taken from ``POS Debt & Credit notebook`` module we add some new fields to the ``account.journal`` `model:
<https://github.com/it-projects-llc/pos-addons/blob/fb8b0724fd4b5a0e66a64ece17643025e45330a8/pos_debt_notebook/static/src/js/pos.js#L29-L30::>`__

.. code-block:: js

    var models = require('point_of_sale.models');
    models.load_fields('account.journal', ['debt', 'debt_limit', 'credits_via_discount', 'pos_cash_out',
                        'category_ids', 'credits_autopay']);

In order to upload a new model into POS we use ``load_models(models,options)``.
Description's taken from `odoo
<https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/static/src/js/models.js#L1175-L1215::>`__ .

Loads ``openerp`` models at the point of sale startup.

``load_models`` take an array of model loader declarations.

The models will be loaded in the array order. If no ``openerp`` model name is provided, no server data will be loaded, but the system can be used to preprocess data before load.

Loader arguments can be functions that return a dynamic value. The function takes the ``PosModel`` as the first argument and a temporary object that is shared by all models, and can be used to store transient information between model loads.

There is no dependency management. The models must be loaded in the right order. Newly added models are loaded at the end but the after / before options can be used to load directly before / after another model.

.. code-block:: js

    models: [{
        model: [string] the name of the openerp model to load.
        label: [string] The label displayed during load.
        fields: [[string]|function] the list of fields to be loaded.
                Empty Array / Null loads all fields.
        order:  [[string]|function] the models will be ordered by the provided fields
        domain: [domain|function] the domain that determines what
                models need to be loaded. Null loads everything
        ids:    [[id]|function] the id list of the models that must
                be loaded. Overrides domain.
        context: [Dict|function] the openerp context for the model read
        condition: [function] do not load the models if it evaluates to
                false.
        loaded: [function(self,model)] this function is called once the
                models have been loaded, with the data as second argument
                if the function returns a deferred, the next model will
                wait until it resolves before loading.
     }]

    options:
        before: [string] The model will be loaded before the named models
                (applies to both model name and label)
        after:  [string] The model will be loaded after the (last loaded)
                named model. (applies to both model name and label)


Example below uploads all records meet the domain ``account.invoice`` model.

The **loaded** function is a handler for uploaded data.

Here you can proceed and save this `example <https://github.com/it-projects-llc/pos-addons/blob/d0323907e35082d6d10416c2f7ef8497aa47dc31/pos_invoice_pay/static/src/js/main.js#L51-L64::>`__ which is taken from ``Pay Sale Orders & Invoices over POS`` module:

.. code-block:: js

    var models = require('point_of_sale.models');
      models.load_models({
        model: 'account.invoice',
        fields: ['name', 'partner_id', 'date_invoice', 'number', 'date_due', 'origin', 'user_id ', 'residual ', 'state ', 'amount_untaxed ', 'amount_tax '],
        domain: [['state', '=', 'open'],['type', '=', 'out_invoice']],
        loaded: function (self, invoices) {
          var invoices_ids = _.pluck(invoices, 'id');
          self.prepare_invoices_data(invoices);
          self.invoices = invoices;
          self.db.add_invoices(invoices);
          self.get_invoice_lines(invoices_ids);
      }
    });

