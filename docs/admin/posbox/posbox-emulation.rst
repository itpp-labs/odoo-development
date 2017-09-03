Running PosBox on your computer for development purposes
========================================================

Running PosBox on your computer is means running the second odoo server instead PosBox.

For run the second odoo server it's necessary to change the configuration settings which is different from the running settings the first odoo server.

For this, just change the ``xmlrpc`` and ``longpolling`` port value.

For example, if the run settings for the first odoo server ``/path/to/openerp-server1.conf``::

   xmlrpc_port = 8069
   longpolling_port = 8072

then the settings for the second odoo server ``/path/to/openerp-server2.conf`` can be as follows::

   xmlrpc_port = 8071
   longpolling_port = 8073

Example of running **PosBox** on your computer with used ``Network Printer``:

   * Run first Odoo Server, e.g.::

      ./openerp-server --config=/path/to/openerp-server1.conf

   * Install the `Pos Printer Network <https://www.odoo.com/apps/modules/10.0/pos_printer_network/>`_ module on Odoo in a `usual <http://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html?highlight=install#from-app-store-install>`_ way.
   * Configure PosBox using the `installation instructions <https://apps.odoo.com/apps/modules/10.0/pos_printer_network/>`_.
   * Run second Odoo Server using new settings and add to ``--load parameters``, e.g.::

         ./openerp-server --load=web,hw_proxy,hw_posbox_homepage,hw_posbox_upgrade,hw_scale,hw_scanner,hw_escpos,hw_printer_network --config=/path/to/openerp-server2.conf

   * Print in network printer.
