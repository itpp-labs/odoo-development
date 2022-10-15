============
 Debugging
============

Launch Configurations
---------------------

    To debug your app in VS Code, you'll first need to set up your launch configuration file - launch.json. 
    Click on the Configure gear icon on the Debug view top bar, choose your debug environment and VS Code will 
    generate a launch.json file under your workspace's .vscode folder.

**sample python Debugging**

.. code-block:: javascript

        {
            "name": "Python",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false,
            "pythonPath": "${config:python.pythonPath}",
            //"program": "${file}", use this to debug opened file.
            "program": "${workspaceRoot}/Path/To/odoo.py",
            "args": [
              "-c ${workspaceRoot}/sampleconfigurationfile.cfg"  
            ],
            "cwd": "${workspaceRoot}",
            "console": "externalTerminal",
            "debugOptions": [
                "WaitOnAbnormalExit",
                "WaitOnNormalExit",
                "RedirectOutput"
            ]
        },  

.. important:: use "args" to specify any options like databace, config or user name and password.

`sorce <https://code.visualstudio.com/Docs/editor/debugging>`_ 
