======================
``Group_id`` in views
======================

``groups_id`` in views (mostly in views that inherits other views) allows to specify for which group make those inheritance.

For example, if you need to add a button that will be available for managers only, make the following:

.. code-block:: XML

    <record id="fleet_vehicle_log_services_form_inherit_bos" model="ir.ui.view">
    <field name="name">fleet.vehicle.log.services.form.inherit.bos</field>
    <field name="model">fleet.vehicle.log.services</field>
    <field name="inherit_id" ref="fleet_vehicle_log_services_form_inherit_buttons"/>
    <field name="groups_id" eval="[(4, ref('fleet_booking.group_branch_officer'), 0)]"/>
    <field name="arch" type="xml">
        <data>
            <xpath expr="//button[@name='confirm']" position="attributes">
                <attribute name='attrs'>{'invisible': [('cost_subtype_in_branch', '=', False)]}</attribute>
            </xpath>
        </data>
    </field>
    </record>

If ``groups_id`` is omitted, then the update is applied for all users.