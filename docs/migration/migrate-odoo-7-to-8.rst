=================================================================
 ``7.0-`` → ``8.0+``, ``(cr, uid, ids, context)`` → ``self.env``
=================================================================

Automatic replacements
======================

.. code-block:: sh

    # IMPORTS
    # replace osv, orm
    find . -type f -name '*.py' | xargs sed -i 's/from openerp.osv import orm$/from odoo import models/g'
    find . -type f -name '*.py' | xargs sed -i 's/from openerp.models.orm import Model$/from odoo.models import Model/g'
    find . -type f -name '*.py' | xargs sed -i 's/osv.osv_memory/models.TransientModel/g'
    find . -type f -name '*.py' | xargs sed -i 's/osv.osv/models.Model/g'
    find . -type f -name '*.py' | xargs sed -i 's/osv.except_osv/UserError/g'
    find . -type f -name '*.py' | xargs sed -i 's/osv\./models./g'
    find . -type f -name '*.py' | xargs sed -i 's/\<orm\./models./g'
    find . -type f -name '*.py' | xargs sed -i 's/\(import .*\), osv/\1, models/g'
    find . -type f -name '*.py' | xargs sed -i 's/\(import .*\)osv, /\1models, /g'
    find . -type f -name '*.py' | xargs sed -i 's/\(import .*\)osv/\1models/g'

    find . -type f -name '*.py' | xargs sed -i 's/\(import .*\), orm/\1/g'
    find . -type f -name '*.py' | xargs sed -i 's/\(import .*\)orm, /\1/g'
    find . -type f -name '*.py' | xargs sed -i 's/^.*import orm$//g'

    find . -type f -name '*.py' | xargs sed -i 's/openerp.osv/openerp/g'

    # replace http import
    find . -type f -name '*.py' | xargs sed -i 's/from openerp.addons.web import http/from odoo import http/g'
    find . -type f -name '*.py' | xargs sed -i 's/openerp.addons.web.http/odoo.http/g'
    find . -type f -name '*.py' | xargs sed -i 's/openerp.http/odoo.http/g'

    # replace odoo
    # fix importing. Otherwise you will get error:
    #   AttributeError: 'module' object has no attribute 'session_dir'
    find . -type f -name '*.py' | xargs sed -i 's/openerp.tools.config/odoo.tools.config/g'

    # general replacement
    find . -type f -name '*.py' | xargs sed -i 's/from openerp/from odoo/g'


    # FIELDS
    # update fields
    # (multiline: http://stackoverflow.com/questions/1251999/how-can-i-replace-a-newline-n-using-sed/7697604#7697604 )
    # delete _columns
    find . -type f -name '*.py' | xargs perl -i -p0e 's/    _columns = {(.*?)\n    }/$1\n/gs'
    # computed fields
    find . -type f -name '*.py' | xargs sed -i 's/fields.function(\(.*\) \(["\x27][^,]*\)/fields.function(\1 string=\2/g'
    find . -type f -name '*.py' | xargs sed -i 's/fields.function(\(.*\) multi=[^,)]*/fields.function(\1/g'
    find . -type f -name '*.py' | xargs sed -i 's/fields.function(\([^,]*\)\(.*\)type=.\([2a-z]*\)["\x27]/fields.\3(compute="\1"\2/g'
    find . -type f -name '*.py' | xargs sed -i 's/fields.many2one(\(.*\)obj=\([^,]*\)/fields.many2one(\2, \1/g'
    find . -type f -name '*.py' | xargs sed -i 's/,[ ]*,/,/g'
    find . -type f -name '*.py' | xargs sed -i 's/,[ ]*,/,/g'
    find . -type f -name '*.py' | xargs sed -i 's/,[ ]*,/,/g'

    # replace fields
    find . -type f -name '*.py' | xargs perl -i -p0e 's/    _columns = {(.*?)    }/$1/gs'
    find . -type f -name '*.py' | xargs sed -i 's/fields\.\(.\)/fields.\u\1/g'
    find . -type f -name '*.py' | xargs sed -i 's/    [\x27"]\(.*\)[\x27"].*:.*\(fields.*\),$/\1 = \2/g'
    
    # renamed attributes
    find . -type f -name '*.py' | xargs sed -i 's/select=/index=/g'
    find . -type f -name '*.py' | xargs sed -i 's/digits_compute=/digits=/g'

Semi-Automatic replacements
===========================

We recommend to use commands below after commiting previous changes. It allows you to check differences.

The commands doesn't update code fully and usually you need to continue updates manually.

.. code-block:: sh

    # pool -> env
    find . -type f -name '*.py' | xargs sed -i 's/self.pool/self.env/g'
    # remove cr, uid
    find . -type f -name '*.py' | xargs sed -i 's/(cr, [^,]*, /(/g'
    find . -type f -name '*.py' | xargs sed -i 's/(self, cr, [^,]*, ids/(self/g'
    find . -type f -name '*.py' | xargs sed -i 's/(self, cr, uid, /(self, /g'
    find . -type f -name '*.py' | xargs sed -i 's/, context=[^,)]*//g'
    find . -type f -name '*.py' | xargs sed -i 's/self.env.get(\([^)]*\))/self.env[\1]/g'
    # res_config.py
    find . -type f -name 'res_config.py' | xargs sed -i 's/\(def get_default_.*\)(self)/\1(self, fields)/g'
