====================
 JS tests via Tours
====================

How to run :doc:`odoo tours<../../description/js_tour>` in :doc:`phantom_js <phantom_js>` method?

10.0+
=====

.. code-block:: python

    class CLASS_NAME(...):
        def test_NAME(self):

            self.phantom_js(
                URL_PATH,

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".run('TOUR_NAME')",

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".tours['TOUR_NAME'].ready",

                login=LOGIN_OR_NONE
            )

8.0, 9.0
========

.. code-block:: python

        class CLASS_NAME(...):
            def test_NAME(self):

                self.phantom_js(
                    URL_PATH,

                    "odoo.__DEBUG__.services['web.Tour']"
                    ".run('TOUR_NAME', 'test')",

                    "odoo.__DEBUG__.services['web.Tour']"
                    ".tours.TOUR_NAME",

                    login=LOGIN_OR_NONE
                )


