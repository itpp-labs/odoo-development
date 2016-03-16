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

Notes
~~~~~

* When you resolving conflicts some times may be situations in which left code brokes right code after joining. You got to manipulate *lines* to make it right order. Do not edit code here. If you want to edit code, do it after you finish with cherry-pick.