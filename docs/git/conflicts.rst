Conflict resolving
==================

After making ``git merge`` there could be conflicts, because some commits try to make changes on the same line. So, you need to choose which change shall be use. It could be one variant, both variants or new variant.

What to do if you got conflicts:

* Check status ::

    git status

* Resolve conflicts:

  * either edit files manually:
  
    * open file with conflicts
    * search for ``<<<`` or ``>>>`` and delete obsolete variant

  * or use following commands, if you are sure which version should be kept ::

        git checkout --ours -- <file>
        # or
        git checkout --theirs -- <file>

* Mark files as resolved via ``git add`` command
* Done. ::

    git push
