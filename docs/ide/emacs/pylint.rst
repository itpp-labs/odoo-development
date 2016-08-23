========
 Pylint
========

Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code’s complexity.
https://pylint.readthedocs.io/en/latest/

Install pylint.

::

 sudo pip install pylint

With the Flycheck emacs extension, pylint’s output will be shown right inside your emacs buffers.
Spacemacs has flycheck in his ``syntax-checking`` layer.

::

 M-x package-install RET flycheck

Configure pylint by using a pylintrc file.

::

 pylint --generate-rcfile >.pylintrc


Pylint Odoo plugin
------------------

Install pylint odoo plugin
https://github.com/OCA/pylint-odoo

::

 pip install --upgrade git+https://github.com/oca/pylint-odoo.git

 or

 pip install --upgrade --pre pylint-odoo


Add the plugin in pylintrc.

::

 load-plugins=pylint_odoo


Useful configurations
---------------------

By default there is 100 characters per line allowed.
Allow 120 characters

::

 max-line-length=120

To disable certain warning add its code to ``disable`` list in pylintrc.
For example, If you don't like this message ``Missing method docstring`` with code C0111 or
this ``Use of super on an old style class`` (E1002)

::

 disable=E1608,W1627,E1601,E1603,E1602,E1605,E1604,E1607,E1606,W1621,W1620,W1623,W1622,W1625,W1624,W1609,W1608,W1607,W1606,W1605,W1604,W1603,W1602,W1601,W1639,W1640,I0021,W1638,I0020,W1618,W1619,W1630,W1626,W1637,W1634,W1635,W1610,W1611,W1612,W1613,W1614,W1615,W1616,W1617,W1632,W1633,W0704,W1628,W1629,W1636,C0111,E1002

You can find other codes here: http://pylint-messages.wikidot.com/


Flychek highlights odoo import lines as ``from openerp import models, fields, api``
with error message ``F0401: Unable to import...``.
There are two options to fix it - http://stackoverflow.com/questions/1899436/pylint-unable-to-import-error-how-to-set-pythonpath.

Edit ``pylintrc`` to include your odoo directory like this:

::

 init-hook='import sys; sys.path.append("/path/to/odoo")'
