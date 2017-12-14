================================
 Fixing references on migration
================================


``9.0-`` → ``10.0+``
====================

.. code-block:: sh

    # menu_hr_configuration
    find . -type f -name '*.xml' | xargs sed -i 's/menu_hr_configuration/menu_human_resources_configuration/g'
    # base.group_hr
    find . -type f -name '*.csv'  -o -name '*.py' -o -name '*.xml'  | xargs sed -i 's/base.group_hr/hr.group_hr/g'
    # website.salesteam_website_sales
    find . -type f -name '*.csv'  -o -name '*.py' -o -name '*.xml'  | xargs sed -i 's/website.salesteam_website_sales/sales_team.salesteam_website_sales/g'
    # base.group_sale_salesman
    find . -type f -name '*.csv'  -o -name '*.py' -o -name '*.xml'  | xargs sed -i 's/base.group_sale_salesman/sales_team.group_sale_salesman/g'
    # product.prod_config_main
    find . -type f -name '*.xml' | xargs sed -i 's/product.prod_config_main/sale.prod_config_main/g'


``10.0-`` → ``11.0+``
=====================

.. code-block:: sh

    # mixins in js
    find . -type f -name '*.js' | xargs sed -i 's/core\.mixins/require("web.mixins")/g'

    # 11.0 doesn't have website.config.settings
    find . -type f -name '*.py' -o -iname '*.xml' | xargs sed -i 's/website\.config\.settings/res.config.settings/g'

    # pos.config form
    find . -type f -name '*.xml' | xargs sed -i 's/point_of_sale\.view_pos_config_form/point_of_sale\.pos_config_view_form/g'

    # web.webclient_bootstrap template
    find . -type f -name '*.xml' | xargs sed -i 's/web\.webclient_script/web\.webclient_bootstrap/g'
