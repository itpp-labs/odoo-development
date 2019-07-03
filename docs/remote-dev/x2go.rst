=======================
 Deploying x2go server 
=======================

x2go allows you to run remotely browser (or any other application on x-server)


* Connect to your server using port forwarding (``-L`` option), e.g.

.. code-block:: sh

   ssh -L 2222:localhost:2222 user@server.example.com -p 22

* Start `x2go server <https://hub.docker.com/r/paimpozhil/docker-x2go-xubuntu/>`_ on 2222 port


.. code-block:: sh

 docker run --name x2go -p 2222:22 -t -d paimpozhil/docker-x2go-xubuntu || docker start x2go
 docker logs x2go 


* note the root/dockerx passwords

* port ``2222`` is available now on your localhost, connect to it using :doc:`x2go client <x2goclient>`
