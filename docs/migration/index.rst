==================
 Module Migration
==================

.. toctree::
   :maxdepth: 3

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
