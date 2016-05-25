===============================
 static/description/index.html
===============================

.. contents::
   :local:

Image sizes
===========

* :doc:`Image Sizes <./image-sizes>`

Templates
=========

Title
-----

.. code-block:: html

    <section class="oe_container">
        <div class="oe_row oe_spaced">
            <div class="oe_span12">
                <h2 class="oe_slogan">NAME</h2>
                <h3 class="oe_slogan">SUMMARY OR SLOGAN</h3>
            </div>
        </div>
    </section>

Text + Image
------------

.. code-block:: html

    <section class="oe_container">
        <div class="oe_row oe_spaced">
            <div class="oe_span6">
                <p class="oe_mt32">
                TEXT
                </p>
            </div>
            <div class="oe_span6">
                <div class="oe_row_img oe_centered">
                    <img class="oe_picture oe_screenshot" src="IMAGE.png"/>
                </div>
            </div>
        </div>
    </section>
    
Image + Text
------------

TODO

Text, Image
-----------

.. code-block:: html

    <section class="oe_container">
        <div class="oe_row oe_spaced">
            <div class="oe_span12">
                <p class="oe_mt32">
                TEXT
                </p>
            </div>
            <div class="oe_row_img oe_centered">
                 <img class="oe_picture oe_screenshot" src="IMAGE.png"/>
             </div>
        </div>
    </section>

Contact us
----------
* :doc:`Contact us block <./contactus>`

oe_dark
=======

Use ``oe_dark`` class on every even ``section``. Don't use ``oe_dark`` on the last section **Contact us**.

.. code-block:: html

    <section class="oe_container">
        <!--Title-->
    </section>

    <section class="oe_container oe_dark">
    </section>

    <section class="oe_container">
    </section>

    <section class="oe_container oe_dark">
    </section>

    <section class="oe_container">
    </section>

    <section class="oe_container">
        <!--Contact us block-->
    </section>


