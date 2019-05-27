============================
 POS Order Creation Process
============================

When POS Order is created and paid the data to be sent to the server gets composed with the ``export_as_JSON`` `method. <https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/static/src/js/models.js#L2077::>`__

Here the talk goes only about ``export_as_JSON``  for order model.

Similar methods for ``Orderline``, ``Packlotline``, ``Paymentline`` are skipped.

Any custom data needed to be uploded to the server is has to be added with this method.

For example ``POS Debt & Credit notebook`` `module <https://github.com/it-projects-llc/pos-addons/blob/fb8b0724fd4b5a0e66a64ece17643025e45330a8/pos_debt_notebook/static/src/js/pos.js#L249-L253::>`__, where we send to the server one more custom variable ``updates_debt``:


.. code-block:: js

    export_as_JSON: function(){
        var data = _super_order.export_as_JSON.apply(this, arguments);
        data.updates_debt = this.updates_debt();
        return data;
    },

The created order is sent to the server and be processed with the **create_from_ui** `method: <https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/models/pos_order.py#L722-L751>`__

The method might be called for several orders at once so we will take a look at the ``_process_order``: the function called to create a ``pos.order`` record out of the incoming order data dictionary for each incoming POS `order:
<https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/models/pos_order.py#L116-L155>`__

For example in our ``POS Debt & Credit notebook`` `module
<https://github.com/it-projects-llc/pos-addons/blob/fb8b0724fd4b5a0e66a64ece17643025e45330a8/pos_debt_notebook/models.py#L493-L520>`__ we inherit and override this method in order to process so called 'Zero transactions on credit payments' journals:


.. code-block:: python

    def _process_order(self, pos_order):
        credit_updates = []
        amount_via_discount = 0
        for payment in pos_order['statement_ids']:
            journal = self.env['account.journal'].browse(payment[2]['journal_id'])
            if journal.credits_via_discount:
                amount = float(payment[2]['amount'])
                product_list = list()
                amount_via_discount += amount
                for o_line in pos_order['lines']:
                    o_line = o_line[2]
                    name = self.env['product.product'].browse(o_line['product_id']).name
                    product_list.append('%s(%s * %s) + ' % (name, o_line['qty'], o_line['price_unit']))
                product_list = ''.join(product_list).strip(' + ')
                credit_updates.append({'journal_id': payment[2]['journal_id'],
                                       'balance': -amount,
                                       'partner_id': pos_order['partner_id'],
                                       'update_type': 'balance_update',
                                       'note': product_list,
                                       })
                payment[2]['amount'] = 0
        pos_order['amount_via_discount'] = amount_via_discount
        order = super(PosOrder, self)._process_order(pos_order)
        for update in credit_updates:
            update['order_id'] = order.id
            entry = self.env['pos.credit.update'].sudo().create(update)
            entry.switch_to_confirm()
        return order

We update payment data before the ``pos.order`` record was created on the call of the super method.

All paymentlines with **credits_via_discount** journals are removed and replaced with ``pos.credit.update`` model record, so the order has no such kind of payments.

All Non-Transaction paid amounts is counted in the ``amount_via_discount`` order `attribute.
<https://github.com/it-projects-llc/pos-addons/blob/fb8b0724fd4b5a0e66a64ece17643025e45330a8/pos_debt_notebook/models.py#L515>`__

Later, within the **create_from_ui** the ``action_pos_order_paid`` `method <https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/models/pos_order.py#L740>`__ is called, which we override to set discounts with total discount amount equals to `amount_via_discount` for POS order lines to make the order be `finished <https://github.com/it-projects-llc/pos-addons/blob/fb8b0724fd4b5a0e66a64ece17643025e45330a8/pos_debt_notebook/models.py#L528-L530>`__

Order completeness is checked in the ``test_paid`` `method. <https://github.com/odoo/odoo/blob/33f1e5f64be0113e4e3ad7cb8de373d8ab5daa7b/addons/point_of_sale/models/pos_order.py#L753-L762>`__
