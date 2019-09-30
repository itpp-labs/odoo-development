==================================
 __manifest__.py (__openerp__.py)
==================================

OCA's manifest
==============

https://github.com/OCA/maintainer-tools/blob/master/template/module/__openerp__.py

name
====

It must be non-technical name of the module

summary
=======

Short description of the module. E.g. you can describe here which problem is solved by the module. It could sound as a slogan.

category
========

Categories from the list below are preferred.

   * ``Accounting``
   * ``Discuss``
   * ``Document Management``
   * ``eCommerce``
   * ``Human Resources``
   * ``Industries``
   * ``Localization``
   * ``Manufacturing``
   * ``Marketing``
   * ``Point of Sale``
   * ``Productivity``
   * ``Project``
   * ``Purchases``
   * ``Sales``
   * ``Warehouse``
   * ``Website``
   * ``Extra Tools``

Hidden
------

For technical modules ``Hidden`` category can be used::

    "category": "Hidden",

Such modules are excluded from search results on app store.

version
=======

version in IT-Projects
----------------------
https://gitlab.com/itpp/handbook/blob/master/technical-docs/__manifest__.md#version

version in OCA
--------------
https://github.com/OCA/odoo-community.org/blob/master/website/Contribution/CONTRIBUTING.rst#version-numbers

author
======

Use company first and then developer(s): ::

        "author": "IT-Projects LLC, Developer Name",

In the main, if module already exists and you make small updates\fixes, you should not add your name to authors.

author in OCA
-------------

https://github.com/OCA/odoo-community.org/blob/master/website/Contribution/CONTRIBUTING.rst#backporting-odoo-modules

website
=======

Url to personal page at company's website (e.g. ``"https://it-projects.info/team/yelizariev"``)

license
=======

IT-Projects LLC uses following licences:

* ``"GPL-3"`` for odoo 8.0 and below
* ``"LGPL-3"`` for odoo 9.0 and above

For OCA's repositories use ``"AGPL-3"``.

external_dependencies
=====================

Check if some python library exists::

  "external_dependencies": {"python" : ["openid"]}


Check if some sytem application exists::

  "external_dependencies": {"bin" : ["libreoffice"]}


See also: :doc:`External dependencies in odoo<../py/external-imports>`


IT-Projects' Template
=====================
* https://gitlab.com/itpp/handbook/blob/master/technical-docs/__manifest__.md