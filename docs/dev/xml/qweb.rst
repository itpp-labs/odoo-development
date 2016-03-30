Basic stuff
===========

Call method of some model and put result in variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Code::

	<t t-set="order" t-value="website.sale_get_order()"/>

Here *website* means you use website=True in controller. TODO my be wrong.

Get value of some setting ir.config_parameter and put it in variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Code::

	<t t-set="foobar" t-value="website.env['ir.config_parameter'].get_param('my_module.foobar')"/>

Show value of variable
^^^^^^^^^^^^^^^^^^^^^^
Code::

	<p><t t-esc="foobar"/></p>

Use variable in condition
^^^^^^^^^^^^^^^^^^^^^^^^^
Code::

	<label t-if="foobar">
		<p>foobar is true</p>
	</label>

Get variable transmitted by render() in XML template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Code::

	t-att-value="my_var"

my_var is element of 'values' dictionary (second argument of render()).

