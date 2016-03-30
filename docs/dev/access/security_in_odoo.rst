Security in Odoo
================

Resources:
 * http://odoo-docs.readthedocs.org/en/latest/04_security.html
 * https://www.odoo.com/documentation/9.0/howtos/backend.html#security
 * https://www.odoo.com/documentation/9.0/reference/security.html

Odoo is very flexible on the subject of security.
We can control what users can do and what they cannot on different levels.
Also we can control independently each of the four basic operations: read, write, create, unlink.
I.e. allow only read, allow only create, grant permission to create or delete only.

On fields/menu level we can:
 * hide fields or menus for some users and show them for others
 * make fields readonly for some users and make them editable for others
 * show different variants to pick on the Selection fields for different users

On the fields level of security ``res.users`` and ``res.groups`` models are used.
These models relate to each other as many2many.
This means that a user can be a member of many groups and one group can be assigned to many users.

One example of how we can hide menu in regard to current user's groups is the following.

.. image:: /images/access/hide_menu.png

On the picture above in ``Settings / Users`` we can see only ``Users`` menu.
We know that there should be ``Groups`` menu also.
Let Us see in ``./openerp/addons/base/res/res_users_view.xml`` on the point of how
menuitem can be hidden.

::

         <record id="action_res_groups" model="ir.actions.act_window">
            <field name="name">Groups</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">res.groups</field>
            <field name="view_type">form</field>
            <field name="help">A group is a set of functional areas that will be assigned to the
            user in order to give them access and rights to specific applications and tasks in
            the system. You can create custom groups or edit the ones existing by default
            in order to customize the view of the menu that users will be able to see. Whether
            they can have a read, write, create and delete access right can be managed from here.
         </field>
         </record>
         <menuitem action="action_res_groups" id="menu_action_res_groups" parent="base.menu_users"
         groups="base.group_no_one"/>

The ``groups`` attribute in the ``menuitem`` element shows us that only the members of ``base.group_no_one``
group can see the ``Groups`` menu item.
The ``base.group_no_one`` xmlid is defined in the ``./openerp/addons/base/security/base_security.xml as follows.

::

        <record model="res.groups" id="group_erp_manager">
            <field name="name">Access Rights</field>
        </record>
        <record model="res.groups" id="group_system">
            <field name="name">Settings</field>
            <field name="implied_ids" eval="[(4, ref('group_erp_manager'))]"/>
            <field name="users" eval="[(4, ref('base.user_root'))]"/>
        </record>

        <record model="res.groups" id="group_user">
            <field name="name">Employee</field>
            <field name="users" eval="[(4, ref('base.user_root'))]"/>
        </record>

        <record model="res.groups" id="group_multi_company">
            <field name="name">Multi Companies</field>
        </record>

        <record model="res.groups" id="group_multi_currency">
            <field name="name">Multi Currencies</field>
        </record>

        <record model="res.groups" id="group_no_one">
            <field name="name">Technical Features</field>
        </record>

        <record id="group_sale_salesman" model="res.groups">
            <field name="name">User</field>
        </record>
        <record id="group_sale_manager" model="res.groups">
            <field name="name">Manager</field>
            <field name="implied_ids" eval="[(4, ref('group_sale_salesman'))]"/>
        </record>


Here we can see the ``group_no_one`` along with the other base groups.
Note that ``group_no_one`` has ``Technical Features`` name.
Let us include our user in the ``Technical Features`` group. Since we
have no access to the ``Groups`` menu item, the only way we can do it
is from the ``Users`` menu item. See the picture below.

.. image:: /images/access/technical_features.png

Check the ``Technical Features`` box and reload odoo.
Now we can see the ``Groups`` menu item!

.. image:: /images/access/show_menu.png

From ``Settings / Users / Groups`` we can see a list of existing groups.
Here we also can assign users for groups.

Hide fields
-----------

In the ``./openerp/addons/base/res/res_users_view.xml`` we can see
the ``view_users_simple_form`` view. Note here that the ``company_id`` field
is visible only for members of the ``base.group_multi_company`` group.

::

        <!-- res.users -->
        <record id="view_users_simple_form" model="ir.ui.view">
            <field name="name">res.users.simplified.form</field>
            <field name="model">res.users</field>
            <field name="priority">1</field>
            <field name="arch" type="xml">
                <form string="Users">
                    <sheet>
                        <field name="id" invisible="1"/>
                        <div class="oe_form_box_info oe_text_center" style="margin-bottom: 10px" attrs="{'invisible': [('id', '>', 0)]}">
                            You are creating a new user. After saving, the user will receive an invite email containing a link to set its password.
                        </div>
                        <field name="image" widget='image' class="oe_avatar oe_left" options='{"preview_image": "image_medium"}'/>
                        <div class="oe_title">
                            <label for="name" class="oe_edit_only"/>
                            <h1><field name="name"/></h1>
                            <field name="email" invisible="1"/>
                            <label for="login" class="oe_edit_only" string="Email Address"/>
                            <h2>
                                <field name="login" on_change="on_change_login(login)"
                                        placeholder="email@yourcompany.com"/>
                            </h2>
                            <label for="company_id" class="oe_edit_only" groups="base.group_multi_company"/>
                            <field name="company_id" context="{'user_preference': 0}" groups="base.group_multi_company"/>
                        </div>
                        <group>
                            <label for="groups_id" string="Access Rights"
                                    attrs="{'invisible': [('id', '>', 0)]}"/>
                            <div attrs="{'invisible': [('id', '>', 0)]}">
                                <field name="groups_id" readonly="1" widget="many2many_tags" style="display: inline;"/> You will be able to define additional access rights by edi ting the newly created user under the Settings / Users menu.
                            </div>
                            <field name="phone"/>
                            <field name="mobile"/>
                            <field name="fax"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

Our current user is Administrator. By default he is not a member of the ``base.group_multicompany`` group.
That is why the ``company_id`` isn't visible for him on the form.

.. image:: /images/access/view_users_simple_form_before.png




Model records:
 * restrict access to specified subset of records in model

Model:
 * restrict access to all records of model

