PyCharm
=======

Remote access with pgAdmin to Odoo postgre database on Ubuntu
-------------------------------------------------------------
**This is for PgAdmin integration, but same method working with PyCharm.**


STEP #1 – get pgAdmin
Install pgAdmin from pgadmin.org

STEP #2 – allow postgre server remote connections from everywhere
Open etc/postgresql/9.x/main/pg_hba.conf and add following line:
host    all             all             all                     md5

STEP #3 – let the postgre server listen to everyone
Open etc/postgresql/9.x/main/postgresql.conf and change following line:
listen_addresses = ‘*’

STEP #4 – give the user “postgres” a password
Start the psql terminal: sudo -u postgres psql
Give a password: ALTER USER postgres PASSWORD ‘yourpassword’;
Leave the psql terminal: \q

STEP #5
Restart postgre server by executing this terminal command:
sudo /etc/init.d/postgresql restart

STEP #6
Start pgAdmin and add a connection to a server like this:

.. image:: /images/new_server_connection_with_pgadmin.png

You are ready!

Original:

http://odoo.guide/remote-access-with-pgadmin-to-odoo-postgre-database-on-ubuntu/
