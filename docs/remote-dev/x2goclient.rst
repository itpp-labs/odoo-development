=============
 X2GO Client
=============

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

  
* create a new session with the settings below and connect to it

::

 Host : localhost
 Port : 2222
 Session type: xfce
 [x] Try auto Login
 Input / Output: Use Whole Display
 Username : dockerx
 Password : (get it from the Docker logs when starting the server container)
