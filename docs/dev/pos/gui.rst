JS access and inheritance
=========================

action_button
-------------

Here you will find explanation of how to get/inherit action_button POS objects.

For example we got JS object::

    odoo.define('pos_reprint.pos_reprint', function (require) {
    ...
    screens.define_action_button({
        'name': 'reprint',
        'widget': ReprintButton,
        'condition': function()

Owner object (pos_reprint.pos_reprint) do not exports (returns) any data.

In order to get access (inherit) to that object we need get instance of it using gui.
To make clear what this is like look up example where guests number button renderings::

    this.gui.screen_instances['products'].action_buttons['guests'].renderElement();

Here *this.gui.screen_instances["products"].action_buttons['guests'].prototype* is undefined. So using of
extend or include is impossible.

This kind of approach make sense only for those widgets::

    DiscountButton
    ReprintButton
    TableGuestsButton
    SubmitOrderButton
    OrderlineNoteButton
    PrintBillButton
    SplitbillButton
    set_fiscal_position_button
