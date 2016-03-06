Multi Pull Request
==================

Find last merged point
----------------------

To find last commit ``origin/8.0`` and ``origin/9.0`` were merged, use following commands

.. code-block:: shell

    git fetch
    git log origin/8.0..origin/9.0 --grep="Merge remote-tracking branch 'origin/8.0'" --merges -n 3

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
    #  origin/9.0
    #  origin/9.0-dev

    # if there is not origin/9.0 in output,
    # then commit have not been merge yet and you cannot use it


