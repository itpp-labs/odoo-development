Inherit
=======

Collisions and priority
-----------------------

If two or more xml templates inherit same parent template they can have same priorities.
It may produce conflicts and unexpected behavior.
What you need is just set priority explicitly in your template::

    <template ..." priority="8" ..>

Less priority means prior execution.

Default priority is 16.
