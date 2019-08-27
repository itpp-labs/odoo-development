# Copyright 2019 {DEVELOPER_NAME} <https://it-projects.info/team/{DEVELOPER_GITHUB_USERNAME}>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """{MODULE_NAME}""",
    "summary": """{SHORT_DESCRIPTION_OF_THE_MODULE}""",
    "category": "{MODULE_CATEGORY}",
    # "live_test_url": "http://apps.it-projects.info/shop/product/DEMO-URL?version={ODOO_BRANCH}",
    "images": [],
    "version": "{ODOO_BRANCH}.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, {DEVELOPER_NAME}",
    "support": "apps@it-projects.info",
    "website": "https://apps.odoo.com/apps/modules/{VERSION}/{TECHNICAL_NAME}/",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        "{DEPENDENCY1}",
        "{DEPENDENCY2}",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "{FILE1}.xml",
        "{FILE2}.xml",
    ],
    "demo": [
        "demo/{DEMOFILE1}.xml",
    ],
    "qweb": [
        "static/src/xml/{QWEBFILE1}.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    # "demo_title": "{MODULE_NAME}",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "{SHORT_DESCRIPTION_OF_THE_MODULE}",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
