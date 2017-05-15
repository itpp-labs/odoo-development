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

* Module Name MUST be the same at :doc:`manifest file<../dev/docs/__openerp__.py>`, :doc:`README.rst<../dev/docs/README.rst>`, :doc:`doc/index.rst<../dev/docs/usage-instructions>`


Summary
=======

* Review ``"summary"`` attribute at  :doc:`manifest file<../dev/docs/__openerp__.py>` and first paragraph at :doc:`README.rst<../dev/docs/README.rst>`. They MUST be presented, but MAY be different.


Price
=====

* Review ``"price"`` attribute at  :doc:`manifest file<../dev/docs/__openerp__.py>`

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

* Prepare image and specify it at ``"images"`` attribute at :doc:`manifest file<../dev/docs/__openerp__.py>`
* :doc:`Preview image at app store<app-store-preview>`
