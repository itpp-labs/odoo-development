====================
 Docs and manifests
====================

**All** files from this section ought to be fully [*]_ prepared **before** any other files in new module. It helps you to review requirements again before you start.

.. toctree::
   :maxdepth: 1

   README.rst.rst           
   usage-instructions
   __openerp__.py
   changelog.rst.rst

Don't forget to keep correct rst format.

::

    OK:
    ===========================
     Correctly formatted Title
    ===========================

    Correctly formatted section
    ===========================

    BAD:
    ===========================================
    No spaces at the beggining and end of title
    ===========================================

    =============================
     No space at the end of title
    =============================

    =======================================
    Incorrect number of signs in title
    ========================================

    ================
    Incorrect number of signs in title
    ================

    Incorrect number of signs in section
    =====================================

    Incorrect number of signs in section
    ===================================

.. [*] The only exception could be made for *"data"* field in ``__openerp__.py`` file.
