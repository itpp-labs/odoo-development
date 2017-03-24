============
 README.rst
============

.. contents::
   :local:

Guidlines
=========

.. code-block:: rst

    ===============
     {Module Name}
    ===============
    
    {Put some short introduction first.}

    {Then add more detailed description, technical specifications, any other information that could be interested for other developers. Don't forget that Usage instructions is a separated and has to be located in doc/index.rst file.}

    Credits
    =======

    Contributors
    ------------
    * {DEVELOPER_NAME} <{PERSON}@it-projects.info>

    Sponsors
    --------
    * `IT-Projects LLC <https://it-projects.info>`__
    
    Maintainers
    -----------
    * `IT-Projects LLC <https://it-projects.info>`__

    Further information
    ===================

    Demo: http://runbot.it-projects.info/demo/{REPO-NAME}/{BRANCH}

    HTML Description: https://apps.odoo.com/apps/modules/{VERSION}/{TECHNICAL_NAME}/

    Usage instructions: `<doc/index.rst>`_

    Changelog: `<doc/changelog.rst>`_

    Tested on Odoo 10.0 {ODOO_COMMIT_SHA_TO_BE_UPDATED}

OCA's README
------------

* https://raw.githubusercontent.com/OCA/maintainer-tools/master/template/module/README.rst

Demo
====

Link to the runbot. Supported repo names are below. Change branche name if needed.

.. code-block:: rst

    Demo: http://runbot.it-projects.info/demo/access-addons/10.0
    Demo: http://runbot.it-projects.info/demo/addons-dev/misc-addons-10.0-some_feature
    Demo: http://runbot.it-projects.info/demo/l10n-addons/10.0
    Demo: http://runbot.it-projects.info/demo/mail-addons/10.0
    Demo: http://runbot.it-projects.info/demo/misc-addons/10.0
    Demo: http://runbot.it-projects.info/demo/odoo-saas-tools/10.0
    Demo: http://runbot.it-projects.info/demo/odoo-telegram/10.0
    Demo: http://runbot.it-projects.info/demo/pos-addons/10.0
    Demo: http://runbot.it-projects.info/demo/rental-addons/10.0
    Demo: http://runbot.it-projects.info/demo/website-addons/10.0

addons-dev
----------
In most cases, if you work in addons-dev, you shall not use demo link to addons-dev (e.g. ``http://runbot.it-projects.info/demo/addons-dev/misc-addons-10.0-some_feature``). Use a link for target repo instead (e.g. ``http://runbot.it-projects.info/demo/misc-addons/10.0``). 
You can use links to addons-dev only if you know who will use it. 



HTML Description
================

Link to app store, e.g.

.. code-block:: rst

    HTML Description: https://apps.odoo.com/apps/modules/10.0/web_debranding/

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

    Tested on Odoo 10.0 03bc8c5f9ac53a3349c1caac222f7619a632ccd8

commit sha can be found as following

.. code-block:: shell

    cd /path/to/odoo
    git rev-parse HEAD

