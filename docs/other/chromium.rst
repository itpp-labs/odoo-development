==================================
Adjust chromium window size script
==================================

You can make screenshot with size exactly you need.

Open chromium. Do not expand window (or in wount work). Run this command::

    wmctrl -a chromium -e 1,0,0,760,451

Last two arguments is width and height.
Consider to add chromium window borders to your screenshot size.
In my case it 10px to width and 80px to height. Likely you got same.
So for 750 x 371  it be 760 x 451.
