Inherit
=======

Collisions and priority
-----------------------

If two or more xml templates inherit same parent template they can have same priorities.
It may produce conflicts and unexpected behavior.
What you need is just set priority explicitly in your template::

    <template id="..." inherit_id="..." priority="8" ..>
            <xpath expr="..." position="...">
                 ...
            </xpath>
    </template>

    <!-- or -->
  
    <record id="..." model="ir.ui.view">
        ...
        <field name="inherit_id" ref="..."/>
        <field name="arch" type="xml">
            <xpath expr="..." position="...">
            </xpath>
        </field>
    </record>

Less priority means prior execution.

Default priority is 16.
