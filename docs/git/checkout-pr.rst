===========================================
 Create branch from another's Pull Request
===========================================

.. code-block:: sh

    git fetch upstream pull/354/head:pr354
    git checkout -b 10.0-branch-name pr354

More information: https://help.github.com/articles/checking-out-pull-requests-locally/

Push updates to another's Pull Request
======================================

If you have access to edit PR files via github UI, you can push such updates from console

.. code-block:: sh

    GITHUB_USERNAME=yelizariev  # set username where PR is made from
    REPO=pos-addons # set repo name
    BRANCH=10.0-fix-something # set source branch name
    
    git remote add ${GITHUB_USERNAME} git@github.com:${GITHUB_USERNAME}/${REPO}.git
    git fetch ${GITHUB_USERNAME} ${BRANCH}
    git checkout ${GITHUB_USERNAME}/${BRANCH}
    # make updates
    # ...
    # make commit
    git commit ...
    
    # push update to another's branch
    git push ${GITHUB_USERNAME} HEAD:${BRANCH}
