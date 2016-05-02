=============
 Longpolling
=============

`Longpolling <https://www.google.com/#q=longpolling>`_ is a way to deliver instant notification to web client (e.g. in chats).

To activate longpolling:

* install gevent ::

    python -c "import gevent" || sudo pip install gevent

* set non-zero value for :doc:`workers <workers>` parameter
* configure nginx ::

    location /longpolling {
        proxy_pass http://127.0.0.1:8072;
    }
    location / {
        proxy_pass http://127.0.0.1:8069;
    }

