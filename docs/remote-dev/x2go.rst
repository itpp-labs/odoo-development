=======================
 Deploying x2go server 
=======================

x2go allows you to run remotely browser (or any other application on x-server)


* Connect to your server using port forwarding (``-L`` option), e.g.

.. code-block:: sh

   ssh -L 2222:localhost:2222 user@server.example.com -p 22

* Start `x2go server <https://hub.docker.com/r/paimpozhil/docker-x2go-xubuntu/>`_ on 2222 port


.. code-block:: sh

 docker run --privileged --name x2go -p 2222:22 -t -d paimpozhil/docker-x2go-xubuntu || docker start x2go
 docker logs x2go 


* note the root/dockerx passwords

* Optionaly. Add ssh keys to authorize without password:

.. code-block:: sh

 PUB_KEY=$(curl --silent https://github.com/YOUR_GITHUB_ACCOUNT.keys)  # Be sure that you have added ssh keys on github
 docker exec -i -u dockerx -t x2go bash -c "mkdir ~/.ssh && echo '$PUB_KEY' >> ~/.ssh/authorized_keys"


* port ``2222`` is available now on your localhost, connect to it using :doc:`x2go client <x2goclient>`
