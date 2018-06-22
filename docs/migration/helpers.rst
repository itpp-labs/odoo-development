==========================
 Common Migration Helpers
==========================

Switching off unported modules
==============================

.. code-block:: sh

    # (create fresh branch from upstream)

    # mark all modules as non-installable
    find . -type f -name __openerp__.py  -or -name __manifest__.py | xargs sed -i 's/"installable": True/"installable": False/'
    find . -type f -name __openerp__.py  -or -name __manifest__.py | xargs sed -i "s/'installable': True/'installable': False/"

    # check for fiels without "installable" tag in manfiest
    find . -type f -name __openerp__.py  -or -name __manifest__.py | xargs grep -L "installable.: "
    # (if there is any output -- edit those files manually)

    # prepare a commit
    git add .
    # check commit diff
    git diff --cached
    # Emoji prefixed with odoo version
    git commit -m ":one::two::sos: mark unported modules as non-installable"
    # (make "git push" and pull request at github)

