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
    
    Put some short introduction first.

    Then add more detailed description, technical specifications, any other information that could be interested for other developers. Don't forget that Usage instructions is a separated and has to be located in doc/index.rst file.

    Credits
    =======

    Contributors
    ------------
    * DEVELOPER_NAME <PERSON@it-projects.info>

    Sponsors
    --------
    * `IT-Projects LLC <https://it-projects.info>`_

    Further information
    ===================

    Demo: http://runbot.it-projects.info/demo/REPO-NAME/BRANCH

    HTML Description: https://apps.odoo.com/apps/modules/VERSION/TECHNICAL_NAME/

    Usage instructions: `<doc/index.rst>`_

    Changelog: `<doc/changelog.rst>`_

    Tested on Odoo 8.0 ODOO_COMMIT_SHA_TO_BE_UPDATED

OCA's README
------------

* https://raw.githubusercontent.com/OCA/maintainer-tools/master/template/module/README.rst

Demo
====

Link to the runbot. Supported repo names are below. Change branche name if needed.

.. code-block:: rst

    Demo: http://runbot.it-projects.info/demo/access-addons/9.0
    Demo: http://runbot.it-projects.info/demo/addons-dev/addons-yelizariev-9.0-some_feature
    Demo: http://runbot.it-projects.info/demo/l10n-addons/9.0
    Demo: http://runbot.it-projects.info/demo/mail-addons/9.0
    Demo: http://runbot.it-projects.info/demo/misc-addons/9.0
    Demo: http://runbot.it-projects.info/demo/odoo-saas-tools/9.0
    Demo: http://runbot.it-projects.info/demo/odoo-telegram/9.0
    Demo: http://runbot.it-projects.info/demo/pos-addons/9.0
    Demo: http://runbot.it-projects.info/demo/rental-addons/9.0
    Demo: http://runbot.it-projects.info/demo/website-addons/9.0



HTML Description
================

Link to app store, e.g.

.. code-block:: rst

    HTML Description: https://apps.odoo.com/apps/modules/9.0/web_debranding/

You have to prepare this link even if the module is not published yet, i.e. link returns 404 error.

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

