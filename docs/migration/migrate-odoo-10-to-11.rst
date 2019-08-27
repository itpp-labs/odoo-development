=====================================================================
 ``10.0-`` → ``11.0+``, py2 → py3, shared Settings, sudo.get_param()
=====================================================================

New API
=======

.. code-block:: sh

    # ir.config_parameter -- prefix get_param / set_param with sudo()
    find . -type f -name '*.py' | xargs perl -i -p0e 's/(?<!sudo\(\)\.)(get_param|set_param)/sudo().$1/g'
    find . -type f -name '*.xml' | xargs perl -i -p0e 's/(?<!sudo\(\)\.)(get_param|set_param)/sudo().$1/g'

    # page="True" is not used anymore
    find . -type f -name '*.xml' | xargs sed -i 's/ page="True"//g'
    
    # TODO: commands for "shared Settings" (python and xml)

New references
==============

.. code-block:: sh

    # mixins in js
    find . -type f -name '*.js' | xargs sed -i 's/core\.mixins/require("web.mixins")/g'

    # 11.0 doesn't have website.config.settings
    find . -type f -name '*.py' -o -iname '*.xml' | xargs sed -i 's/website\.config\.settings/res.config.settings/g'

    # pos.config form
    find . -type f -name '*.xml' | xargs sed -i 's/point_of_sale\.view_pos_config_form/point_of_sale\.pos_config_view_form/g'

    # web.webclient_bootstrap template
    find . -type f -name '*.xml' | xargs sed -i 's/web\.webclient_script/web\.webclient_bootstrap/g'

    # 11.0 doesn't have base_action_rule module, it was was renamed to base_automation
    find . -type f -name '*.xml' | xargs sed -i 's/base\.action\.rule/base\.automation/g'
    find . -type f -name '*.py' | xargs sed -i "s/'base_action_rule'/'base_automation'/g"
    find . -type f -name '*.py' | xargs sed -i 's/"base_action_rule"/"base_automation"/g'

    # base.config.settings merged into res.config.settings
    find . -type f -name '*.xml' -or -name "*.py"  | xargs sed -i 's/base\.config\.settings/res.config.settings/g'

    # kanban_record in js
    find . -type f -name '*.js' | xargs sed -i 's/web_kanban\.Record/web.KanbanRecord/g'

    # Model -> rpc in require
    find . -type f -name '*.js' | xargs sed -i "s/var Model = require('web\.Model');/var rpc = require('web\.rpc');/g"
    find . -type f -name '*.js' | xargs sed -i 's/var Model = require("web\.Model");/var rpc = require("web\.rpc");/g'

Python 3
========

.. code-block:: sh

    # coding: utf-8 is not needed anymore
    find . -type f -name '*.py' | xargs sed -i '/# -\*- coding: utf-8 -\*-/d'

    # urlparse
    find . -type f -name '*.py' | xargs sed -i 's/import urlparse/import urllib.parse as urlparse/g'
    find . -type f -name '*.py' | xargs sed -i 's/from urlparse/from urllib.parse/g'
    # StringIO
    find . -type f -name '*.py' | xargs sed -i 's/from cStringIO import StringIO/from io import StringIO/g'
    find . -type f -name '*.py' | xargs sed -i 's/from StringIO import StringIO/from io import StringIO/g'

    # base64
    # TODO
    # SOMETHING.encode('base64') -> base64.b64encode(SOMETHING)
    # SOMETHING.decode('base64') -> base64.b64decode(SOMETHING)
