====================================
 Initial git & github configuration
====================================

ssh keys
========
Configure github ssh keys: https://help.github.com/articles/generating-ssh-keys/

github emails
=============

*IT-Projects LLC employees only:*

  * https://github.com/settings/profile

    * public email should be personal address …@it-projects.info
  * https://github.com/settings/emails

    * primary email should be personal address …@it-projects.info
    * “Keep my email address private” should be turned off

git email
=========

* `Configure email in git <https://help.github.com/articles/setting-your-email-in-git/>`_. Email must be the same as in github settings::

    git config --global user.email "your_email@example.com"

gitignore
=========

* `Configure global gitignore <https://help.github.com/articles/ignoring-files/#create-a-global-gitignore>`_

    Possible content for ``~/.gitignore_global``: ::

    *~
    *.pyc   

