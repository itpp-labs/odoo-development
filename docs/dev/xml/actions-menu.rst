==============
 Actions Menu
==============

.. image:: ../../images/actions-menu.png

To add such button, you need to create ``ir.actions.act_window`` record with ``binding_model_id`` value.

`Example for Odoo 14.0+ <https://github.com/odoo/odoo/blob/45c9dc8e389908d32be076b3b49597a9dd305b5b/addons/crm_sms/views/crm_lead_views.xml#L17-L28>`__:

.. code-block:: xml

    <record id="crm_lead_act_window_sms_composer_multi" model="ir.actions.act_window">
        <field name="name">Send SMS Text Message</field>
        <field name="res_model">sms.composer</field>
        <field name="view_mode">form</field>
        <field name="target">new</field>
        <field name="context">{
            'default_composition_mode': 'comment',
            'default_res_id': active_id,
        }</field>
        <field name="binding_model_id" ref="model_crm_lead"/>
        <field name="binding_view_types">form</field>
    </record>

`Example for Odoo 13.0- <https://github.com/odoo/odoo/blob/2a7ec79c6a4563b608a4525ebccdea5978799caa/addons/crm_sms/views/crm_lead_views.xml#L17-L28>`__:

.. code-block:: xml

    <act_window id="crm_lead_act_window_sms_composer_multi"
        name="Send SMS Text Message"
        binding_model="crm.lead"
        res_model="sms.composer"
        binding_views="form"
        view_mode="form"
        target="new"
        context="{
            'default_composition_mode': 'comment',
            'default_res_id': active_id,
        }"
    />


See also https://www.odoo.com/documentation/master/howtos/backend.html#launching-wizards
