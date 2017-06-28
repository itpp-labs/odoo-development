====================================
 Initial git & github configuration
====================================

ssh keys
========
Configure github ssh keys: https://help.github.com/articles/connecting-to-github-with-ssh/

gpg keys
========

* Generate gpg keys: https://help.github.com/articles/generating-a-new-gpg-key/
* Add gpg key to github: https://help.github.com/articles/adding-a-new-gpg-key-to-your-github-account/
* Tell to git which key to use https://help.github.com/articles/telling-git-about-your-gpg-key/
* Tell git to sign all commits:

  .. code-block:: sh

     git config --global commit.gpgsign true

* Make gpg remember your passphrase

  .. code-block:: sh

     # Update gpg-agent config 
     # 28800 is 8 hours
     echo "default-cache-ttl 28800" >> ~/.gnupg/gpg-agent.conf
     echo "max-cache-ttl 28800" >> ~/.gnupg/gpg-agent.conf

     # tell git to use gpg-agent
     git config --global gpg.program gpg2

     # restart gpg-agent
     gpgconf --kill gpg-agent
     gpg-agent --daemon


github profile
==============

*IT-Projects LLC employees only:*

* https://github.com/settings/profile

  * public email must be personal address …@it-projects.info
  * URL must be personal twitter account

    * you can use your account to tweet about development, work, traveling, vacation, fun
    * twitter profile's website URL has to be https://www.it-projects.info/
    * no requirements for profile description, header photo
    * profile photo should be a real face photo
    * location has to be specifed ``YouCity, Country``
  
  * Company must be set to ``@it-projects-llc``
  * Location must be your ``YouCity, Country``
  * Photo must be your real face photo

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

