Tmux installation
=================


Install Tmux
------------

::

 sudo apt-get install tmux 

Check version

::

 tmux -V

If you have 1.8 or older then you should update.
Here are update commands for ubuntu 14.04

::

 sudo apt-get update
 sudo apt-get install -y python-software-properties software-properties-common
 sudo add-apt-repository -y ppa:pi-rho/dev
 sudo apt-get update
 sudo apt-get install -y tmux=2.0-1~ppa1~t

Now if you do ``tmux -V`` it should show ``tmux 2.0`` which is a good version for tmux plugins.

Based on: http://stackoverflow.com/questions/25940944/ugrade-tmux-from-1-8-to-1-9-on-ubuntu-14-04


Install Tmux Plugin Manager
---------------------------

Requirements: ``tmux`` version 1.9 (or higher), ``git``, ``bash``

Clone TPM:

::

 $ git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

Put this at the bottom of .tmux.conf:

::

 # List of plugins
 set -g @plugin 'tmux-plugins/tpm'
 set -g @plugin 'tmux-plugins/tmux-sensible'

 # Other examples:
 # set -g @plugin 'github_username/plugin_name'
 # set -g @plugin 'git@github.com/user/plugin'
 # set -g @plugin 'git@bitbucket.com/user/plugin'

 # Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
 run '~/.tmux/plugins/tpm/tpm'

Reload TMUX environment so TPM is sourced:

::

 # type this in terminal
 $ tmux source ~/.tmux.conf

Based on: https://github.com/tmux-plugins/tpm

Install Tmux Resurrect
----------------------

Add plugin to the list of TPM plugins in .tmux.conf:

::

 set -g @plugin 'tmux-plugins/tmux-resurrect'

Hit ``prefix + I`` to fetch the plugin and source it. You should now be able to use the plugin.

Based on: https://github.com/tmux-plugins/tmux-resurrect

Install tmux-continuum
----------------------

Last saved environment is automatically restored when tmux is started.
Put the following lines in ``tmux.conf``:

::

 set -g @continuum-save-interval '5'
 set -g @continuum-restore 'on'

Your environment will be automatically saved every 5 minutes.
When you start tmux it will automatically restore

Based on: https://github.com/tmux-plugins/tmux-continuum
