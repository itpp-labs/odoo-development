Files relocation
================

This article based on http://gbayer.com/development/moving-files-from-one-git-repository-to-another-preserving-history/

Goal:
 - Move directory 1 from Git repository A to Git repository B.
Constraints:
 - Git repository A contains other directories that we don’t want to move.
 - We’d like to perserve the Git commit history for the directory we are moving.
Let's start
 - $REPO: the repository hosting the module (e.g. ``misc-addons``)
 - $DEST_REPO: the repository you want to move the module to (e.g. ``access-addons``)
 - $MODULE: the name of the module you want to move (e.g. ``group_menu_no_access``)
 - $BRANCH: the branch of the $REPO with $MODULE (source branch, e.g. ``8.0``)

.. warning:: If you have installed git from official ubuntu 14.04 deb repository then you should first update it. You can update git using this instruction :doc:`Update git<git_update>`

::

 $ cd ~
 $ git clone https://github.com/it-projects-llc/$REPO -b $BRANCH
 $ cd $REPO
 $ git remote rm origin
 $ git filter-branch --subdirectory-filter $MODULE -- --all
 $ mkdir $MODULE
 $ mv * $MODULE # never mind the "mv: cannot move..." warning message
 $ git add .
 $ git commit -m "[MOV] $MODULE: ready"
 $ cd ~
 $ cd $DEST_REPO
 $ git remote add $MODULE-hosting-remote ~/$REPO
 $ git pull $MODULE-hosting-remote $BRANCH

After the last command you will have the module with all its commits in your destination repo.
Now you can push it on github etc. You can remove ``~/$REPO`` folder - no use of it now.

.. warning:: Cloning - this is required step. It is temporary directory. It will removed all modules except the one that you want to move.

The following script may come in handy if you need to move several modules. But be sure that you understand all its commands before using.

::

 #!/bin/bash

 source_repo=$PWD
 echo $source_repo

 if [ -n "$1" ]
 then
  	module=$1
  	echo $module
 else
  	echo "Must be module name"
  	exit $E_WRONGARGS
 fi


 if [ -n "$2" ]
 then
  	dest_repo=$2
  	echo $dest_repo
 else
  	echo "Must be dest_repo"
  	exit $E_WRONGARGS
 fi

 if [ -n "$3" ]
 then
  	branch=$3
  	echo $branch
 else
  	echo "Must be branch specified"
  	exit $E_WRONGARGS
 fi

 cp -r $source_repo ../$module
 cd ../$module
 git remote rm origin
 git filter-branch --subdirectory-filter $module -- --all
 mkdir $module
 mv * $module
 git add .
 git commit -m "[MOV] module -- $module"
 cd $dest_repo
 git remote add repo_moved_module $source_repo/../$module
 git pull repo_moved_module $branch --no-edit
 git remote rm repo_moved_module
 rm -rf $source_repo/../$module

In order to use it you should  make the movemodule.sh file in your home directory
and put all lines above there and make this file executable.
::

$ cd ~
$ chmod +x movemodule.sh

To do the moving of group_menu_no_access from addons-yelizariev to access-addons
with the movemodule.sh take the following steps.

::

 $ cd ~
 $ git clone https://github.com/yelizariev/addons-yelizariev.git
 $ cd addons-yelizariev

This part is the same as moving without the script.
But then I type only one command instead of many in case of fully manual approach.

::

    addons-yelizarie$ ~/movemodule.sh group_menu_no_access ~/access-addons 8.0








