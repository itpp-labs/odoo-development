=============
 Image sizes
=============

.. contents::
   :local:
   :depth: 1

__openerp__.py -> 'images'
==========================

This images is displayed on application page (`example <https://www.odoo.com/apps/modules/8.0/res_partner_mails_count/>`_) and in application list (`example <https://www.odoo.com/apps/modules/browse?author=IT-Projects%20LLC>`_ )

Displayed size:

* app page::

  750 x 400

* app list::

  262,5 x 130

Recommended size (aspect) to fit both usage::

    750 x 371

You can scale picture, saving proportion.

.. note:: Appearance in *app list* is more important, as there is less chance that user open *app page*, if small sized image in *app list* is not attractive enough.

See also

* :doc:`Preview module on App Store <./app-store-preview>`

Adjust chromium window size script
----------------------------------

You can make screenshot with size exactly you need.

Open chromium. Do not expand window (or in wount work). Run this command::

    wmctrl -a chromium -e 1,0,0,760,480

Last two arguments is width and height.
Consider to add chromium window borders to your screenshot size.
In my case it 10px to width and 80px to height. Likely you got same.
So for 750 x 400  it be 760 x 480.
