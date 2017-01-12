===========================
 ESC/POS printer emulation
===========================


hw_escpos
---------

* apply `patch <https://raw.githubusercontent.com/it-projects-llc/odoo-development/master/docs/dev/debug/hw_escpos.patch>`__

* install hw_escpos on odoo

* run odoo with ``-d DB_WITH_HW_ESCPOS --db-filter=DB_WITH_HW_ESCPOS``

* in new terminal run

.. code-block:: shell

    tail -f /tmp/printer

On printing:

* some binary data is sent to /tmp/printer
* odoo prints logs with unparsed data

POS
---

* set ``Receipt printer`` checkbox in pos.config and set ip equal to ``127.0.0.1``

* open POS interface (at any database, including one on runbot)

* print ticket

