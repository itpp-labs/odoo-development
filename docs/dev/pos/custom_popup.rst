===========================
Creation of Custom Pop-Ups
===========================

Use the Custom Pop-Ups to provide information or to prompt Users to do something in POS. You can define the appearance of a pop-up.

**Let take the example of the creation a pop-up of** ``QR Code Scanning in POS`` `module <https://github.com/it-projects-llc/pos-addons/blob/6eaac4e168d7cf854d302b298b068e2b38db822c/pos_qr_scan/static/src/js/qr_scan.js>`__ , where we needed to create a pop-up to show the video from camera to scan QR codes.

First, attach necessary `requirements:
<https://github.com/it-projects-llc/pos-addons/blob/6eaac4e168d7cf854d302b298b068e2b38db822c/pos_qr_scan/static/src/js/qr_scan.js#L10::>`__

.. code-block:: js

    var PopupWidget = require('point_of_sale.popups');

Then, create a new instance, the new default pop-up `extension:
<https://github.com/it-projects-llc/pos-addons/blob/6eaac4e168d7cf854d302b298b068e2b38db822c/pos_qr_scan/static/src/js/qr_scan.js#L29-L30::>`__

.. code-block:: js

    var QrScanPopupWidget = PopupWidget.extend({
    // It requires the template attribute with a Qweb template name for showing pop-up
    template: 'QrScanPopupWidget',

To make the pop-up be reachable with regular methods after the ``QrScanPopupWidget`` declaration do the `following:
<https://github.com/it-projects-llc/pos-addons/blob/6eaac4e168d7cf854d302b298b068e2b38db822c/pos_qr_scan/static/src/js/qr_scan.js#L194::>`__

.. code-block:: js

    gui.define_popup({name:'qr_scan', widget: QrScanPopupWidget});


so it can be called with the next `code:
<https://github.com/it-projects-llc/pos-addons/blob/6eaac4e168d7cf854d302b298b068e2b38db822c/pos_qr_scan/static/src/js/qr_scan.js#L17-L20::>`__

.. code-block:: js

    this.gui.show_popup('qr_scan',{
      'title': 'QR Scanning',
      'value': false,
    });
