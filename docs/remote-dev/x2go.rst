=======================
 Deploying x2go server 
=======================

x2go allows you to run remotely browser (or any other application on x-server)

* Start x2go server on 2222 port

source: https://hub.docker.com/r/paimpozhil/docker-x2go-xubuntu/

.. code-block:: sh

 docker run --name x2go -p 2222:22 -t -d paimpozhil/docker-x2go-xubuntu
 docker logs x2go


* note the root/dockerx passwords

* Connect to your server using port forwarding (``-L`` option), e.g.
.. code-block:: sh

 ssh -L 2222:localhost:2222 user@server.example.com

* port ``2222`` is available now on your localhost, connect to it using :doc:`x2go client <x2goclient>`
