==========================
 ``odoo.define`` function
==========================

Official doc about the topic is `here: <https://www.odoo.com/documentation/12.0/reference/javascript_reference.html#javascript-module-system>`__

*Javascript Module* in odoo is some piece of code declared via ``odoo.define('js_module_name', ...)`` and can be used in other modules via ``require('js_module_name')``.

**Example:**

.. code-block:: js

    odoo.define('js_module_name', function (require) {
      "use strict";
      var A = require('js_module_name_A');
      var B = require('js_module_name_B');
      require('js_module_name_C');

      // some code
      return something;
    });

.. warning::

    You cannot rename variable ``require``.

.. note::

    Single file may have several *JS modules*, though it's recommended to put them to different files

.. note::

    You can use any string as a module name, but recommended way is ``<ODOO_MODULE>.<JS_MODULE>``, e.g. ``point_of_sale.popups``

Return value
============

A js-module may return value. That value can be used in another js-modules (of the same odoo-module or others).

For example:

.. code-block:: js

    odoo.define('point_of_sale.gui', function (require) {
      "use strict";
        return {
          Gui: Gui,
          define_screen: define_screen,
          define_popup: define_popup,
	    };
    });

Then, we can use ``define_screen`` as following:

.. code-block:: js

    odoo.define('point_of_sale.screens', function (require) {
      "use strict";
        var gui = require('point_of_sale.gui');
        //...
          gui.define_screen({
          name: 'scale',
          widget: ScaleScreenWidget
          });
        // ..
	  return ....
    })

.. note::

    If you don't to use value returned by another js-module, you still might you you *import js-module* (via require(....)) to be sure that that module is loaded before executing you module.

Asynchronous modules
---------------------

It can happen that a module needs to perform some work before it is ready. For
example, it could do a rpc to load some data. In that case, the module can simply return a deferred (promise). In that case, the module system will simply wait for the deferred to complete before registering the module.

.. code-block:: js

    odoo.define('module.Something', function (require) {
      "use strict";
        var ajax = require('web.ajax');
          return ajax.rpc(...).then(function (result) {
          // some code here
        return something;
      });
    });
