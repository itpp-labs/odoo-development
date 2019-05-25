================
 Action Buttons
================

In POS module buttons above ``numpad`` are called ``Action Buttons``.

* These buttons only show up after installing ``pos_discount`` module (``Discount`` button, which allows defining the size of discount for the order) and ``pos_restaurant`` module (``Split``, ``Guests`` buttons etc.)

* You can create your own buttons assigning them to actions (for example ``open popup``, ``screen`` and etc).

* To create a Button you need to inherit ``ActionButtonWidget`` Class, select ``define_action_button`` and choose the necessary action after the pressing corresponding button.

**Consider, for example, the way of creating a simple Button, which opens popup-window.**

In order to use ``ActionButtonWidget``, which specified in Screens please start with downloading the ``screens`` widget:

.. code-block:: js

    var screens = require('point_of_sale.screens');

Then you need to declare a new variable and inherit ``ActionButtonWidget``:

.. code-block:: js

    var PopupButton = screens.ActionButtonWidget.extend({

    });

Thus ``PopupButton`` contains all methods from ``ActionButtonWidget``.
Now we need to define Template for our button:

.. code-block:: js

    template: 'PopupButton'

*where* the type of button you can find in ``Qweb``.

We define ``template`` in ``Qweb`` as follows:

.. code-block:: XML

    <t t-name="PopupButton">
        <div class="control-button">
            <i class="fa fa-list-alt" /> Popup Button
        </div>
    </t>

We also need to choose the Action, which which will be executed after we click the button. For this purpose we define ``button_click`` method.

.. code-block:: js

    button_click: function (){
	    this.gui.show_popup('confirm',{
		    'title': 'Popup',
		    'body': 'Opening popup after clicking on the button'',
	    });
    }

.. code-block:: js

    screens.define_action_button({
	    'name': 'popup_button',
	    'widget': PopupButton,
	    'condition': function (self) {
		return self.config.show_popup_button;
	    },
    });

*where:* ``name`` - Button name;

``widget`` - Button object;

``condition`` - Condition, which calls the button to show up (in our case, setting on ``show_popup_button`` option in POS config).

**Listing:**

.. code-block:: js

    odoo.define('pos_popup_button', function (require){
	    'use_strict';
	    var screens = require('point_of_sale.screens');

	    var PopupButton = screens.ActionButtonWidget.extend({
		    template: 'PopupButton',
		    button_click: function () {
			    this.gui.show_popup('confirm', {
				    'title': 'Popup',
				    'body': 'Opening popup after clicking on the button'',
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
