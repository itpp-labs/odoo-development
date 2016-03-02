Logs
====

There are several places where you can get logs.

It's better to activate developer (debug) mode in browser when you are looging for logs.

.. contents::
   :local:

Error Message
-------------

It's a first place where you can see error message. But in most time, it doesn't contain enough information to resolve problem. Check other possbile ways to get log messages below.

Terminal
--------

It's a place where you run odoo.

Any errors related to python can be found here

Console
-------

It's a short term for browser's console. Click F12 in browser to open console.

It can contain error and warning about client part.

boot.js
^^^^^^^

If into server console no errors but boot.js raise exception that find out reason error next steps:

.. image:: ../img/screenshots/boot_js/error.png

1. Go to error line into boot.js.

2. Turn on breakpoint.

.. image:: ../img/screenshots/boot_js/breakpoint.png

3. Rerun script.

4. When script stop on error line move to console.

5. Typing command: failed[0].error

6. To receive the output

.. image:: ../img/screenshots/boot_js/console.png


Network
-------

Sometime error are not printed neither in Terminal, nor in Console. Then you can try to find some logs at Network tab of browser's developer tool.
