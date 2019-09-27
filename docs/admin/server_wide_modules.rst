============
 ``--load``
============

The option ``--load`` (also known as ``server_wide_modules``) is used to define list of modules that are loaded on odoo start. Such modules are loaded even if there are no databases in odoo. Odoo by default loads ``web`` module, but exact list may varies for different odoo versions

Default value
=============

* `Odoo 12 <https://github.com/odoo/odoo/blob/95b4f2ab4b5698ab3a28c9c35ac8da6fb6def983/odoo/tools/config.py#L120>`__: ``base,web``
* `Odoo 11 <https://github.com/odoo/odoo/blob/717f4583949219c346c87c390fbc336b4f31571c/odoo/tools/config.py#L119>`__: ``web``
* `Odoo 10 <https://github.com/odoo/odoo/blob/80d363cd31ec56b72e38e02571285349b60e428e/odoo/tools/config.py#L114>`__: ``web,web_kanban``
* `Odoo 9 <https://github.com/odoo/odoo/blob/752dcc761caf15cb532b1e787e9a378a8112a6a4/openerp/tools/config.py#L114>`__: ``web,web_kanban``
* `Odoo 8 <https://github.com/odoo/odoo/blob/492d8ce4d024e11c9aa715d4a4b7f99493eaef4b/openerp/tools/config.py#L145>`__: ``web,web_kanban``
* `Odoo 7 <https://github.com/odoo/odoo/blob/ae34a1e93ec3e6e54ece9d546d527af5787f5c3f/openerp/tools/config.py#L487>`__: ``web,web_kanban``

Adding new module to the list
=============================

In general, you need to take default value and add there a new module.

Via CLI
-------

.. code-block:: sh

    # Example for Odoo 12.0:
    ./odoo-bin --workers=2 --load base,web,NEWMODULE --config=/path/to/odoo.conf


Via config file
---------------
Parameter name is config file is ``server_wide_modules``. Add this parameter if it's not presented yet or modify existing value by adding new module::

    [options]
    # example for Odoo 12.0:
    server_wide_modules=base,web,NEWMODULE
    # ...

Odoo.sh 
-------

* navigate to Shell tab in odoo.sh 
* execute ``nano .config/odoo/odoo.conf`` 
* add ``server_wide_modules`` parameter with NEWMODULE added (see above)
* restart server by executing following command: ``odoosh-restart``
