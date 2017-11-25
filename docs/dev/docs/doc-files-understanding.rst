=========================
 Difference of doc files
=========================

README.rst
==========

Contains information interested for developers:

* short description
* technical details

doc/index.rst
=============

Usage instruction. Used by end users after purchasing the module. It shall give an answer to the question *"How to check that module works (how to install, how to configure, how to use)?"*. Also, it may cover the question *"How to safely uninstall the module"*.


static/description/index.html
=============================

Module representation. It shall give an answer to the questions *"Do I need this module? Should I buy it?"*.

Content intersection
====================

While every file has its own purpose, the content may intersect. If you don't want duplicate content, use the following priority:

* index.html
* index.rst
* README.rst

    .. image:: ../../images/doc-files.jpg
