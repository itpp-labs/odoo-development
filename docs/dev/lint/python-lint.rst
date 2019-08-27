=============================
 Fixing python lints in odoo
=============================

All versions
============
::
 
    # PEP8 for py-files:
    autopep8 --in-place -r --aggressive --aggressive --ignore E501 ./

    # fix CamelCase
    oca-autopep8 -ri --select=CW0001 .

    # Replacement (relative-import)
    find . -type f -name '__init__.py' | xargs sed -i 's/^import/from . import/g'
    #find . -type f -name '__init__.py' | xargs sed -i 's/^import controllers/from . import controllers/g'
    #find . -type f -name '__init__.py' | xargs sed -i 's/^import models/from . import models/g'

    # remove unused imports
    autoflake --in-place -r --imports=openerp,openerp.http.request,openerp.SUPERUSER_ID,openerp.addons.base.ir.ir_qweb,openerp.exceptions.ValidationError,openerp.fields,openerp.api.openerp.models,openerp.osv.fields,openerp.osv.api,telebot,lxml,werkzeug,MySQLdb.cursors,cStringIO.StringIO,werkzeug.utils,pandas.merge,pandas.DataFrame,werkzeug.wsgi.wrap_file,werkzeug.wsgi,werkzeug.wsgi.wrap_file,openerp.exceptions,openerp.tools.DEFAULT_SERVER_DATETIME_FORMAT ./

    # remove prints
    find . -type f -name '*.py' | xargs sed -i 's/^\( *\)\(print .*\)/\1# \2/g'

    #Fix comments:
    find . -type f -name '*.py' | xargs sed -i -e 's/ #\([^ ]\)/ # \1/g'


    # Correction is rights for run:
    find -iname '*.py' | xargs chmod -x

Odoo 10-
========
::

    # Addition of the first row (coding) in py-files
    find -iname '*.py' | grep -v "__init__.py" | xargs grep -rLP 'coding: *utf-8' | xargs sed -i '1s/^/# -*- coding: utf-8 -*-\n/'


 
@api.one -> @api.multi
======================
::

    # Note. This solution doesn't work on methods that call super (e.g. write, create methods) or has to return value
    # Note. This solution doesn't handle properly methods with kwargs
    find . -type f -name '*.py' | xargs perl -i -p0e 's/'\
    '@api\.one\n'\
    '    def ([^(]*)\(self, ([^(]*)\):/'\
    '@api.multi\n'\
    '    def $1(self, $2):\n'\
    '        for r in self:\n'\
    '            r.$1_one($2)\n'\
    '        return True'\
    '\n'\
    '\n'\
    '    \@api.multi\n'\
    '    def $1_one(self, $2):\n'\
    '        self.ensure_one()/g'

    find . -type f -name '*.py' | xargs perl -i -p0e 's/'\
    '@api\.one\n'\
    '    def ([^(]*)\(self\):/'\
    '@api.multi\n'\
    '    def $1(self):\n'\
    '        for r in self:\n'\
    '            r.$1_one()\n'\
    '        return True'\
    '\n'\
    '\n'\
    '    \@api.multi\n'\
    '    def $1_one(self):\n'\
    '        self.ensure_one()/g'
