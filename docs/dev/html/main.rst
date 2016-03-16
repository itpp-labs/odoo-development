Active elements
---------------
Link-button that calls controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Code::

	<form action="/shop/checkout" name="myform" method="post">
		<a class="btn btn-primary a-submit">My button</a>
	</form>

Here action="/shop/checkout" sets controller address. Class a-submit usually means do what in 'action' of form.

Submit with button
^^^^^^^^^^^^^^^^^^
Code::

	<form action="/my_page" name="myform" method="post">
		<button type="submit" class="btn btn-default">My button</button>
	</form>

Wherein in controller in **post will be available some values from source form, those like <input/>.
