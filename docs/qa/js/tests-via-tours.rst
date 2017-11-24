====================
 JS tests via Tours
====================


It is possible to run js phantom tests using :doc:`odoo tours<../../description/js_tour>` as JS testing code.

How to run tour in unittests
============================

* :doc:`Create tour<../../description/js_tour>` via js file
* Follow instruction for `python tests <../python/test-enable#docker-users>`_
* run tour via phantom js

  * 10.0+:

    .. code-block:: python

        class CLASS_NAME(...):
        def test_NAME(self):

            self.phantom_js(
                URL_PATH,

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".run('TOUR_NAME')",

                "odoo.__DEBUG__.services['web_tour.tour']"
                ".tours.TOUR_NAME.ready",

                login=LOGIN_OR_NONE
            )

  * 8.0, 9.0:

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


