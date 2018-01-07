=====================
 ir.config_parameter
=====================

Add record by module
====================

XML: <record>
-------------
Code::

    <data noupdate="1">
        <record id="myid" model="ir.config_parameter">
            <field name="key">mymodule.mykey</field>
            <field name="value">True</value>
            <field name="group_ids" eval="[(4, ref('base.group_system'))]"/>
        </record>

Prons:

* record is deleted on uninstalling

Cons:

* it raises error, if record with that key is already created manually

XML: <function>
---------------

Code::

    <function model="ir.config_parameter" name="set_param" eval="('auth_signup.allow_uninvited', True, ['base.group_system'])" />

Prons:

* it doesn't raise error, if record with that key is already created manually

Cons:

* record is not deleted on uninstalling
* value is overwrited after each module updating

YML
---
Code::

  -
    !python {model: ir.config_parameter}: |
      SUPERUSER_ID = 1
      if not self.get_param(cr, SUPERUSER_ID, "ir_attachment.location"):
        self.set_param(cr, SUPERUSER_ID, "ir_attachment.location", "
        postgresql:lobject")
  
Prons:

* value is not overwrited if it already exists

Cons:

* record is not deleted on uninstalling
