Multi Pull Request
==================

Find last merged point
----------------------

To find last commit ``upstream/8.0`` and ``upstream/9.0`` were merged, use following commands

.. code-block:: shell

    git fetch
    git log upstream/8.0..upstream/9.0 --grep="Merge remote-tracking branch 'origin/8.0'" --merges -n 3

    # you will get something like that:
    # commit 5cb3652be72a05330c3988d270f3aef548511b29
    # Merge: f1cd564 6cc2562
    # Author: Ivan Yelizariev <yelizariev@it-projects.info>
    # Date:   Sat Feb 27 16:00:42 2016 +0500
    # 
    #     Merge remote-tracking branch 'origin/8.0' into 9.0-dev
    # 
    # commit 14632a790aa01ee2a1ee9fe52152cf2fbfa86423
    # Merge: 7a48b3a d66ba4f
    # Author: Ivan Yelizariev <yelizariev@it-projects.info>
    # Date:   Thu Feb 25 11:31:43 2016 +0500
    # 
    #     Merge remote-tracking branch 'origin/8.0' into 9.0-dev
    # 
    # commit 6981c245afdccc39b2b49585f8205a784161f9c6
    # Merge: 22081ed 6eb9f8d
    # Author: Ivan Yelizariev <yelizariev@it-projects.info>
    # Date:   Fri Feb 19 19:14:15 2016 +0500
    #
    #    Merge remote-tracking branch 'origin/8.0' into 9.0-dev


    # take one commit sha from the list and check that it's in origin/9.0.

    git branch -r --contains 5cb3652be72a05330c3988d270f3aef548511b29

    # possible output:
    #  upstream/9.0
    #  origin/9.0-dev

    # if there is not upstream/9.0 in output,
    # then commit has not been merged yet and you cannot use it
    # for branch 9.0 use this commit sha 5cb3652be72a05330c3988d270f3aef548511b29
    # for branch 8.0 need find which of two commits in ``Merge:`` line contains "upstream/8.0"

    git branch -r --contains f1cd564
    git branch -r --contains 6cc2562

    # Use commit sha to create new branches:
    
    git checkout -b '9.0-new_branch_name' 5cb3652be72a05330c3988d270f3aef548511b29
    git checkout -b '8.0-new_branch_name' 6cc2562
