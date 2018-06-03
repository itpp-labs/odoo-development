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
     
     # install gpg2 if needed
     sudo apt-get install gnupg2

     # restart gpg-agent
     gpgconf --kill gpg-agent
     gpg-agent --daemon

* Make a backup if needed 

  .. code-block:: sh

     # make backup file and move it to secret place
     gpg --export-secret-keys > secret-backup.gpg
     
     # you will be able to restore keys by following command:
     gpg --import secret-backup.gpg
     # or
     gpg2 --import secret-backup.gpg

.. warning:: If you lost your key or forgot password, you need to create new
             one, but don't remove old one from github, because otherwise all signed
             by old key commits will be "Unverified"


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

