JS access and inheritance
=========================

action_button
-------------

Here you will find explanation of how to get/inherit action_button POS objects.

For example we have definition in /../../../*js file::

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
