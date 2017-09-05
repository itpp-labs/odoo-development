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
                <h2 class="oe_slogan" style="color:#875A7B;">NAME</h2>
                <h3 class="oe_slogan">SUMMARY OR SLOGAN</h3>
            </div>
        </div>
    </section>

Key features
------------
.. code-block:: html

    <section class="oe_container">
      <div class="oe_row oe_spaced">
        <div class="oe_span12">

        <div class="alert alert-info oe_mt32" style="padding:0.3em 0.6em; font-size: 150%;">
          <i class="fa fa-hand-o-right"></i><b> Key features: </b>
          <ul class="list-unstyled">

            <li>
            <i class="fa fa-check-square-o text-primary"></i>
              FEATURE 1 
            </li>

            <li>
            <i class="fa fa-check-square-o text-primary"></i>
              FEATURE 2 
            </li>

          </ul>
        </div>

        </div>
      </div>
    </section>

Subsection
----------

.. code-block:: html

    <h4 class="oe_slogan">SUBSECTION NAME</h4>

*(Put it inside <section class="..."><div class="oe_row oe_spaced"> tags)*

Text + Image
------------

.. code-block:: html

    <section class="oe_container oe_dark">
        <div class="oe_row oe_spaced">
            <div class="oe_span6">
                <p class="oe_mt32">
                TEXT
                </p>
            </div>
            <div class="oe_span6">
                <div class="oe_row_img oe_centered">
                    <img class="oe_demo oe_picture oe_screenshot" src="IMAGE.png"/>
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

    <section class="oe_container oe_dark">
        <div class="oe_row oe_spaced">
            <div class="oe_span12 text-center">
                <p class="oe_mt32">
                TEXT
                </p>
            </div>
            <div class="oe_row_img oe_centered">
                 <img class="oe_demo oe_picture oe_screenshot" src="IMAGE.png"/>
             </div>
        </div>
    </section>

Free Support
------------
.. code-block:: html

    <section class="oe_container">
      <div class="oe_row oe_spaced">
        <h2 class="oe_slogan" style="color:#875A7B;">Free Support</h2>
        <h3 class="oe_slogan">You will get free support in case of any issues</h3>
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
    
    <section class="oe_container">
        <!--Key features-->
    </section>

    <section class="oe_container">
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


