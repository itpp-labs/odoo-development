=======================
 Multi-session Support
=======================

``pos_multi_session`` is a module, which allows synchronizing data in POSes within one multi_session.

In order to synchronize new user data Order or Orderline models of one POS with others, you no need to add a new module ``pos_multi_session`` into ``depends`` on your module, you need to extend such methods as ``export_as_JSON``, ``init_from_JSON`` and add the method ``apply_ms_data``.

Сonsider the **Example of synchronization for the Order model.**

Let us have some data for the order and we need to synchronize it with all POSes, which use the same multi-session:


.. code-block:: js

    apply_ms_data: function (data) {
		// This methods is added for compatibility with module https://www.odoo.com/apps/modules/10.0/pos_multi_session/
		/*
		    It is necessary to check the presence of the super method
		    in order to be able to inherit the apply_ms_data
		    without calling require('pos_multi_session')
		    and without adding pos_multi_session in dependencies in the manifest.

		    At the time of loading, the super method may not exist. So, if the js file is loaded
		    first among all inherited, then there is no super method and it is not called.
		    If the file is not the first, then the super method is already created by other modules,
		    and we call super method.
		*/
		if (_super_order.apply_ms_data) {
			_super_order.apply_ms_data.apply(this, arguments);
		}
		this.first_new_variable = data.first_new_variable;
		this.second_new_variable = data.second_new_variable;
		// etc ...

		/* Call renderElement direclty or trigger corresponding event if you need to rerender something after updating */
	},
	export_as_JSON: function () {
		// export new data as JSON
		var data = _super_order.export_as_JSON.apply(this, arguments);
		data.first_new_variable = this.first_new_variable;
		data.second_new_variable = this.second_new_variable;
		return data;
	},
	init_from_JSON: function (json) {
		// import new data from JSON
		this.first_new_variable = json.first_new_variable;
		this.second_new_variable = json.second_new_variable;
		return _super_order.init_from_JSON.call(this, json);
	}
