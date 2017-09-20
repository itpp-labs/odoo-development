Reading logs on posbox
======================

Reading logs

.. code-block:: shell

   tail -f /var/log/odoo/odoo-server.log

`Edit <https://odoo-development.readthedocs.io/en/latest/admin/posbox/administrate-posbox.html#how-to-edit-config>`_  log level:

.. code-block:: shell

   nano /home/pi/odoo/addons/point_of_sale/tools/posbox/configuration/odoo.conf

replace to

.. code-block:: shell

   log_level = info
