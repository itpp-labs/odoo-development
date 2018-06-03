===========
 post_load
===========


.. contents::
   :local:

What do we know from comments in odoo source?
=============================================

.. code-block:: py

    # Call the module's post-load hook. This can done before any model or
    # data has been initialized. This is ok as the post-load hook is for
    # server-wide (instead of registry-specific) functionalities.

What is it actually for?
========================

For **Monkey patches**

.. image:: ../../images/monkey-patch.jpg

Example of monkey patch in odoo
===============================

.. code-block:: py

    from odoo import tools

    def new_image_resize_images(...)
        ...

    tools.image_resize_images = new_image_resize_images

Why shall we use ``post_load`` to apply monkey patch?
=====================================================

.. note:: Since `odoo 12 <https://github.com/odoo/odoo/commit/8226aa1db828d2a559c7ffaa31a27ef3e5ba4d0b>`_ monkey patch could be applied without post_load, but it's still recommended to use it to be sure.

Because otherwise monkey patch will be applied every time it is available in addons path.
It happens because odoo loads python files of a module if there is a static
folder in the module (no matter if the module is installed or not -- see
``load_addons`` method in `http.py <https://github.com/odoo/odoo/blob/10.0/odoo/http.py>`_ file of odoo source).

How to use post_load?
=====================

You need to define a function available in ``__init__.py`` file of the module. Then set that function name as value of ``"post_load"`` attribute in module manifest.

Example?
========

Sure. E.g. from  `telegram module <https://github.com/it-projects-llc/odoo-telegram>`_.

In *__openerp__.py*

.. code-block:: py

        ...
        "post_load": "telegram_worker",
        "pre_init_hook": None,
        "post_init_hook": None,
        "installable": True,
        "auto_install": False,
        "application": True,
    }

In *__init__.py*

.. code-block:: py

    from odoo.service.server import PreforkServer

    ...

    def telegram_worker():
        # monkey patch
        old_process_spawn = PreforkServer.process_spawn

        def process_spawn(self):
            old_process_spawn(self)
            while len(self.workers_telegram) < self.telegram_population:
                # only 1 telegram process we create.
                self.worker_spawn(WorkerTelegram, self.workers_telegram)

        PreforkServer.process_spawn = process_spawn
        old_init = PreforkServer.__init__

        def __init__(self, app):
            old_init(self, app)
            self.workers_telegram = {}
            self.telegram_population = 1
        PreforkServer.__init__ = __init__

Something else we need to know?
===============================

Yes.

Additionally, if you need to apply monkey patch before any other initialisation, the module has to be added to :doc:`server_wide_modules<../../admin/server_wide_modules>` parameter.

Other usage of post_load?
=========================

In case of extending pos-box modules (e.g. ``hw_escpos``), you probably need to use post_load, because importing hw_escpos from your module runs posbox specific initialisation. 

Example from hw_printer_network module:

In *__manifest__.py*

.. code-block:: py

        ...
        "post_load": "post_load",
        "pre_init_hook": None,
        "post_init_hook": None,
        "installable": True,
        "auto_install": False,
        "application": True,
    }

In *__init__.py*

.. code-block:: py

    def post_load():
        from . import controllers

In *controllers/hw_printer_network_controller.py*

.. code-block:: py

    # first reason of using post_load
    from odoo.addons.hw_escpos.escpos import escpos
    import odoo.addons.hw_escpos.controllers.main as hw_escpos_main
    
    ...

    # second reason - monkey patch:
    driver = UpdatedEscposDriver()
    hw_escpos_main.driver = driver
