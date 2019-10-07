==========================
 Common Migration Helpers
==========================

.. contents::
   :local:

Creating Pull Requests in batch
===============================

See https://odoo-devops.readthedocs.io/en/latest/git/github.html

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
    git commit -m ":sos::one::three: mark unported modules as non-installable"
    # (make "git push" and pull request at github)

Updating odoo versions in docs
==============================

.. code-block:: sh

    # bump versions in docs (excluding "Tested on Odoo" expression)
    find . -type f -name *.rst -or -name *.html | xargs sed -i '/Tested on Odoo/!s/12.0/13.0/g'

Reviewing odoo updates
======================

Code below helps you to find what is new between odoo branches

.. code-block:: sh

    cd path/to/odoo/

    # check name for remote corresponding to https://github.com/odoo/odoo.git
    git remote -v

    # update to specific file or folder if needed
    PATHTOCHECK=. 

    git log \
        --date=relative \
        --pretty=format:"%h%x09%Cblue%ad%Creset%x09%ae%x09%Cgreen%s%Creset" \
        --invert-grep \
        --grep='\[FIX\]' \
        --grep='\[MERGE\]' \
        --grep='\[DOC\]' \
        --grep='\[CLA\]' \
        --grep='\[I18N\]' \
        origin/10.0..origin/11.0 -- $PATHTOCHECK # use corresponding remote name, version and path to folder or file

    # to get diff of such commits (e.g. to find in which commit something is added or removed), execute following:
    git log \
        --format=format:%H \
        --invert-grep \
        --grep='\[FIX\]' \
        --grep='\[MERGE\]' \
        --grep='\[DOC\]' \
        --grep='\[CLA\]' \
        --grep='\[I18N\]' \
        origin/10.0..origin/11.0 -- $PATHTOCHECK | xargs -I{} git --no-pager show {} -- $PATHTOCHECK | less
    
Reviewing module source
=======================

Commands below may help you to estimate amount of work to migrate module. The commands simply show all source in one view

.. code-block:: sh

  # view source
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" -or -iname "*.rst" -or -iname "*.md" | xargs tail -n +1 | less

  # view source without docs
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" | xargs tail -n +1 | less
  
