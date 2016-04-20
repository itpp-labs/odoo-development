ir.actions.todo
===============

The model is used for executing actions (records in the "ir.actions.act_window" model).
The model allows to set conditions and sequence of appearance of wizards. Also you can specify a regular
interface window but only as last action.
Code::

        <record id="sce.initial_setup" model="ir.actions.todo">
            <field name="action_id" ref="action_initial_setup"/>
            <field name="state">open</field>
            <field name="sequence">1</field>
            <field name="type">automatic</field>
        </record>

The startup type can be one of the following:

* manual: Launched manually.
* automatic: Runs whenever the system is reconfigured. The launch takes place either after install/upgrade any module
  or after calling the "execute" method in the "res.config" model.
* once: After having been launched manually, it sets automatically to Done.
