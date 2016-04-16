CSS tips and tricks
===================

Add your css on template
^^^^^^^^^^^^^^^^^^^^^^^^
Code::

	<template id="my_module_frontend" name="my_module assets" inherit_id="website_sale.assets_frontend">
	    <xpath expr="//link[@rel='stylesheet']" position="after">
	        <link rel="stylesheet" href="/my_module/static/src/css/main.css"/>
	    </xpath>
	</template>

*website_sale.assets_frontend* is what you inherits.

Hide fields
^^^^^^^^^^^
Hide all children (that have attribute bill='1') of oe_website_sale class owner (that have attribute bill_enabled='0')::

	.oe_website_sale[bill_enabled='0'] [bill='1']{
	    display:none;
	}
