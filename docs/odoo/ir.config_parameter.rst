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

Search addons for *model="ir.config_parameter"* for more examples.

Change existing setting
^^^^^^^^^^^^^^^^^^^^^^^
Code::

    <function model="ir.config_parameter" name="set_param" eval="('auth_signup.allow_uninvited', True)" />

