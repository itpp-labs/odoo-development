ir.config_parameter
===================

XML operations
--------------

Create new setting
^^^^^^^^^^^^^^^^^^
Code::

        <record id="myid" model="ir.config_parameter">
            <field name="key">auth_signup.allow_uninvited</field>
            <field name="value">True</value>
        </record>

Instead of *myid* existed id from other module can be used to overwrite value. Example: <record id="auth_signup.allow_uninvited" model="ir.config_parameter">.

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

