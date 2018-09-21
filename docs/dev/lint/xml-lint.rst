==========================
 Fixing xml lints in odoo
==========================

::

    # xml-deprecated-tree-attribute
    find . -type f -name '*.xml' | xargs sed -i 's/\(\<tree.*\) string="[^"]*"/\1/g'
