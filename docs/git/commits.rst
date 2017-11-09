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
* **[NEW]** for uploading new modules *(version tag is required)*
* **[ADD]** for adding new resources and features.
* **[REM]** for removing of resources *(version tag is required)*
* **[DEMO]** for adding / updating demostration data
* **[CI]** for updating ``.travis.yml``, ``requirements.txt``, ``*/tests/*``, etc. files
* **[LINT]** for fixing lint errors
* **[i18n]** for translations

Version tags
------------

* **[8.0]**
* **[9.0]**
* **[10.0]**
* etc.

Put tags before other tags, e.g.::

    [9.0][BACKPORT] module_xxx

Temporar tags
-------------

* **[WIP]**, **[DEV]**, **[TMP]** -- for commits that has to be squashed before merging

Which tag to use?
-----------------

* If commit upload new module:

  * use **[NEW]**

* If commit updates are only in module description (*doc/\**, *static/description/\**,  *README.rst*, ``name`` and ``summarry`` attributes at manifest) or in code comments:

  * use **[DOC]**

* If commit works with translation\localisations only:

  * use **[i18n]**

* If commit changes only some string related to UI (e.g. Error Message, Name of something etc.)

  * use **[TEXT]**

* If commit fixes issue related to switch to another major odoo version 

  * use *Version tag* and

    * use **[PORT]** if target version is newer than original (e.g. porting from odoo 10.0 to odoo 11.0)
    * use **[BACKPORT]** if target version is older than original (e.g. porting from odoo 10.0 to odoo 9.0)
* If commit updates demostration data

  * use **[DEMO]**

* If commit updates / configures automatic tests

  * use **[CI]**

* If commit fixes existing features:

  * use **[FIX]**

* If commit improves existing features:

  * use **[IMP]**

* If commit adds new features:

  * use **[ADD]**

* If commit makes updates asked by lint tools:

  * use **[LINT]**

* If commit updates (refactors) existing code without adding or fixing features:

  * use **[REF]**

**Notes**

* Order of this *if-then-that* list matters. Use some *that* only if all *if-blocks* above it are false.
* If your commit makes update of different types you need to describe each update separately using appropriate tag, e.g.::

    [FIX] bug in feature X ...
    [IMP] UI improvements in feature Y ...
    ...

Emoji
-----

Yes, you can add some fun and emotions to your commit. Select emojii you like `here <https://gist.github.com/yelizariev/6277767c8e3e01148a52f15024efc2fd>`_ and copy-paste to you commit message, `e.g. <https://github.com/yelizariev/dummy-addons/commit/30e3c1cd7723583a52c6ea268381ef6922781826>`_:

``[NEW] super-puper module is released! :boom:``
