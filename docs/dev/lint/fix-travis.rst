========================================
 Script for fixing travis error on odoo
========================================

Installation
============
::

    # install autopep8
    sudo pip install --upgrade autopep8

    # install oca-autopep8
    git clone https://github.com/OCA/maintainer-tools.git
    cd maintainer-tools
    sudo python setup.py install

    # install autoflake
    sudo pip install --upgrade autoflake

    # install fixmyjs
    sudo npm install fixmyjs -g

Script
======
::

    # fix line break symbols
    cd /path/to/MODULE_NAME
    find * -type f | grep -v ".\(svg\|png\|jpg\)$" | xargs sed -i 's/\r//g'

    # trim trailing whitespaces
    find * -type f | grep -v ".\(svg\|png\|jpg\)$" | xargs sed -i 's/[ \t]*$//g'

    # PEP8 для py-файлов:
    autopep8 --in-place -r --aggressive --aggressive --ignore E501 ./

    # fix CamelCase
    oca-autopep8 -ri --select=CW0001 .

    # Replacement button 'Tab' on 4 button 'Space':
    find . -type f -name '*.xml' | xargs sed -i 's/\t/    /g'
    find . -type f -name '*.py' | xargs sed -i 's/\t/    /g'
    find . -type f -name '*.js' | xargs sed -i 's/\t/    /g'


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

    #lint for js:
    fixmyjs --legacy --config ~/js_conf.json ./

    # Addition of the first row (coding) in py-files
    find -iname '*.py' | xargs grep -rLP 'coding: *utf-8' | xargs sed -i '1s/^/# -*- coding: utf-8 -*-\n/'

    # Correction is rights for run:
    find -iname '*.py' | xargs chmod -x

    # Duplicate implicit target name: "changelog".
    find . -type f -name 'changelog.rst' | xargs sed -i 's/^Changelog/Updates/g'
    find . -type f -name 'changelog.rst' | xargs sed -i 's/^=========/=======/g'
    
    # Replace @api.one -> @api.multi
    find . -type f -name '*.py' | xargs perl -i -p0e 's/'\
    '@api\.one\n'\
    '    def ([^(]*)\(([^(]*)\):/'\
    '@api.multi\n'\
    '    def $1($2):\n'\
    '        for r in self:\n'\
    '            r.$1_one($2)\n'\
    '\n'\
    '    \@api.multi\n'\
    '    def $1_one($2):\n'\
    '        self.ensure_one()/g'





Run following script only once::

    # Correction is links in rst-files
    #`_   ->   `__
    find . -type f -name '*.rst' | xargs sed -i 's/`_/`__/g'
