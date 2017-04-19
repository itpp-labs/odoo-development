Commit comment prefix
=====================
Based on: https://www.odoo.com/documentation/8.0/reference/guidelines.html

Basic tags
----------

* **[DOC]**  for documentation. Don't use any other tags when you improve, fix, refactor documentation
* **[PORT]** for porting *(version tag is required)*
* **[BACKPORT]** for back-porting *(version tag is required)*
* **[IMP]** for improvements
* **[FIX]** for bug fixes
* **[REF]** for refactoring
* **[TEXT]** for commits with text changes only: labels, hints, comments, etc., but not for updates in documentation (\*.rst and \*.html files)
* **[ADD]** for adding new resources (new modules or files) and some time - for new features.
* **[REM]** for removing of resources
* **[REL]** for releases
* **[CI]** for updating ``.travis.yml``, ``requirements.txt``, ``*/tests/*``, etc. files
* **[LINT]** for fixing lint errors
* **[i18n]** for translations

Version tags
------------

* **[8.0]**
* **[9.0]**
* **[10.0]**
* etc.

Forbidden
---------

Don't use tags below

* **[WIP]**, **[DEV]** -- instead of noting that work in progress make message as if your work is already done.
