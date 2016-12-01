========================================
 Script for fixing travis error on odoo
========================================

Installation
============

TODO

Script
======
::

    # fix line break symbols
    find * -type f | grep -v ".\(svg\|png\|jpg\)$" | xargs sed -i 's/\r//g'

    # trim trailing whitespaces
    find * -type f | grep -v ".\(svg\|png\|jpg\)$" | xargs sed -i 's/[ \t]*$//g'

    #PEP8 для py-файлов:
    autopep8 --in-place -r --aggressive --aggressive --ignore E501 ./

    # fix CamelCase
    oca-autopep8 -ri --select=CW0001 .

    #Замена знаков табуляций на 4 пробела:
    find . -type f -name '*.xml' | xargs sed -i 's/\t/    /g'
    find . -type f -name '*.py' | xargs sed -i 's/\t/    /g'
    find . -type f -name '*.js' | xargs sed -i 's/\t/    /g'


    #Замена (relative-import)
    find . -type f -name '__init__.py' | xargs sed -i 's/^import/from . import/g'
    #find . -type f -name '__init__.py' | xargs sed -i 's/^import controllers/from . import controllers/g'
    #find . -type f -name '__init__.py' | xargs sed -i 's/^import models/from . import models/g'

    #Удаление unused импортов (по мере появления новых неспользуемых пакетов можно пополнять список --imports)
    autoflake --in-place -r --imports=openerp,openerp.http.request,openerp.SUPERUSER_ID,openerp.addons.base.ir.ir_qweb,openerp.exceptions.ValidationError,openerp.fields,openerp.api.openerp.models,openerp.osv.fields,openerp.osv.api,telebot,lxml,werkzeug,MySQLdb.cursors,cStringIO.StringIO,werkzeug.utils,pandas.merge,pandas.DataFrame,werkzeug.wsgi.wrap_file,werkzeug.wsgi,werkzeug.wsgi.wrap_file,openerp.exceptions,openerp.tools.DEFAULT_SERVER_DATETIME_FORMAT ./

    # удаление принтов
    find . -type f -name '*.py' | xargs sed -i 's/^\( *\)\(print .*\)/\1# \2/g'


    #Fix comments:
    find . -type f -name '*.py' | xargs sed -i -e 's/ #\([^ ]\)/ # \1/g'

    #lint for js:
    fixmyjs --legacy --config ~/js_conf.json ./

    #Добавление первой строки (coding) в py-файлы
    find -iname '*.py' | xargs grep -rLP 'coding: *utf-8' | xargs sed -i '1s/^/# -*- coding: utf-8 -*-\n/'

    #Исправление прав на исполнение:
    find -iname '*.py' | xargs chmod -x

    # Duplicate implicit target name: "changelog".
    find . -type f -name 'changelog.rst' | xargs sed -i 's/^Changelog/Updates/g'
    find . -type f -name 'changelog.rst' | xargs sed -i 's/^=========/=======/g'


Run following script only once::

    #Исправление ссылок в rst-файлах делается простой автозаменой.
    # (запускать 1 раз!)
    #`_   ->   `__
    find . -type f -name '*.rst' | xargs sed -i 's/`_/`__/g'
