=========================
 Squash commits into one
=========================

Backup
======

Before making a squash consider to "backup" your commits.

Local backup:

.. code-block:: sh

   git tag 9.0-new-module-backup

Remote backup

.. code-block:: sh

   git push origin 9.0-new-module:9.0-new-module-backup

git commit --amend
==================

Adds current commit to latest commit

git rebase -i
=============

Interactive squahing

.. code-block:: sh

    git rebase -i <your-first-commit>^
    # e.g.
    git rebase -i 7801c8b^

Then edit opened file and use ``pick`` for first commit and ``squash`` for the rest.
