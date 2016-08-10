Tmux configuration
==================

Create a file with the name ``.tmux.conf`` in your home directory.

An example of ``.tmux.conf``:

::

  # Global settings 

  # Set prefix key to Ctrl-a
  # unbind-key C-b
  # set-option -g prefix C-a

  # send the prefix to client inside window
  # bind-key C-a send-prefix

  # scrollback buffer n lines
  set -g history-limit 10000

  # tell tmux to use 256 colour terminal
  set -g default-terminal "screen-256color"

  # enable wm window titles
  set -g set-titles on

  # reload settings
  bind-key R source-file ~/.tmux.conf

  # Statusbar settings 

  # toggle statusbar
  bind-key s set status

  # use vi-style key bindings in the status line
  set -g status-keys vi

  # amount of time for which status line messages and other indicators
  # are displayed. time is in milliseconds.
  set -g display-time 2000

  # default statusbar colors
  set -g status-fg white
  set -g status-bg default
  set -g status-attr default

  # default window title colors
  setw -g window-status-fg white
  setw -g window-status-bg default
  setw -g window-status-attr dim

  # active window title colors
  setw -g window-status-current-fg cyan
  setw -g window-status-current-bg default
  #setw -g window-status-current-attr bright
  setw -g window-status-current-attr underscore

  # command/message line colors
  set -g message-fg white
  set -g message-bg black
  set -g message-attr bright

  set-option -g status-keys vi 
  set-option -g mode-keys vi 

  # List of plugins
  set -g @plugin 'tmux-plugins/tpm'
  set -g @plugin 'tmux-plugins/tmux-sensible'
  set -g @plugin 'tmux-plugins/tmux-resurrect'
  set -g @plugin 'tmux-plugins/tmux-continuum'
  set -g @continuum-save-interval '5'
  set -g @continuum-restore 'on'

  # Other examples:
  # set -g @plugin 'github_username/plugin_name'
  # set -g @plugin 'git@github.com/user/plugin'
  # set -g @plugin 'git@bitbucket.com/user/plugin'

  # Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
  run '~/.tmux/plugins/tpm/tpm'
