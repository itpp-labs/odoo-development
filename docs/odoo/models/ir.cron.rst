ir.cron
=======


**Creating automated actions in Odoo**


Schedulers are automated actions that run automatically over a time period and can do a lot of things. They give the ability to execute actions database without needing manual interaction. Odoo makes running a background job easy: simply insert a record to ``ir.cron`` table and Odoo will execute it as defined.


**1. Creating the model and method of this model.**


.. code-block:: shell

        class model_name(models.Model):
            _name = "model.name"
            # fields
            def method_name(self, cr, uid, context=None): # method of this model
                # your code

**2. Creating the automated action**


    `If you want to build new modules in the guidelines from Odoo you should add the code for an automated action under yourDefaultModule/data/ in a separate XML file.`

An important thing to note with automated actions is that they should always be defined within a noupdate field since this shouldn’t be updated when you update your module.

.. code-block:: xml

    <openerp>
        <data noupdate="1">
            <record id="unique_name" model="ir.cron">
            	<field name="name">Name </field>
            	<field name="active" eval="True" />
            	<field name="user_id" ref="base.user_root" />
            	<field name="interval_number">1</field>
            	<field name="interval_type">days</field>
            	<field name="numbercall">-1</field>
            	<field name="doall">1</field>
            	<!--<field name="nextcall" >2016-12-31 23:59:59</field>--> 
            	<field name="model" eval="'model.name '" />
            	<field name="function" eval="'method_name '" />
            	<field name="args" eval="" />
		<!--<field name="priority" eval="5" />--> 
            </record>
        </data>
    </openerp>

The first thing you notice is the data ``noupdate="1"``, this is telling Odoo that all code within this tag shouldn’t be updated when you update your module.

.. code-block:: xml

    <record id="unique_name" model="ir.cron">

The id is an unique identifier for Odoo to know what record is linked to which id. The model called ("ir.cron") is the model specifically made by Odoo for all automated actions. This model contains all automated actions and should always be specified.

.. code-block:: xml

    <field name="name">Name </field>

The next line is the name. 

.. code-block:: xml

    <field name="active" eval="True" />

Boolean value indicating whether the cron job is active or not.

.. code-block:: xml

    <field name="user_id" ref="base.user_root"/>

This user id is referring to a specific user, in most cases this will be base.user_root.

.. code-block:: xml

    <field name="interval_number">1</field>

Number of times the scheduler is to be called based on the "interval_type" 

.. code-block:: xml

    <field name="interval_type">days</field>

Interval Unit.

It should be one value for the list: ``minutes``, ``hours``, ``days``, ``weeks``, ``months``.

.. code-block:: xml

    <field name="numbercall">-1</field>

An integer value specifying how many times the job is executed. A negative value means no limit.

.. code-block:: xml

    <field name="doall">1</field>

A boolean value indicating whether missed occurrences should be executed when the server restarts.

.. code-block:: xml

    <field name="nextcall" >2016-12-31 23:59:59</field> <!-- notice the date/time format -->

Next planned execution date for this job.

.. code-block:: xml

    <field name="model" eval="'model.name '" />

The field ``model`` specifies on which model the automated action should be called.

.. code-block:: xml

    <field name="function" eval="'method_name '" />

Name of the method to be called when this job is processed.

.. code-block:: xml

    <field name="args" eval="" />

The arguments to be passed to the method.

.. code-block:: xml

    <field name="priority" eval="5" />

The priority of the job, as an integer: 0 means higher priority, 10 means lower priority.


**Defaults.**


+------------------+---------------------------------------------------------------+
| Name             | Definition                                                    |
+==================+===============================================================+
| nextcall	   | ``lambda *a: time.strftime(DEFAULT_SERVER_DATETIME_FORMAT``   |
+------------------+---------------------------------------------------------------+
| priority         | 5                                                             |
+------------------+---------------------------------------------------------------+
| user_id          | ``lambda obj,cr,uid,context: uid``                            |
+------------------+---------------------------------------------------------------+
| interval_number  | 1                                                             |
+------------------+---------------------------------------------------------------+
| interval_type    | months                                                        |
+------------------+---------------------------------------------------------------+
| numbercall       | 1                                                             |
+------------------+---------------------------------------------------------------+
| active           | 1                                                             |
+------------------+---------------------------------------------------------------+
| doall            | 1                                                             |
+------------------+---------------------------------------------------------------+
