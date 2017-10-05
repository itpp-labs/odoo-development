Running PosBox on your computer for development purposes
========================================================

Running PosBox on your computer is means running the second odoo server instead PosBox.

For run the second odoo server it's necessary to change the configuration settings which is different from the running settings the first odoo server.

For this, just change the ``xmlrpc`` and ``longpolling`` port value.

For example, if the run settings for the first odoo server ``/path/to/openerp-server1.conf``::

   xmlrpc_port = 8069
   longpolling_port = 8072

then the settings for the second odoo server ``/path/to/openerp-server2.conf`` can be as follows::

   xmlrpc_port = 9069
   longpolling_port = 9072

Example of running **PosBox** on your computer with used ``Network Printer``:

* Run first Odoo Server, e.g.::

   ./openerp-server --config=/path/to/openerp-server1.conf

* Install the `Pos Printer Network <https://www.odoo.com/apps/modules/10.0/pos_printer_network/>`_ module on Odoo in a `usual <http://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html?highlight=install#from-app-store-install>`_ way.
* Configure PosBox using the `installation instructions <https://apps.odoo.com/apps/modules/10.0/pos_printer_network/>`_.
* Run second Odoo Server using new settings and add to ``--load parameters``, e.g.::

      ./openerp-server --load=web,hw_proxy,hw_posbox_homepage,hw_scale,hw_scanner,hw_escpos,hw_printer_network --config=/path/to/openerp-server2.conf

* Print in network printer.

Run PosBox via docker
---------------------
Example with `hw_printer_network <https://www.odoo.com/apps/modules/10.0/pos_printer_network/>`_ and `PosBox 8.0 <https://github.com/odoo/odoo/tree/8.0/addons/point_of_sale/tools/posbox>`_:

.. code-block:: sh

    docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo --name db-posbox-8.0 postgres:9.5

    docker run \
    -p 9069:8069 \
    -p 9072:8072 \
    -e ODOO_MASTER_PASS=admin \
    --privileged \
    -v /dev/bus/usb:/dev/bus/usb \
    --name 8.0-posbox \
    --link db-posbox-8.0:db \
    -t itprojectsllc/install-odoo:8.0-posbox --  --load=web,hw_proxy,hw_posbox_homepage,hw_scale,hw_scanner,hw_escpos,hw_printer_network

Source of this docker can be found here: https://github.com/it-projects-llc/install-odoo/tree/8.0/dockers/posbox

Nginx configurations
--------------------
For each docker runs on a different ports add the server block in the Nginx configuration file for example::

    server {
        listen 80;
        server_name $YOUR_SERVER_NAME;
        proxy_buffers 16 64k;
        proxy_buffer_size 128k;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        #proxy_redirect http:// https://;
        proxy_read_timeout 600s;
        client_max_body_size 100m;
        location /longpolling {
            proxy_pass http://127.0.0.1:$LONGPOLLING_PORT;
        }
        location / {
            proxy_pass http://127.0.0.1:$XMLRPC_PORT;
        }
    }

If you've got 'Access-Control-Allow-Origin' error, try to write next code below each line contains proxy_pass::

        add_header 'Access-Control-Allow-Origin' * always;
