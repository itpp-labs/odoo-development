Conflict resolving
==================

After making ``git merge`` or ``git cherry-pick`` there could be conflicts, because some commits try to make changes on the same line. So, you need to choose which change shall be use. It could be one variant, both variants or new variant.

What to do if you got conflicts:

* Check status ::

    git status

* Resolve conflicts:

  * either edit files manually:
  
    * open file with conflicts
    * search for ``<<<`` or ``>>>`` and delete obsolete variant or make a mix of both variants.

  * or use following commands, if you are sure which version should be kept ::

        git checkout --ours -- <file>
        # or
        git checkout --theirs -- <file>

* Mark files as resolved via ``git add`` command
* Done. ::

    git push

Deleted files
~~~~~~~~~~~~~
Sometimes, changes can be conflicted because files are not exist anymore in *ours* version, but updated in *theirs* (or vice versa). In that case execute the code below in order to ignore such changes:

.. code:: bash

    git status | grep 'deleted by us' | awk '{print $4}' | xargs git rm
    git status | grep 'deleted by them' | awk '{print $4}' | xargs git rm


Notes
~~~~~

* It's important, that on resolving conflict stage you should not make any updates inside conflicting lines. You can only choose which lines should be kept and which deleted. E.g. if you resolve conflicts due to porting some update\feature from one odoo version (e.g. 8.0) to another (e.g. 9.0), then such changes some time must be tuned to make update\feature work on target odoo version. But you have to make such tuning on a new commit only. Make merging\chery-picking commits be only about merging and chery-picking, make porting commits separately.
* If you don't have conflicts, you do not need to make commit after cherry-pick because it creates commit by its own.

