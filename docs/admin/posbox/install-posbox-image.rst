=====================
 PosBox installation
=====================

Download last version ``posbox_image``:

   * https://nightly.odoo.com/master/posbox/

.. note:: Use another computer with an SD card reader to install the image.

You will need to use an image writing tool to install the image you have downloaded on your SD card.

**Etcher** is a graphical SD card writing tool that works on Mac OS, Linux and Windows, and is the easiest option for most users. Etcher also supports writing images directly from the zip file, without any unzipping required.
To write your image with Etcher:

   - Download `Etcher <https://etcher.io/>`_ and install it.
   - Connect an SD card reader with the SD card inside.
   - Open Etcher and select from your hard drive the Raspberry Pi ``.img`` or ``.zip`` file you wish to write to the SD card.
   - Select the SD card you wish to write your image to.
   - Review your selections and click 'Flash!' to begin writing data to the SD card.

**Connect peripheral devices**

Officially supported hardware is listed on `the POS Hardware page <https://www.odoo.com/page/point-of-sale-hardware>`_, but other hardware might work as well.

   - ``Printer:`` Connect an ESC/POS printer to a USB port and power it on.
   - ``Cash drawer:`` The cash drawer should be connected to the printer with an RJ25 cable.
   - ``Barcode scanner:`` Connect your barcode scanner. In order for your barcode scanner to be compatible it must behave as a keyboard and must be configured in US QWERTY. It also must end barcodes with an Enter character (keycode 28). This is most likely the default configuration of your barcode scanner.
   - ``Scale:`` Connect your scale and power it on.
   - ``Ethernet:`` If you do not wish to use Wi-Fi, plug in the Ethernet cable. Make sure this will connect the POSBox to the same network as your POS device.
   - ``Wi-Fi:`` If you do not wish to use Ethernet, plug in a Linux compatible USB Wi-Fi adapter. Most commercially available Wi-Fi adapters are Linux compatible. Officially supported are Wi-Fi adapters with a Ralink 5370 chipset. Make sure not to plug in an Ethernet cable, because all Wi-Fi functionality will be bypassed when a wired network connection is available.
   - ``Network Printer:`` Connect Network Printer.

**Power the POSBox**

Plug the power adapter into the POSBox, a bright red status led should light up.

**Make sure the POSBox is ready**

Once powered, The POSBox needs a while to boot. Once the POSBox is ready, it should print a status receipt with its IP address. Also the status LED, just next to the red power LED, should be permanently lit green.

More information read the:

   - https://www.raspberrypi.org/documentation/installation/installing-images/
   - https://www.odoo.com/documentation/user/9.0/point_of_sale/overview/setup.html
