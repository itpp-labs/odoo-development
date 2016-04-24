POS screen widget subclassing and modifying
===========================================

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
