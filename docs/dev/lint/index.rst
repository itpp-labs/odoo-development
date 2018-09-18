======
 Lint
======

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
    # increase max errors to be fixed (otherwise script stops)
    echo '{"maxerr": 1000}' > ~/.jshintrc


Common lints
============
::

    EXCLUDE_FILES=".\(svg\|gif\|png\|jpg\)$"
    # fix line break symbols
    cd /path/to/MODULE_NAME
    find * -type f | grep -v $EXCLUDE_FILES | xargs sed -i 's/\r//g'

    # add line break to the end of file
    find * -type f | grep -v $EXCLUDE_FILES | xargs sed -i '$a\'

    # trim trailing whitespaces
    find * -type f | grep -v $EXCLUDE_FILES | xargs sed -i 's/[ \t]*$//g'

    # Replacement button 'Tab' on 4 button 'Space':
    find . -type f -name '*.xml' -or -name '*.py' -or -name '*.js'| xargs sed -i 's/\t/    /g'


.. toctree::

   python-lint
   js-lint
   rst-lint
   xml-lint
