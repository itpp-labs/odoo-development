====================
 JS tests via Tours
====================

How to run :doc:`odoo tours<../../description/js_tour>` in :doc:`phantom_js <phantom_js>` method?

10.0+
=====

.. code-block:: python

    from odoo.tests.common import HttpCase

    class CLASS_NAME(HttpCase):
        def test_NAME(self):

            tour = 'TOUR_NAME'
            self.phantom_js(
                URL_PATH,

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".run('%s')" % tour,

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".tours['%s'].ready" % tour,

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


