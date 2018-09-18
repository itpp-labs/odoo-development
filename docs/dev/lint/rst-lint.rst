==========================
 Fixing rst lints in odoo
==========================
::

    # Correction is links in rst-files
    #`_   ->   `__
    find . -type f -name '*.rst' | xargs sed -i '`_(?!_)/`__/g'
