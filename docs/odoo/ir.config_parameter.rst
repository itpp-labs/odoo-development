ir.config_parameter
===================

XML operations
--------------

Create new setting
^^^^^^^^^^^^^^^^^^
Code::

        <record id="myid" model="ir.config_parameter">
            <field name="key">mymodule.mykey</field>
            <field name="value">True</value>
        </record>

Use this approach only to manipulate keys you create.
It's not recommended to change others modules this way.
For example such like this::

     <record model="ir.config_parameter" id="website.google_app_key">

Search addons for *model="ir.config_parameter"* for more examples.

Such record usually used with <data noupdate="1">.

Change existing setting
^^^^^^^^^^^^^^^^^^^^^^^
Code::

    <function model="ir.config_parameter" name="set_param" eval="('auth_signup.allow_uninvited', True)" />

Prons:

    works if you are not sure whether key already used or not

Cons:

    record is not deleted on uninstalling

