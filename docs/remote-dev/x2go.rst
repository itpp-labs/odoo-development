=========================
 Remote desktop via X2GO
=========================

Deploying X2GO server
=====================

x2go allows you to run remotely browser (or any other application on x-server)


* Connect to your server:
* `install x2go server <https://wiki.x2go.org/doku.php/doc:installation:x2goserver>`_ :


.. code-block:: sh

 sudo add-apt-repository ppa:x2go/stable
 sudo apt-get update
 sudo apt-get install x2goserver x2goserver-xsession


* install desktop environment you prefer, e.g. LXDE:

.. code-block:: sh

 sudo apt-get install lubuntu-desktop
 # choose lightdm

* Install browser `Pale Moon <http://linux.palemoon.org>`_

.. code-block:: sh

 # http://linux.palemoon.org
 sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/stevenpusser/xUbuntu_16.04/ /' > /etc/apt/sources.list.d/home:stevenpusser.list"
 sudo apt-get update
 sudo apt-get install palemoon -y

X2GO Client
===========

* :doc:`Run or start x2go server container <x2go>`
* install ``x2goclient``

  Ubuntu:

  .. code-block:: sh

      sudo add-apt-repository ppa:x2go/stable
      sudo apt-get update
      sudo apt-get install x2goclient

  References:

  * https://www.howtoforge.com/tutorial/x2go-server-ubuntu-14-04/
  * http://wiki.x2go.org/doku.php/doc:installation:x2goclient

* Run client:

.. code-block:: sh

   x2goclient


* create a new session with the settings below and connect to it (we assume that you have user named "noroot" with ssh keys configured):

::

 Host : YOUHOST
 Port : 22
 Session type: LXDE
 [x] Try auto Login
 Input / Output: Use Whole Display
 Username: noroot


* Once you connected, fix a `firefox bug <https://bugzilla.mozilla.org/show_bug.cgi?id=1283089>`_:

  * run firefox
  * open new page and type ``about:config``
  * *Accept the risk*
  * find config ``gfx.xrender.enabled`` and set value to ``True``
  * restart firefox
