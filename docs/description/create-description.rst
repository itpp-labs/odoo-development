Module description
=============================

Banner
------

The Banner is displayed only in Odoo Apps. It should be located in the ``path_to_module/images/`` directory and its size should not exceed 1500x1000 px.
Next, in the ``__openerp__.py`` file you need make the relevant record:

.. code-block:: shell

   "images": ["images/banner.png"],

Icon and index.html
-----------------------------
The module icon needs to be located at ``path_to_module/static/description/`` and it must be called ``icon.png``. Also in this directory you need to create ``index.html``, where will be contained necessary HTML tags, text description and screenshots (the recommended size is 752x352 px).

.. seealso::

   See the official template https://github.com/odoo/odoo/blob/master/addons/crm/static/description/index.html

It is important that ``index.html`` and screenshots it contains should be included at the same folder.

The result of the ``index.html`` and icon appearance can be checked by opening the module in "Local Modules" of your Odoo instance.

Summary
-----------------------------
This is an overview of content that provides a reader with the overaching theme, but does not expand on specific details.

Summary should be included at ``__openerp__.py`` as ``'summary': """Summary text"""``. 
For example:

.. code-block:: shell

   'summary': """Use multiple POS for handling orders"""

