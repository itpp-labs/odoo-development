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

Then edit opened file and use ``reword`` for first commit and ``squash`` for the rest. E.g.

Origin::

    TODO

Edited::

    TODO

Push
====

.. code-block:: sh

    git push -f origin 9.0-new-module
