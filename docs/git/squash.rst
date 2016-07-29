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

To restore original state you can use following command:

.. code-block:: sh

    # be sure that you on the branch you are going to change
    git status

    # restore from tag
    git rebase 9.0-new-module-backup -X theirs

    # restore from remote branchtag
    git rebase origin/9.0-new-module-backup -X theirs

``git commit --amend``
======================

Instead of creating new commit, adds updates to the latest commit.

``git rebase -i``
=================

Interactive squashing

.. code-block:: sh

    git rebase -i <your-first-commit>^
    # e.g.
    git rebase -i 7801c8b^

Then edit opened file and keep ``pick`` for the first commit and and replace ``pick`` with ``squash`` for the rest ones. E.g.

Origin::

    TODO

Edited::

    TODO

.. warning:: If you remove a line here THAT COMMIT WILL BE LOST.

Push
====

.. code-block:: sh

    git push -f origin 9.0-new-module
