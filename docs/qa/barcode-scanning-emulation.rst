===================
 Emulation barcode
===================

Barcode scanner connected with computer work as keyboard. E.g. after scanning send sequence of symbols as if fast typing on the keyboard.

Install **xdotool** app if you haven't it yet.

.. code-block:: shell

    sudo apt-get install xdotool

Emulation scanning barcode:

.. code-block:: shell

    sleep 3 && echo '1234567890128' | grep -o . | xargs xdotool key && xargs xdotool key \n &

or so:

.. code-block:: shell

    sleep 3 && echo '3333333333338' | grep -o . | xargs xdotool key && xargs xdotool key \n &

Where: 3 - sleep seconds; 3333333333338 - barcode.

After successfully scanning you will see '3333333333338' in the command line. If toggle to other window that symbols appear in the input field in the this window. So we can send sequence in the app as if we scanning it.

