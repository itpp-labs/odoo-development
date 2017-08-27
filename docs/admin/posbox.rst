==============
 local PosBox
==============

Local run of PosBox is means running the second odoo instead PosBox.

For run the second odoo it is necessary to change the configuration settings which is different from the running settings the first odoo.

For this, just change the xmlrpc and longpolling port value.

For example, if the run settings for the first odoo:
``xmlrpc_port = 8069``,
``longpolling_port = 8072``

then the settings for the second odoo can be as follows: 
``xmlrpc_port = 8071``,
``longpolling_port = 8073``.

Example of run local PosBox with used Network Printer:

1. Run First Odoo.

2. Install the `Pos Printer Network <https://www.odoo.com/apps/modules/10.0/pos_printer_network/>`_ module on Odoo in a `usual <http://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html?highlight=install#from-app-store-install>`_ way.

3. Configure PosBox using the `installation instructions <https://apps.odoo.com/apps/modules/10.0/pos_printer_network/>`_. 

4. Run second Odoo using new setting and load=web,hw_proxy,hw_posbox_homepage,hw_posbox_upgrade,hw_scale,hw_scanner,hw_escpos,hw_printer_network.

5. Print in network printer.

============================
 Installing image to PosBox
============================

Download last version posbox_image:

   https://nightly.odoo.com/master/posbox/

Install OPERATING SYSTEM IMAGES in your SD card using instruction:

   https://www.raspberrypi.org/documentation/installation/installing-images/


**Connect peripheral devices**

Officially supported hardware is listed on the POS Hardware page, but other hardware might work as well.

``Printer:`` Connect an ESC/POS printer to a USB port and power it on.

``Cash drawer:`` The cash drawer should be connected to the printer with an RJ25 cable.

``Barcode scanner:`` Connect your barcode scanner. In order for your barcode scanner to be compatible it must behave as a keyboard and must be configured in US QWERTY. It also must end barcodes with an Enter character (keycode 28). This is most likely the default configuration of your barcode scanner.

``Scale:`` Connect your scale and power it on.

``Ethernet:`` If you do not wish to use Wi-Fi, plug in the Ethernet cable. Make sure this will connect the POSBox to the same network as your POS device.

``Wi-Fi:`` If you do not wish to use Ethernet, plug in a Linux compatible USB Wi-Fi adapter. Most commercially available Wi-Fi adapters are Linux compatible. Officially supported are Wi-Fi adapters with a Ralink 5370 chipset. Make sure not to plug in an Ethernet cable, because all Wi-Fi functionality will be bypassed when a wired network connection is available.

``Network Printer:`` Connect Network Printer.

**Power the POSBox**

Plug the power adapter into the POSBox, a bright red status led should light up.

Make sure the POSBox is ready.

Once powered, The POSBox needs a while to boot. Once the POSBox is ready, it should print a status receipt with its IP address or you can specify the device IP address using the list of connected devices on your network. Also the status LED, just next to the red power LED, should be permanently lit green. 

More information read the 

   https://www.odoo.com/documentation/user/10.0/point_of_sale/overview/setup.html

==============================
 Settings for Network Printer
==============================

If you have the POSBox's IP address and an SSH client you can access the POSBox's system remotely. 

**Login:** ``pi``

**Password:** ``raspberry``

Beware that root (/) is mounted read only and so you cannot use write.

If you want to use it you need to reboot in normal mode.

.. code-block:: shell

   sudo su 
   mount -o rw,remount /
   mount -o rw,remount /root_bypass_ramdisks

edit /root_bypass_ramdisks//etc/init.d/odoo

.. code-block:: shell

   nano /root_bypass_ramdisks/etc/init.d/odoo 

add ``hw_printer_network`` to ``--load parameter``

Then

.. code-block:: shell

   cd /home/pi
   git clone https://github.com/it-projects-llc/pos-addons.git
   cp -rp /home/pi/pos-addons/hw_printer_network /home/pi/odoo/addons
   rm -rf /home/pi/pos-addons

Comment code:

.. code-block:: shell

   cd /home/pi/odoo/addons/hw_escpos/controllets/

edit ``main.py``

.. code-block:: shell

   nano main.py


and replace ``driver.push_task('printstatus')`` with ``# driver.push_task('printstatus')``

sync and reboot posbox

.. code-block:: shell

   sync
   reboot


