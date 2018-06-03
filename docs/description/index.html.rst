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

Warnings and notes
------------------

Green:

.. code-block:: html

    <section class="oe_container">
      <div class="oe_row oe_spaced">
        <div class="oe_span12">

        <div class="alert alert-success oe_mt32" style="padding:0.3em 0.6em; font-size: 150%;">
          YOUR TEXT HERE
        </div>

        </div>
      </div>
    </section>

Yellow:

.. code-block:: html

    <section class="oe_container">
      <div class="oe_row oe_spaced">
        <div class="oe_span12">

        <div class="alert alert-warning oe_mt32" style="padding:0.3em 0.6em; font-size: 150%;">
          YOUR TEXT HERE
        </div>

        </div>
      </div>
    </section>

Red:

.. code-block:: html

    <section class="oe_container">
      <div class="oe_row oe_spaced">
        <div class="oe_span12">

        <div class="alert alert-danger oe_mt32" style="padding:0.3em 0.6em; font-size: 150%;">
          YOUR TEXT HERE
        </div>

        </div>
      </div>
    </section>

Subsection
----------

.. code-block:: html

    <h4 class="oe_slogan"><b>SUBSECTION NAME</b></h4>

*(Put it inside <section class="..."><div class="oe_row oe_spaced"> tags)*

Reference to menu
-----------------

To specify references to menu, use right arrow character ``&rarr;``, for example:

.. code-block:: html

    Go to <em>Sales &rarr; Configuration &rarr; Settings</em>


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

.. code-block:: html

    <section class="oe_container oe_dark">
        <div class="oe_row oe_spaced">
	    <div class="oe_span6">
                <div class="oe_row_img oe_centered">
                    <img class="oe_demo oe_picture oe_screenshot" src="IMAGE.png"/>
                </div>
            </div>
            <div class="oe_span6">
                <p class="oe_mt32">
                TEXT
                </p>
            </div>
        </div>
    </section>

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

Text, Image (large size)
------------------------

.. code-block:: html

    <section class="oe_container oe_dark">
        <div class="oe_row oe_spaced">
            <div class="oe_span12 text-center">
                <p class="oe_mt32">
                  <font style="font-size: 120%;">TEXT</font>
                </p>
            </div>
            <div class="oe_screenshot" align="center">
                 <img style="max-width: 80%" src="IMAGE.png"/>
             </div>
         </div>
     </section>
    
Demo note
---------

.. code-block:: html

    <section class="oe_container">
        <div class="oe_row oe_spaced">
            <div class="oe_span8">
                <h2>Want to take a look?</h2>
                <p class="oe_mt32">For a live demostration click <em>LIVE PREVIEW</em> button above (near to <em><i class="fa fa-shopping-cart"></i> Add to Cart</em>) </p>
            </div>
        </div>
    </section>

Contact us
----------
* :doc:`Contact us block <./contactus>`

oe_dark
=======

Use ``oe_dark`` class on every even ``section``. Don't use ``oe_dark`` for beginning and ending sections.

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
        <!--Free support section-->
    </section>

    <section class="oe_container">
        <!--Contact us block-->
    </section>


