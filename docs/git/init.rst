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

    * public email must be personal address …@it-projects.info
    * URL must be personal twitter account

  * https://github.com/settings/emails

    * primary email must be personal address …@it-projects.info
    * “Keep my email address private” must be switched off
  
  * https://github.com/orgs/it-projects-llc/people
  
    * get invitation
    * set ``Organization visibility`` to ``Public``

git email
=========

* `Configure email in git <https://help.github.com/articles/setting-your-email-in-git/>`_. Email must be the same as in github settings::

    git config --global user.email "your_email@example.com"

git editor
==========
::

    git config --global core.editor "nano"

gitignore
=========

* `Configure global gitignore <https://help.github.com/articles/ignoring-files/#create-a-global-gitignore>`_

    Possible content for ``~/.gitignore_global``: ::

    *~
    *.pyc   

