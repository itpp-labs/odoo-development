===========
 Dom Cache
===========

Dom Cache is used to save rendered elements to speed POS up.

To add something to Dom Cache you need to do something like this:

.. code-block:: js

    this.cache = new screens.DomCache();
    this.cache.cache_node(key, value);

To restore rendered element from cache do something like this

.. code-block:: js

    this.cache = new screens.DomCache();
    var cache = this.cache.get_node(key);

Here is complete example from Point of Sale `module <https://github.com/odoo/odoo/blob/12.0/addons/point_of_sale/static/src/js/screens.js#L761-L789>`__:

The purpose of this code is the optimization of the elements rendering in POS. Each new POS loading use data from ``DomCache`` - thereby save time for the rendering of new elements.

Let's take the example:

``POS Order History`` module
============================

In this  in this `module <https://github.com/it-projects-llc/pos-addons/blob/12.0/pos_orders_history/static/src/js/screens.js#L159-L198>`__ ``DomCache`` is used when the orders' list renders.

After the first loading POS elements of orders, which have been rendered (*HTML code*), are saved in Cache.

After reloading POS the existence of saved elements in Cache are checked and this data is used when orders are rendered.

.. code-block:: js

    init: function(parent, options) {
      this._super(parent, options);
      //object of DomCache,which we will use in order to address the methods of this object
      this.orders_history_cache = new screens.DomCache();
    },
    render_list: function(orders) {
      var contents = this.$el[0].querySelector('.order-list-contents');
      contents.innerHTML = "";
      for (var i = 0, len = Math.min(orders.length,1000); i < len; i++) {
        var order = orders[i];
        // getting cache via key
        var orderline = this.orders_history_cache.get_node(order.id);
        var lines_table = this.orders_history_cache.get_node(order.id + '_table');
        /* here we check for the presence of cache among existing data
        if there is no cache, then we render elements and save into cache
        if the cache exists, we just use it
        */
        if ((!orderline) || (!lines_table)) {
        // rendering of elements may take time
          var orderline_html = QWeb.render('OrderHistory',{widget: this, order:order});
          orderline = document.createElement('tbody');
          lines_table = document.createElement('tr');
          var $td = document.createElement('td');
            if (order.lines) {
             $td.setAttribute("colspan", 8);
            }
          lines_table.classList.add('line-element-hidden');
          lines_table.classList.add('line-element-container');

          var line_data = this.get_order_line_data(order);
          var $table = this.render_lines_table(line_data);

          $td.appendChild($table);
          lines_table.appendChild($td);

          orderline.innerHTML = orderline_html;
          orderline = orderline.childNodes[1];
          //save the result into cache
          this.orders_history_cache.cache_node(order.id, orderline);
          this.orders_history_cache.cache_node(order.id + '_table', lines_table);
        }
        contents.appendChild(orderline);
        contents.appendChild(lines_table);
      }
    },
