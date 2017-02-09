mail.message
============


**Message Subtypes in Odoo**


Most of the time in Odoo multiple users work upon one particular record or document like sale order,Invoice ,Tasks etc. In such scenarios,it becomes extremely important to track changes done by every individual against that document. It helps management to find any possible reason in case of any issue occurs. Odoo provides this feature to great extent with the help of OpenChatter Integration.

Consider a scenario where multiple users are working in a single project.Various parameters for that project are already configured like deadline,Initially Planned Hours etc. Now one of the user changes the value of Planned Hours. So now it is important to know which user has changed it and what was the previous value. We can track it by creating message subtypes in Odoo as following.

It needs to be defined in XML which will have following syntax.

.. code-block:: xml

    <record id="mt_task_planned_hours" model="mail.message.subtype">
        <field name="name">Task planned hours changed</field>
        <field name="res_model">project.task</field>
        <field name="default" eval="True"/>
        <field name="description">Task planned hours changed</field>
    </record>

Users can also have a mail.message.subtype that depends on an other to act through a relation field. For the planned hours, we can have following syntax for it.

.. code-block:: xml

    <record id="mt_task_planned_hours_change" model="mail.message.subtype">
        <field name="name">Task planned hours changed</field>
        <field name="sequence">10</field>
        <field name="res_model">projec.project</field>
        <field name="parent_id" eval="ref('mt_task_planned_hours')"/>
        <field name="relation_field">project_id</field>
    </record>

Odoo provide feature to track various events related with one particular document with the help of _track attribute. If we inherit mail.thread object then with the help of _track attribute, user can sent notification also to keep aware others about changes happening against this particular document. The syntax can be as follow.

.. code-block:: shell

    _track = {
        'planned_hours': {
        'module_name.mt_task_planned_hours': lambda self, cr, uid, obj, ctx=None: obj.planned_hours,
    },


In order to track changes related with any field,Odoo provides an attribute named as track_visibility.It has to be defined at field level which has below syntax. 

.. code-block:: shell

    planned_hours = fields.Float(string = 'Initially Planned Hours', track_visibility='onchange', help='Estimated time to do the task, it is project manager when the task is in draft state.')

Hence, it is easy to track the changes done so far against any particular document by different users.
