==========================
 Common Migration Helpers
==========================

.. contents::
   :local:

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

Updating odoo versions in docs
==============================

    # TODO

Reviewing odoo updates
======================

Code below helps you to find what is new between odoo branches

.. code-block:: sh

    cd path/to/odoo/

    # check name for remote corresponding to https://github.com/odoo/odoo.git
    git remote -v

    # change directory to the module you need. To check core updates use "cd odoo/"
    cd addons/mail/

    git log \
        --date=relative \
        --pretty=format:"%h%x09%Cblue%ad%Creset%x09%ae%x09%Cgreen%s%Creset" \
        --invert-grep \
        --grep='\[FIX\]' \
        --grep='\[MERGE\]' \
        --grep='\[DOC\]' \
        --grep='\[CLA\]' \
        --grep='\[I18N\]' \
        origin/10.0..origin/11.0 -- . # use corresponding remote name and version

Reviewing module source
=======================

Commands below may help you to estimate amount of work to migrate module. The commands simply show all source in one view

.. code-block:: sh

  # view source
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" -or -iname "*.rst" -or -iname "*.md" | xargs tail -n +1 | less

  # view source without docs
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" | xargs tail -n +1 | less
  
