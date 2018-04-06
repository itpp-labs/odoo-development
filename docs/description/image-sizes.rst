=============
 Image sizes
=============

See also

* :doc:`Preview module on App Store <./app-store-preview>`

* :doc:`Adjust chromium window size script <../other/chromium>`

.. contents::
   :local:
   :depth: 1

__openerp__.py -> 'images'
==========================

This images is displayed on application page (`example <https://www.odoo.com/apps/modules/8.0/res_partner_mails_count/>`__) and in application list (`example <https://www.odoo.com/apps/modules/browse?author=IT-Projects%20LLC>`__ )

Displayed size:

* app page::

    750 x 400

* app list::

    262,5 x 130

Recommended size (aspect) to fit both usage::

    750 x 371

You can scale picture, saving proportion.

.. note:: Appearance in *app list* is more important, as there is less chance that user open *app page*, if small sized image in *app list* is not attractive enough.

description/index.html
======================

All values assumed, that you put the code inside ``.oe_container`` and ``.oe_row``, e.g.::

    <section class="oe_container">
        <div class="oe_row oe_spaced">
            ...
            <div class="oe_demo oe_picture oe_screenshot">
                <img class="img img-responsive" src="1.png"/>
            </div>
            ...
        </div>
    </section>

oe_span6 img.oe_demo.oe_picture.oe_screenshot
---------------------------------------------
::
    max-width: 362px;
    max-height: 382px;

img.oe_demo.oe_picture.oe_screenshot
------------------------------------
::
    max-width: 761px;
    max-height: 382px;

img.oe_demo.oe_screenshot
-------------------------
::
    max-width: 928px;

img.oe_screenshot
-----------------
::
    max-width: 1500px;
    max-height: 1000px;

