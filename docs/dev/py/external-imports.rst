===============================
 External dependencies in odoo
===============================

What
====

External dependencies are python packages or any binaries, that have to be installed to make module work.


How
===

In python files where you use external dependencies you will
need to add ``try-except`` with a debug log.

.. code-block:: py

    import

    try:
        import external_dependency_python_N
        import external_dependency_python_M
    except ImportError as err:
        _logger.debug(err)

    # for binary dependencies:
    try:
        import external_dependency_python_N
        import external_dependency_python_M
    except IOError as err:
        _logger.debug(err)

This rule doesn't apply to the test files since these files are loaded only when
running tests and in such a case your module and their external dependencies are installed.

Also, you you need to add external dependencies to :doc:`manifest<../docs/__manifest__.py>`.

Why
===

Odoo loads python files of a module whenever following conditions are satisfied:

* the module has static folder (e.g. for an icon)
* the module marked as installable in :doc:`manifest<../docs/__manifest__.py>`, i.e. the module *can* be installed

One can see, that odoo loads python files even if module is not installed (and even not intenteded to be installed). But modules usually are added to addons-path as a part of some repository (e.g. *pos-addons*). This is why importing external dependencies without ``try-except`` leads to problems on adding repostitory to :doc:`addons-path<../../admin/addons_path>`.
