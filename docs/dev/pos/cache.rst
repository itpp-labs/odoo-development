=======
 Cache
=======

The ``init_from_JSON`` function allows providing data from the ``storage`` of the browser, which has been saved using ``export_as_JSON`` function.

While calling the function of saving unpaid orders in POS another function, which is ``export_as_JSON`` are called, which returns present data in the dictionary form and this data is saved in the ``storage`` of browser.

During downloading or updating the page with POS the ``init_from_JSON`` function is called, which gets saved data in the browser and actualize data for models. For example:

.. code-block:: js

    export_as_JSON: function () {
		var data = _super_order.export_as_JSON.apply(this, arguments);
		data.note = this.note;
		return data;
	},
	init_from_JSON: function (json) {
		this.note = json.note;
		_super_order.init_from_JSON.call(this, json);
	},

In code snippet below the saving of note for the order happens every time when ``export_as_JSON`` function are called.

In order to avoid the disappearance of note after updating or downloading POS (because the note has not been saved on the server), you need to update the variable using data which has been saved in browser with the ``init_from_JSON`` function.

===========
 Dom Cache
===========

One of the **examples** of using ``Dom Cache`` is the generation of product list.

This method allows using the browser cache during the next generation of dom elements of templates in POS, therefore, rendering time are decreased.

With elements generation you need to check whether saved data in cache for this element:

.. code-block:: js

    this.cache = new screens.DomCache();
    var key = item.id;
    var cache = this.cache.get_node(key);

In case if the cache is found you need to use this cache as dom element template, otherwise you need to save the result of generation:

.. code-block:: js

   if (!cache) {
	var item_html = QWeb.render('ITEM_TEMPLATE', {
		widget: this,
		item: item,
	});
	var item_node = document.createElement('div');
	item_node.innerHTML = item_html;
	item_node = item_node.childNodes[1];
	this.cache.cache_node(key, item_node);
	return item_node;
    }

A complete listing of the ``DomCache`` usage can be presented as follows:

.. code-block:: js

    init: function () {
		this._super(parent, options);
		this.cache = new screens.DomCache();
	},
	template: 'TEMPLATE',
	item_template: 'ITEM_TEMPLATE',
	renderElement: function () {
		var self = this;
		var el_str = QWeb.render(this.template, {widget: this});
		var el_node = document.createElement('div');
		el_node.innerHTML = el_str;
		el_node = el_node.childNodes[1];

		if (this.el && this.el.parentNode) {
			this.el.parentNode.replaceChild(el_node, this.el);
		}
		this.el = el_node;
		var list_container = el_node.querySelector('.item-list');
		this.items.forEach(function (item) {
			var item_node = self.render_item(item);
			list_container.appendChild(product_node);
		})
	},
	render_item: function (item) {
		var key = item.id;
		var cached = this.cache.get_node(key);
		if (!cached) {
			var product_html = QWeb.render(this.item_template, {
				widget: this,
				item: item,
			});
			var item_node = document.createElement('div');
			item_node.innerHTML = item_html;
			item_node = item_node.childNodes[1];
			this.cache.cache_node(key, item_node);
			return item_node;
		}
		return cached;
	},
