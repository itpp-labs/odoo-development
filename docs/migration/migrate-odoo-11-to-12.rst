=======================
 ``11.0-`` → ``12.0+``
=======================

New API
=======

.. code-block:: sh

    # renames in base modules
    find . -type f -name '*.py' | xargs sed -i 's/from odoo.addons.base.res/from odoo.addons.base.models/g'
    find . -type f -name '*.py' | xargs sed -i 's/from odoo.addons.base.ir/from odoo.addons.base.models/g'
    # renames in tours  
    # https://github.com/odoo/odoo/commit/21c4480821e669ef22e090334d5afdacfc1043c9
    # https://github.com/odoo/odoo/commit/38c7ed3c73eb5efc370c6ac0050e38ca8810e59e
    find . -type f -name '*.js' | xargs sed -i 's/STEPS.TOGGLE_APPSWITCHER/STEPS.TOGGLE_HOME_MENU/g'
    find . -type f -name '*.js' | xargs sed -i 's/STEPS.MENU_MORE/STEPS.SHOW_APPS_MENU_ITEM/g'
