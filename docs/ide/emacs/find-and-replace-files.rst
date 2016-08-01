=========================================
 Replace text in recursively found files
=========================================

 1. ``M-x find-name-dired``: you will be prompted for a root directory and a filename pattern.
 2. Press ``t`` to "toggle mark" for all files found.
 3. Press ``Q`` for "Query-Replace in Files...": you will be prompted for query/substitution regexps.
 4. Proceed as with ``query-replace-regexp``: ``SPACE`` to replace and move to next match, ``n`` to skip a match, etc.

Based on: http://stackoverflow.com/questions/270930/using-emacs-to-recursively-find-and-replace-in-text-files-not-already-open
