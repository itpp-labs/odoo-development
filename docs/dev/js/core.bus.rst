==========
 core.bus
==========

core.bus (web.bus in 8.0) is used handle js events between modules.

Usage
=====

.. code-block:: js

   // 8.0
   var bus = openerp.web.bus;

   // 9.0+
   var core = require('web.core');
   var bus = core.bus;

   // bind event handler
   bus.on('barcode_scanned', this, function (barcode) { 
      //...
   })

   // trigger event
   bus.trigger('barcode_scanned', barcode);


