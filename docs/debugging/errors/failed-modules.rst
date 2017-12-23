Error: Failed modules
=====================


If into server console no errors but boot.js raise exception that find out reason error next steps:

.. image:: ../../dev/img/screenshots/boot_js/error.png

1. Go to error line into boot.js.

2. Turn on breakpoint.

.. image:: ../../dev/img/screenshots/boot_js/breakpoint.png

3. Rerun script (click F5)

4. When script stop on error line move to console.

5. Type command::

    failed[0].error

6. To receive the output

.. image:: ../../dev/img/screenshots/boot_js/console.png

