==============
 What to test
==============

Obviously, you have to test features that module provide. But, it's important to have a stable module to test that features in a different context. This article tries to describe what that context could be. It can be used both for manual and automatic tests.

More about automatic tests:

*   :doc:`Client-side unittests <js>`
*   :doc:`Server-side unittests <python>`


User
====

While you develop a module, you can use an admin user for manual checking the result. It could simplify the process of development, because you can skip security stuff for a while. But when you prepare module for relase you absolutely need to check how system works from non-admin user.

.. warning:: Admin user has :doc:`special access rights <../access/admin>`. Use another User to test module.
