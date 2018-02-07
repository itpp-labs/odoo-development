# -*- coding: utf-8 -*-
{
    "name": """{MODULE_NAME}""",
    "summary": """{SHORT_DESCRIPTION_OF_THE_MODULE}""",
    "category": "{MODULE_CATEGORY}",
    # "live_test_url": "",
    "images": [],
    "version": "{BRANCH}.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, {DEVELOPER_NAME}",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/{DEVELOPER_GITHUB_USERNAME}",
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
    "qweb": [
        "static/src/xml/{QWEBFILE1}.xml",
    ],
    "demo": [
        "demo/{DEMOFILE1}.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
