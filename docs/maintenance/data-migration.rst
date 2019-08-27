================
 Data Migration
================

Data Migration is a process of keeping correct data in database after updating to new module version. For example, simple field renaming leads to data lost if you don't have proper data migration scripts.

For *Module Migration* see :doc:`Porting Modules<../migration/index>`

Preparing
---------

Those migrations are between module version.

From Odoo https://github.com/odoo/odoo/blob/11.0/odoo/modules/migration.py#L53:

This class manage the migration of modules.
Migrations files must be python files containing a ``migrate(cr, installed_version)``
function. Theses files must respect a directory tree structure: A 'migrations' folder
which contains a folder by version. Version can be 'module' version or 'server.module'
version (in this case, the files will only be processed by this version of the server).
Python file names must start by *pre* or *post* and will be executed, respectively,
before and after the module initialisation. *end* scripts are run after all modules have been updated.

Example::

    <moduledir>
    `-- migrations
        |-- 1.0
        |   |-- pre-update_table_x.py
        |   |-- pre-update_table_y.py
        |   |-- post-create_plop_records.py
        |   |-- end-cleanup.py
        |   `-- README.txt                      # not processed
        |-- 9.0.1.1                             # processed only on a 9.0 server
        |   |-- pre-delete_table_z.py
        |   `-- post-clean-data.py
        `-- foo.py                              # not processed

Execution
---------

Migration files are just code files that don't need to be registered anywhere.
When updating an addon Odoo searching in the *migrations* for folders with a version in between, up to, and including the version that is in updating for.
It happens before all other files were observed, so at this moment nothing is changed at your database layout.
Then, if folders are found Odoo executes python files with prefix *pre-* in it.
They should contain a defined function called migrate. This function has two arguments: database cursor and currently installed version.

After all pre-migrate functions were successfully executed, Odoo updates the module.
Now, the database might be different from the previous version one.
For example, if in a new version we changed the model field type, in the database this column will be changed without data preserving.
Or if a field was renamed, in the new version just a new column will be created.

Then, after the module was updated, Odoo search for post-migrate files by the same algorithm and execute them.

*end* scripts are run after all modules have been updated.

.. warning:: Migration updates are not rollbacked if some errors happened later during modules updating process. So, you shall always try to update module with migration scripts on a copy first.

Example
-------

*POS Debt & Credit notebook*. We need to preserve credit_product field data in the ``product.template`` model after updating to a newer version.
In previous version it was boolean field, now it is a many2one field with the relation to ``account.journal`` model.
Here, we, using a temporary column, calculate transfer data from boolean to many2one credit_product field.

*pre-migrate.py*::

    def migrate(cr, version):
        # Add temporary credit product column
        cr.execute('ALTER TABLE product_template ADD temporary_credit_product int')
        # Select debt journals
        cr.execute('SELECT id FROM account_journal WHERE account_journal.debt is true')
        # Take the first journal
        journal_id = cr.fetchone()
        if journal_id:
            # set token one to all credit products
            cr.execute('UPDATE product_template SET temporary_credit_product=%s WHERE credit_product is true', journal_id)

*post-migrate.py*::

    def migrate(cr, version):
        # update new credit_product column with the tempory one
        cr.execute('UPDATE product_template SET credit_product=temporary_credit_product')
        # Drop temporary column
        cr.execute('ALTER TABLE product_template DROP COLUMN temporary_credit_product')
