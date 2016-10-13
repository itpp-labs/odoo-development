================================
 Fixing references on migration
================================


``9.0``- > ``10.0+``
====================

.. code-block:: sh

    # hr
    find . -type f -name '*.xml' | xargs sed -i 's/menu_hr_configuration/menu_human_resources_configuration/g'
    find . -type f -name '*.csv'  -o -name '*.py' -o -name '*.xml'  | xargs sed -i 's/base.group_hr/hr.group_hr/g'

