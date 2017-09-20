Introduction
============

The **POSBox** runs a heavily modified **Raspbian Linux** installation, a Debian derivative for the **Raspberry Pi**.
It also runs a barebones installation of Odoo which provides the webserver and the drivers.
The hardware drivers are implemented as Odoo modules. Those modules are all prefixed with ``hw_*`` and they are the only
modules that are running on the POSBox. Odoo is only used for the framework it provides. No business data is processed
or stored on the POSBox. The Odoo instance is a shallow git clone of the ``8.0`` branch.

The root partition on the POSBox is mounted ``read-only``, ensuring that we don't wear out the SD card by writing to it too
much. It also ensures that the filesystem cannot be corrupted by cutting the power to the POSBox. Linux applications expect
to be able to write to certain directories though. So we provide a ramdisk for ``/etc`` and ``/var`` (Raspbian automatically provides
one for ``/tmp``). These ramdisks are setup by ``setup_ramdisks.sh``, which we run before all other init scripts by running
it in ``/etc/init.d/rcS``. The ramdisks are named ``/etc_ram`` and ``/var_ram`` respectively. Most data from
``/etc`` and ``/var`` is copied to these tmpfs ramdisks. In order to restrict the size of the ramdisks, we do not copy
over certain things to them (eg. apt related data). We then bind mount them over the original directories. So when an
application writes to ``/etc/foo/bar`` it's actually writing to ``/etc_ram/foo/bar``. We also bind mount ``/`` to ``/root_bypass_ramdisks``
to be able to get to the real ``/etc`` and ``/var`` during development.

How to edit config
==================

If you have the POSBox's IP address and an SSH client you can access the POSBox's system remotely.

**Login:** ``pi``
**Password:** ``raspberry``

Beware that root (/) is mounted read only and so you cannot use write.

If you want to use it you need to reboot in normal mode.

.. code-block:: shell

   sudo su
   mount -o rw,remount /
   mount -o rw,remount /root_bypass_ramdisks

sync and reboot posbox

.. code-block:: shell

   sync
   reboot

How to update odoo command-line options
=======================================

edit /root_bypass_ramdisks/etc/init.d/odoo

.. code-block:: shell

   nano /root_bypass_ramdisks/etc/init.d/odoo

add ``hw_printer_network`` to ``--load parameter``

.. code-block:: shell

   $LOGFILE --load=web,hw_proxy,hw_posbox_homepage,hw_posbox_upgrade,hw_scale,hw_scanner,hw_escpos,hw_blackbox_be,hw_screen,hw_printer_network

How to edit odoo source
=======================

Comment out line 354 in ``hw_escpos/controllers/main.py``

.. code-block:: shell

   nano /home/pi/odoo/addons/hw_escpos/controllets/main.py

i.e. replace ``driver.push_task('printstatus')`` with

.. code-block:: shell

   # driver.push_task('printstatus')

sync and reboot posbox

.. code-block:: shell

   sync
   reboot
