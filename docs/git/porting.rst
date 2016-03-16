Porting
=======

If you add some feature to one branch and need to add it to anoher branch, then you have to make *port*.

See also:

* :doc:`Conflicts resolving <conflicts>`

Forward-port
------------

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
---------

If you need to port new feature from newer branch (e.g. 9.0) to older one (e.g. 8.0), then you have to make *back-port*.

The problem here is that newer branch has commits which should be applied for newer branch only. That is you cannot just make ``git merge 9.0``, because it brings 9.0-only commits to 8.0 branch. Possible solutions here are:

git cherry-pick
^^^^^^^^^^^^^^^

Apply commits from newer branch (e.g. 9.0) to older branch (e.g. 8.0) ::

  git checkout 8.0

  git cherry-pick <commit-1>
  # [Resolve conflicts if needed]

  git cherry-pick <commit-2>
  # [Resolve conflicts if needed]
  # ...

  git push

Also possible to pick the commit from any remote repository. Add this repository to your remotes. Do fetch from it. And then cherry-pick.

If after cherry-picking you have some conflicts then resolve it and do ::

  cherry-pick --continue

**Important things:** 
 * When you resolving conflicts some times may be situations in which left code brokes right code after joining. You got to manipulate *lines* to make it right order. Do not edit code here. If you want to edit code, do it after you finish with cherry-pick. 
 * You do not need to commit cherry-pick because it creates commit by its own.

Then make forward-port ::
  
  git fetch
  git checkout 9.0
  git merge origin/8.0



