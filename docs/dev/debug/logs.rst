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

Example is here:  :doc:`Failed modules <errors/failed-modules>`

Sources
-------
Allows you to check which client side files are loaded and which are not. To do this:

1. Turn on debug mode in the url.

2. Open Developer tools (F12), go to the Sources tab and reload page.

3. Open left panel (if it is not open yet) and search interested app.

Example:  :doc:`Missing dependencies error in console <errors/missing-dependencies>`


Network
-------

Sometime error are not printed neither in Terminal, nor in Console. Then you can try to find some logs at Network tab of browser's developer tool.
