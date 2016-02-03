Resolving conflicts
=================

Manual resolving
----------------

Steps.

* Make merge with upstream or other branch you need
* Check status ::

    git status

* open file with conflicts
* search for ``<<<`` or ``>>>`` and delete obsolete variant
* mark files as resolved via ``git add`` command

If you are sure which version should be keeped use following commands ::

    git checkout --ours -- <file>
    # or
    git checkout --theirs -- <file>

Merge strategy
-------------

git-merge has an option to apply stategy that doesn't lead to conflicts, but absolutely ignore updates from one or another branch.

You need to be very carefull about changing default merge strategy.
::
    git merge -s ours ... 
    # or
    git merge -s theirs ... 


