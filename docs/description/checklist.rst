============================
 Module releasing checklist
============================

This articles cover documentation and description part only.

Module Name
===========

* Module Name MUST be non-technical.

  Examples of technical names:

  * web_debranding
  * Web Debranding

  Example of non-technical names:

  * Backend Debranding

* Module Name MUST be the same at :doc:`manifest file<../dev/docs/__manifest__.py>`, :doc:`README.rst<../dev/docs/README.rst>`, :doc:`doc/index.rst<../dev/docs/usage-instructions>`


Summary
=======

* Review ``"summary"`` attribute at  :doc:`manifest file<../dev/docs/__manifest__.py>` and first paragraph at :doc:`README.rst<../dev/docs/README.rst>`. They MUST be presented, but MAY be different.


Price
=====

* Review ``"price"`` attribute at  :doc:`manifest file<../dev/docs/__manifest__.py>`

Category
========

* Review ``"category"`` attribute at  :doc:`manifest file<../dev/docs/__manifest__.py>`

doc/index.rst
=============

* Review :doc:`content<../dev/docs/doc-files-understanding>` and :doc:`formatting<../dev/docs/rst-requirements>` of :doc:`doc/index.rst file<../dev/docs/usage-instructions>`

README.rst
==========

* Review :doc:`content<../dev/docs/doc-files-understanding>` and :doc:`formatting<../dev/docs/rst-requirements>` of :doc:`README.rst file<../dev/docs/usage-instructions>`

static/description/index.html
=============================

* Prepare :doc:`HTML Description<index.html>`
* Check :doc:`image sizes<image-sizes>`

Main image
==========

* Prepare image and specify it at ``"images"`` attribute at :doc:`manifest file<../dev/docs/__manifest__.py>`
* :doc:`Preview image at app store<app-store-preview>`

Live Preview
============

* Review ``"live_test_url"`` attribute at :doc:`manifest file<../dev/docs/__manifest__.py>`

  For example: ::
  
   "live_test_url": "http://apps.it-projects.info/shop/product/pos-multi-session?version=11.0",

* ``Live Preview`` button will appear at Odoo Apps Store after releasing the updates

.. image:: ../../images/live_preview.png
