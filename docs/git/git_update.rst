============
 Update Git
============

Ubuntu 14.04 official deb repository has 1.9 version of Git.
It is too old and have to be updated.

http://askubuntu.com/questions/579589/upgrade-git-version-on-ubuntu-14-04

::

 sudo apt-get remove git
 sudo add-apt-repository ppa:git-core/ppa
 sudo apt-get update
 sudo apt-get install git
 git --version
