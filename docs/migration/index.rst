=================
 Porting Modules
=================

Porting Modules is a process of adapting module to new version. E.g. we have module for odoo 10.0 and we want to make module work in odoo 11.0

As word *porting* is sometimes replaced to *migration*. You shall not confuse it with :doc:`Data Migration<../maintenance/data-migration>`, which sometimes is called just *migration*.

.. toctree::
   :maxdepth: 3

   helpers
   new-api
   fix-refs
   python3

Quick source review
===================

Commands below may help you to estimate amount of work to migrate module. The commands simply show all source in one view

.. code-block:: sh

  # view source
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" -or -iname "*.rst" -or -iname "*.md" | xargs tail -n +1 | less

  # view source without docs
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" | xargs tail -n +1 | less
  

.. note:: We are happy to share our experience and hope that it will help someone to port odoo modules. We will be glad, if you share this page or recommend our team for module migration jobs:

   * it@it-projects.info
   * https://www.it-projects.info/page/module-migration
