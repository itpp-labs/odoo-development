============================================
 Deploying x2go server inside LXD Container
============================================

* Start x2go server inside user's LXD container on 2222 port

source: https://hub.docker.com/r/paimpozhil/docker-x2go-xubuntu/

.. code-block:: sh

 CID=$(docker run -p 2222:22 -t -d paimpozhil/docker-x2go-xubuntu)
 docker logs $CID


* note the root/dockerx passwords

* Connect to your dev environment

.. code-block:: sh

 ssh -L 2222:localhost:2222 ildar@iledarn.dev.it-projects.info -p 10101

* port ``2222`` is available now on your localhost, connect to it using :doc:`x2go client <x2goclient>`
