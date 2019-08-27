================
 Action Buttons
================

``Action Buttons`` are following buttons:

* ``Note``
* ``Transfer``
* ``Guests``
* ``Bill``
* ``Split``
* ``Order``
* ``Discount``
* etc.

that are located above **Numpad**.

* These buttons only show up after installing **pos_discount** module (``Discount`` button, which allows defining the size of discount for the order) and **pos_restaurant** module (``Split``, ``Guests`` buttons etc.)

* You can create your own buttons assigning them to actions (for example **open_popup**, **screen** and etc).

* To create a Button you need to inherit **ActionButtonWidget** Class, select **define_action_button** and choose the necessary action after the pressing corresponding button.

*Consider, for example, the way of creating a simple Button, which opens popup-window.*

.. code-block:: js

    odoo.define('pos_popup_button', function (require){
      'use_strict';
      /*
      In order to use ActionButtonWidget, which specified in Screens
      please start with downloading the screens widget
      */

     var screens = require('point_of_sale.screens');

    //declare a new variable and inherit ActionButtonWidget

    var PopupButton = screens.ActionButtonWidget.extend({
      /*
      Thus PopupButton contains all methods from ActionButtonWidget.
      Now we need to define Template for our button,
      where the type of button you can find in Qweb (see below)
      */

    template: 'PopupButton',
      /*
      We also need to choose the Action,
      which which will be executed after we click the button.
      For this purpose we define button_click method, where
      where name - Button name; widget - Button object;
      condition - Condition, which calls the button to show up
      (in our case, setting on show_popup_button option in POS config).
      */

    button_click: function () {
      this.gui.show_popup('confirm', {
        'title': 'Popup',
        'body': 'Opening popup after clicking on the button',
        });
        }
      });

    screens.define_action_button({
      'name': 'popup_button',
      'widget': PopupButton,
      'condition': function () {
      return this.pos.config.popup_button;
        },
        });
    return PopupButton;
    });

The definition of the ``template`` in ``Qweb``:

.. code-block:: XML

    <t t-name="PopupButton">
      <div class="control-button">
        <i class="fa fa-list-alt" /> Popup Button
      </div>
    </t>

For a concrete example check the **POS Orders History** `module <https://github.com/it-projects-llc/pos-addons/blob/12.0/pos_orders_history/static/src/js/screens.js#L22>`__ ,
where you can see that a button with the label *Orders History* is added.
