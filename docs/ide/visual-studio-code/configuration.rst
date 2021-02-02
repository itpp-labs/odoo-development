===============
Configuration:-
===============

**sample configuration (for user or workspace setting)**

.. code-block:: javascript
    
        // Place your settings in this file to overwrite default and user settings.
        {   
            //"python.pythonPath": "optional: path to python use if you have environment path ",

            // use this so the autocompleate/goto definition will work with python extension
            "python.autoComplete.extraPaths": [
            "${workspaceRoot}/odoo/addons",
            "${workspaceRoot}/odoo",
            "${workspaceRoot}/odoo/openerp/addons" ],

            //"python.linting.pylintPath": "optional: path to python use if you have environment path",

            "python.linting.enabled": true,

            //load the pylint_odoo 

            "python.linting.pylintArgs": ["--load-plugins", "pylint_odoo"],

            "python.formatting.provider": "yapf",

            //"python.formatting.yapfPath": "optional: path to python use if you have environment path",

             // "python.linting.pep8Path": "optional: path to python use if you have environment path",

             "python.linting.pep8Enabled": true,

            // add this auto-save option so the pylint will sow errors while editing otherwise 
            //it will only show the errors on file save
            "files.autoSave": "afterDelay",
            "files.autoSaveDelay": 500,

            // The following will hide the compiled file in the editor/ add other file to hide them from editor
            "files.exclude": {
                "**/*.pyc": true     
                                }
        }

.. note:: some lines are commented because it is optional. 
          you can activate them if needed like in the case
          of using Virtualenv.


