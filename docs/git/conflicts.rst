Resolving conflicts
===================

Manual resolving
----------------

Steps.

* Make merge with upstream or other branch you need
* Check status ::

    git status

* Resolve conflicts:

  * either edit files manually:
  
    * open file with conflicts
    * search for ``<<<`` or ``>>>`` and delete obsolete variant

  * or use following commands, if you are sure which version should be keeped ::

        git checkout --ours -- <file>
        # or
        git checkout --theirs -- <file>

* mark files as resolved via ``git add`` command

Merge strategy
--------------

git-merge has an option to apply stategy that doesn't lead to conflicts, but absolutely ignore updates from one or another branch.

You need to be very carefull about changing default merge strategy. ::

    git merge -s ours ... 
    # or
    git merge -s theirs ... 


