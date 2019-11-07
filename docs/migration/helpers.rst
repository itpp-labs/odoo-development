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

Updating odoo version in files
==============================

Once per repository:

.. code-block:: sh

    # update CI stuff
    sed -i '/Build Status/s/12.0/13.0/g' README.md
    sed -i '/VERSION=/s/12.0/13.0/' .travis.yml
    git commit README.md .travis.yml -m ":shield::one::three: bump versions"

General helpers (could be executed in new branch as well as on porting modules):

.. code-block:: sh

    # bump versions in urls in docs (excluding "Tested on Odoo 12.0 SHA" expression)
    find . -type f -name *.rst -or -name index.html -or -name *.md | xargs sed -i '/\(Tested on \| 12.0\)/!s/12.0/13.0/g'
    # update "tested on Odoo 12.0 community / enterprise" -- IT-Projects specific
    find . -type f -name index.html | xargs sed -i 's;<br/>12.0;<br/>13.0;g'
    git commit *.rst *.html *.md -m ":book::one::three: bump versions in docs"

Only on porting modules:

.. code-block:: sh

    # update version in manifest
    find . -type f -name __manifest__.py | xargs sed -i 's;12.0;13.0;g'

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
        --grep='\[MERGE\]' \
        --grep='\[DOC\]' \
        --grep='\[CLA\]' \
        --grep='\[I18N\]' \
        origin/12.0..origin/13.0 -- $PATHTOCHECK # use corresponding remote name, version and path to folder or file

    # to get diff of such commits (e.g. to find in which commit something is added or removed), execute following:
    git log \
        --format=format:%H \
        --invert-grep \
        --grep='\[MERGE\]' \
        --grep='\[DOC\]' \
        --grep='\[CLA\]' \
        --grep='\[I18N\]' \
        origin/12.0..origin/13.0 -- $PATHTOCHECK | xargs -I{} git --no-pager show {} -- $PATHTOCHECK | less
    
Reviewing module source
=======================

Commands below may help you to estimate amount of work to migrate module. The commands simply show all source in one view

.. code-block:: sh

  # view source
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" -or -iname "*.rst" -or -iname "*.md" | xargs tail -n +1 | less

  # view source without docs
  find . -iname "*.py" -or -iname "*.xml" -or -iname "*.csv" -or -iname "*.yml" -or -iname "*.js" | xargs tail -n +1 | less
  
Other tools
===========

* all-in-one tool: https://github.com/grap/odoo-migrate
* OCA autopep: https://github.com/OCA/maintainer-tools#auto-fix-pep8-guidelines
* `bowler <https://pybowler.io>`__ based fixers: https://gist.github.com/blaggacao/13cf79fad489bca962e4a43eb580e9ee
