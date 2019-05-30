================
 Custom Screens
================

List of **partners**, **payment's screen**, and **floor screen** are examples of ``screens``.

We will consider *an example of creating the User interface*.

In order to create a new ``custom screen`` we plug ``screens`` and ``gui``:

.. code-block:: js

    var screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');

Then we declare a new variable and inherit ``ScreenWidget``:

.. code-block:: js

    var CustomScreenWidget = screens.ScreenWidget.extend({
    });

Now ``CustomScreenWidget`` consist of all methods from ``ScreenWidget``. Then we need to define a template, where the structure of the screen is described using ``Qweb``:

.. code-block:: js

    template: 'CustomScreenWidget'

In ``Qweb`` we define a template as follows:

.. code-block:: XML

    <t t-name="CustomScreenWidget">
      <div class="custom-screen screen">
        <div class="screen-content">
           <section class="top-content">
             <span class="button back">
               <i class="fa fa-angle-double-left" />
                 Cancel
             </span>
             <span class="button next oe_hidden highlight">
                 Apply
               <i class="fa fa-angle-double-right" />
             </span>
           </section>
           <section class="full-content">
             <div class="window">
               <section class="subwindow collapsed">
                 <div class="subwindow-container collapsed">
                   <div class="subwindow-container-fix custom-details-contents" />
                 </div>
               </section>
             </div>
           </section>
      </div>
    </t>


Define styles in ``css`` file, which you need for the screen.

This ``Qweb`` will be rendered every time when the method ``renderElement`` runs (prior to the downloading POS all screens are drawn and hidden already). This method can be redefine and, for example, used for actions of  ``back`` and ``next`` buttons:

.. code-block:: js

    renderElement: function () {
      this._super();

	this.$('.back').click(function () {
      self.gui.back();
	});

	this.$('.next').click(function () {
      // some actions
      });
    },

All screens are hidden by default (except those, which are called after POS downloading).
In order to open Custom Screens you need to define it inside screens' list:

.. code-block:: js

    gui.define_screen({name:'custom_screen', widget: CustomScreenWidget});

In order to open Custom Screen you need to call the next function (for example after click to the Action button):

.. code-block:: js

    this.gui.show_screen('custom_screen');

*where* ``this`` is a pointer to ``PosModel``.

For a concrete example check the **POS Orders History** `module <https://github.com/it-projects-llc/pos-addons/blob/12.0/pos_orders_history/static/src/js/screens.js#L311>`__ ,
where ``orders_history_screen`` is defined.