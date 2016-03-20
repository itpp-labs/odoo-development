__openerp__.py
==============

.. contents::
   :local:

Guidlines
---------

Use example below as template. What are important here:

* order of attributes 
* quote characters (``"``, ``"""``)
* empty lines
* no description attribute
* price and currency attributes are commented-out if not used
* comma after last item in list (e.g. in 'depends' attribute)
* add new line symbol at the end of file (i.e. right after last ``}``)

.. code-block:: python

    # -*- coding: utf-8 -*-
    {
        "name": """Module name""",
        "summary": """Short description of the module""",
        "category": "Some Category",
        "images": []
        "version": "1.0.0",

        "author": "IT-Projects LLC, Devenloper Name",
        "website": "https://it-projects.info",
        "license": "GPL-3",
        #"price": 9.00,
        #"currency": "EUR",

        "depends": [
            "dependency1",
            "dependency2",
        ],
        "external_dependencies": {"python": [], "bin": []},
        "data": [
            "file1.xml",
            "file2.xml",
            "file3.yml",
        ],
        "demo": [
        ],
        "installable": True,
        "auto_install": False,
    }


.. image:: ../images/__openerp__.py-no-new-line-at-the-end-of-file.png

See also:

* OCA's template: https://github.com/OCA/maintainer-tools/blob/master/template/module/__openerp__.py

version
-------

*Note: whenever you change version, you have to add a record in* :doc:`changelog.rst <changelog.rst>`

The `x.y.z` version numbers follow the semantics `breaking.feature.fix`:

  * `x` increments when the data model or the views had significant
    changes. Data migration might be needed, or depending modules might
    be affected.
  * `y` increments when non-breaking new features are added. A module
    upgrade will probably be needed.
  * `z` increments when bugfixes were made. Usually a server restart
    is needed for the fixes to be made available.

On each version change a record in ``doc/changelog.rst`` should be added.

If a module ported to different odoo versions (e.g. 8 and 9) and some update is
added only to one version (e.g. 9), then version is changed as in example below:

* init

  * [8.0] 1.0.0
  * [9.0] 1.0.0
* feature added to 8.0 and ported to 9.0

  * [8.0] 1.1.0
  * [9.0] 1.1.0
* feature added to 9.0 only and not going to be ported to 8.0:

  * [8.0] 1.1.0
  * [9.0] 1.2.0
* fix made in 9.0 only and not going to be ported to 8.0:

  * [8.0] 1.1.0
  * [9.0] 1.2.1
* fix made in 8.0 and ported to 9.0

  * [8.0] 1.2.2
  * [9.0] 1.2.2

i.e. two module branches cannot have same versions with a different meaning

author
------

Use company first and then developer(s): ::

        "author": "IT-Projects LLC, Devenloper Name",

For OCA's repositories put company name first, then OCA. Developers are listed in README file: ::

    "author": "IT-Projects LLC, Odoo Community Association (OCA)",


license
-------

IT-Projects LLC uses following licences:

* ``"GPL-3"`` for odoo 8.0 and below
* ``"LGPL-3"`` for odoo 9.0 and above

For OCA's repositories use ``"AGPL-3"``.

external_dependencies
---------------------

Check if some python library exists::

  "external_dependencies": {"python" : ["openid"]}


Check if some sytem application exists::

  "external_dependencies": {"bin" : ["libreoffice"]}


