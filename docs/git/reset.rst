Cancel lame commit
------------------

Imagine you make lame commit. Now to repair things do next:

1. git reset HEAD~1 --soft
2. git status

You will see:
Your branch is behind 'origin/8.0' by 1 commit, and can be fast-forwarded. (use "git pull" to update your local branch)

3. git add // Add here changed (fixed) files 
4. git diff --cached  //make sure everything is ok.
5. git status  

You will see:
Your branch is behind 'origin/8.0' by 1 commit, and can be fast-forwarded. (use "git pull" to update your local branch)

6. git commit -m'I fixed my mistakes'
7. git status

You will see:
Your branch and 'origin/8.0' have diverged,
and have 1 and 1 different commit each, respectively. (use "git pull" to merge the remote branch into yours)

Now finaly force is with you:

8. git push origin 8.0 -f
