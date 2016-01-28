Short notes
=======
Pull request from console
------------------------------------
Yes it possible! Try this manual: https://github.com/github/hub
Than in console::

 alias git=hub

And pull request::

 git pull-request upstream

Nessesary to add some header for pull request. Save it. If everything is ok you will got link to your pull request.

Odoo XML
--------------

Create record of model::

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