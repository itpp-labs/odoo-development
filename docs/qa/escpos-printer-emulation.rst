===========================
 ESC/POS printer emulation
===========================


hw_escpos
---------

* apply patch

  .. code-block:: sh

      cd /path/to/odoo/

      # odoo 10
      curl https://raw.githubusercontent.com/it-projects-llc/odoo-development/master/docs/debugging/hw_escpos-patch/hw_escpos-10.patch > hw_escpos.patch

      # odoo 9
      curl https://raw.githubusercontent.com/it-projects-llc/odoo-development/master/docs/debugging/hw_escpos-patch/hw_escpos-9.patch > hw_escpos.patch

      git apply hw_escpos.patch


* install hw_escpos on odoo

* run a separate odoo with following args::

  -d DB_WITH_HW_ESCPOS --db-filter=DB_WITH_HW_ESCPOS --xmlrpc-port=8888 --workers=0

* in new terminal run

.. code-block:: shell

    tail -f /tmp/printer

On printing:

* some binary data is sent to /tmp/printer
* odoo prints logs with unparsed data

POS
---
At any database (including one on runbot as well as database where you have installed hw_escpos):

* set ``Receipt printer`` checkbox in pos.config and set ip equal to ``127.0.0.1:8888``

* open POS interface

  .. warning:: for some reason printer emulation doesn't work in debug mode

* print ticket

