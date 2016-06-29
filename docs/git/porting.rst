=========
 Porting
=========

If you add some feature to one branch and need to add it to anoher branch, then you have to make *port*.

See also:

* :doc:`Conflicts resolving <conflicts>`

Forward-port
============

It's the simplest case. You merge commits from older branch (e.g. 8.0) to newer branch (e.g. 9.0) ::

    git checkout 9.0
    git merge origin/8.0

    # [Resolve conflicts if needed]

    git push

After ``git merge`` you probably need to make some minor changes. In that case just add new commits to newer branch ::

    git add ...
    git commit -m "...."
    git push

Back-port
=========


If you need to port new feature from newer branch (e.g. 9.0) to older one (e.g. 8.0), then you have to make *back-port*.

The problem here is that newer branch has commits which should be applied for newer branch only. That is you cannot just make ``git merge 9.0``, because it brings 9.0-only commits to 8.0 branch. Possible solutions here are:

git cherry-pick
===============


Apply commits from newer branch (e.g. 9.0) to older branch (e.g. 8.0) ::

    git checkout 8.0
    
    git cherry-pick <commit-1>
    # [Resolve conflicts if needed]
    
    git cherry-pick <commit-2>
    # [Resolve conflicts if needed]
    # ...
    
    git push

Also possible to pick the commit from any remote repository. Add this repository to your remotes. Do fetch from it. And then cherry-pick.

cherry-pick range of commits
----------------------------

The command ``git cherry-pick A..B`` applies commits betwwen A and B, but without A (A must be older than B). To apply inclusive range of commits use format as follows::

   git cherry-pick A^..B

For example, to backport this PR https://github.com/it-projects-llc/odoo-saas-tools/pull/286/commits , use command::

   git cherry-pick 6ee4fa07d4c0adc837d7061e09da14638d8abf8d^..9133939a25f9e163f52e6662045fc2dc6010ac14
