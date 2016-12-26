===========================
 JS access and inheritance
===========================

action_button
=============

Here you will find explanation of how to get/inherit action_button POS objects.

For example we have definition in `this file <https://github.com/odoo/odoo/blob/9.0/addons/pos_reprint/static/src/js/reprint.js#L1>`_::

    odoo.define('pos_reprint.pos_reprint', function (require) {
    ...
    screens.define_action_button({
        'name': 'guests',
        'widget': TableGuestsButton,
        'condition': function()

This defenition doesn't return class ReprintButton. So, we cannot inherit it in a usual way.

In order to reach that object we need get instance of it using ``gui``. Then we can inherit it

To make clear what this is like look up example where guests number button renderings::

    this.gui.screen_instances['products'].action_buttons['guests'].renderElement();

While you can make call and even replace function with new one, you are not able to make inheritance via ``extend`` or ``include`` functions. It's because we cannot reach Class and only get access to instance of that class.


This kind of approach make sense only for those widgets::

    DiscountButton
    ReprintButton
    TableGuestsButton
    SubmitOrderButton
    OrderlineNoteButton
    PrintBillButton
    SplitbillButton
    set_fiscal_position_button

screen_classes
==============


To create new screen widget (via the extend() method) or to modify existing screen widget (via the include() method) 
you need the target class. Usually you can get this class using following code: ::

    odoo.define('module_name.file_name', function (require) {
    "use strict";

    var screens = require('point_of_sale.screens');

    screens.OrderWidget.include({
        ...

But it is available only for widgets that are returned by main function in the file 
"point_of_sale/static/src/js/screens.js".

**List of the screens:**

- ReceiptScreenWidget
- ActionButtonWidget
- define_action_button
- ScreenWidget
- PaymentScreenWidget
- OrderWidget
- NumpadWidget
- ProductScreenWidget
- ProductListWidget

In other cases you can get targeted screen widget class using following code: ::

    odoo.define('module_name.file_name', function (require) {
    "use strict";

    var gui = require('point_of_sale.gui');

    gui.Gui.prototype.screen_classes.filter(function(el) { return el.name == 'clientlist'})[0].widget.include({
        ...

List of screens available via ``screen_classes``:

.. code-block:: js

    gui.define_screen({name: 'scale', widget: ScaleScreenWidget});
    gui.define_screen({name: 'products', widget: ProductScreenWidget});
    gui.define_screen({name: 'clientlist', widget: ClientListScreenWidget});
    gui.define_screen({name: 'receipt', widget: ReceiptScreenWidget});
    gui.define_screen({name: 'payment', widget: PaymentScreenWidget});
    gui.define_screen({name: 'bill', widget: BillScreenWidget});
    gui.define_screen({'name': 'splitbill', 'widget': SplitbillScreenWidget,
    gui.define_screen({'name': 'floors', 'widget': FloorScreenWidget, 
