Create record of model
======================

Create new record::

    <openerp>
        <data>
            <record id="demo_multi_session" model="pos.multi_session">
                <field name="name">multi session demo</field>
            </record>
        </data>
    openerp>

If model exist it will be modifyed.
Record creating in module it declareted. 
To change model created in another module add mule name before id::

    <openerp>
        <data>
            <record id="point_of_sale.pos_config_main" model="pos.config">
                <field name="multi_session_id" ref="demo_multi_session"/>
            </record>
        </data>
    openerp>