============
 README.rst
============

.. contents::
   :local:

Guidlines
=========

.. code-block:: rst

    =============
     Module Name
    =============

    Description or Technical specifications

    Credits
    =======

    Contributors
    ============
    * DEVELOPER_NAME <PERSON@it-projects.info>

    Sponsors
    ========
    * `IT-Projects LLC <https://it-projects.info>`_

    Further information
    ===================

    HTML Description: https://apps.odoo.com/apps/modules/VERSION/TECHNICAL_NAME/

    Usage instructions: `<doc/index.rst>`_

    Changelog: `<doc/changelog.rst>`_

    Tested on Odoo 8.0 ODOO_COMMIT_SHA_TO_BE_UPDATED

Rendering
---------

    Be sure, that rendered README file looks as you expected.

Raw
^^^

.. image:: ../../images/raw-rst.png

Rendered
^^^^^^^^

.. image:: ../../images/rendered-rst.png

OCA's README
------------

* https://raw.githubusercontent.com/OCA/maintainer-tools/master/template/module/README.rst

HTML Description
================

Link to app store, e.g.

.. code-block:: rst

    HTML Description: https://apps.odoo.com/apps/modules/9.0/web_debranding/

Usage instructions
==================

* :doc:`doc/index.rst <usage-instructions>`

Changelog
=========

* :doc:`doc/changelog.rst <changelog.rst>`


Tested on
=========

.. code-block:: rst

    Tested on Odoo 8.0 a40d48378d22309e53e6d38000d543de1d2f7a78

commit sha can be found as following

.. code-block:: shell

    cd /path/to/odoo
    git rev-parse HEAD

