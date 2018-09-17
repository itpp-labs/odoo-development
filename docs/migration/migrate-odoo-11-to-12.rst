=======================
 ``11.0-`` → ``12.0+``
=======================

New API
=======

.. code-block:: sh

    # renames in base modules
    find . -type f -name '*.py' | xargs sed -i 's/from odoo.addons.base.res/from odoo.addons.base.models/g'
    find . -type f -name '*.py' | xargs sed -i 's/from odoo.addons.base.ir/from odoo.addons.base.models/g'
