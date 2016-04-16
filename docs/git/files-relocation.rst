Files relocation
================

This article based on http://gbayer.com/development/moving-files-from-one-git-repository-to-another-preserving-history/

Goal:
 - Move directory 1 from Git repository A to Git repository B.
Constraints:
 - Git repository A contains other directories that we don’t want to move.
 - We’d like to perserve the Git commit history for the directory we are moving.

::

 $ cd ~
 $ git clone https://github.com/yelizariev/addons-yelizariev.git
 $ cd addons-yelizariev

We have the group_menu_no_access module that we are about to move from addons-yelizariev
to the access-addons repo.

::

 addons-yelizariev$ git remote rm origin
 addons-yelizariev$ git filter-branch --subdirectory-filter group_menu_no_access -- --all
 addons-yelizariev$ mkdir group_menu_no_access
 addons-yelizariev$ mv * group_menu_no_access/
 addons-yelizariev$ git add .
 addons-yelizariev$ git commit -m '[MOV] group_menu_no_access: ready to move'

 $ cd ../access-addons-8/
 access-addons-8$ git remote add repo-addons-yelizariev-branch ../addons-yelizariev
 access-addons-8$ git pull repo-addons-yelizariev-branch 8.0
 access-addons-8$ git push origin 8.0

Create pull request from your origin to upstream on github in your fork
of https://github.com/yelizariev/access-addons.git.
There must be the [MOV] commits along with the group_menu_no_access module ralated commits
that was created earlier in the addons-yelizariev repo.

After some time of typing the same commands to move several modules, I
decided to make simple bash bash script. Here it is

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
But then I type only one command instead of ten in case of fully manual approach.

::

    addons-yelizarie$ ../movemodule.sh group_menu_no_access ../access-addons 8.0

I assume here that the addons-yelizariev directory would be placed in your home
directory along with the access-addons directory. Be  sure that you are on the 8.0 branches
in both of your addons-yelizariev and access-addons.










