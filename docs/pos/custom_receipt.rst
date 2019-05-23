================
 Custom Receipt
================

There are two types of receipts in POS:

1. ``PosTicket`` - displays on screen after payment;
2. ``XmlReceipt`` - prints in PosBox after pressing the button Print receipt on the Payment screen if PosBox connected with the ESC POC printer.

These two receipts are implemented on ``Qweb`` and generated after purchase order. If ``PosTicket`` allows any design in ``Qweb``, then for ``XmlReceipt`` you can use only strictly defined tags, which supported by the ESC POC printer.

Using ``t-extend`` mechanism, which takes the template's name to be modified as a parameter, you can extend existing ``Qweb`` templates for receipts. After that, a modification with any number t-jquery sub-directives can be performed.

``t-jquery`` directives use the CSS selector. This selector is used in the extended template for choosing context nodes, for which ``t-operation`` can be applied. If you want to add, for example, another title for Product in ``XmlReceipt``, you need to create ``Qweb`` with the following content:

.. code-block:: XML

    <t t-extend="XmlReceipt">
        <t t-jquery="t[t-if='simple'] line" t-operation="after">
            <t t-set="second_product_name" t-value="line.second_product_name"/>
                <t t-if="pos.config.show_second_product_name_in_receipt and second_product_name">
                    <line>
                        <left>(<t t-esc='second_product_name' />)</left>
                    </line>
                </t>
            </t>
        </t>
    </t>

For the same action for PosTicket:

.. code-block:: XML

    <t t-extend="PosTicket">
	    <t t-jquery=".receipt-orderlines tr[t-foreach='orderlines']" t-operation="append">
		<t t-set="second_product_name" t-value="orderline.get_product().second_product_name"/>
		</t>
    </t>

One of the difficult but at the same time flexible method of creating Customer receipt is to download the field from the Server, where ``Qweb`` template is described in the text form. After downloading and before printing this text template need to be converted into ``XML format`` and produced data based on this template.

.. code-block:: python

    template_receipt_qweb = fields.Text(string="Custom Receipt Qweb")

In POS you need to convert this text format into ``XML`` and generate a receipt using this template:

.. code-block:: js

    convert_to_xml: function (template) {
	    var parser = new DOMParser();
	    var xmlDoc = parser.parseFromString(template, "text/xml");
	    return xmlDoc.documentElement;
    },

Usage of this template instead of standards ones requires to generate received ``XML``, in order to do this you need to connect ``Qweb``:

.. code-block:: js

    var core = require('web.core');
    var Qweb = core.qweb;

To define a custom function, which will generate a user's ``Qweb`` as follows:

.. code-block:: js

    custom_qweb_render: function (template, options) {
	    var template_name = $(template).attr('t-name');
	    Qweb.templates[template_name] = template;
	    return Qweb._render(template_name, options);
    },

This function needs to be called every time when the receipt is generated.
