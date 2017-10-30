ir.cron
=======


**在Odoo中创建自动化操作**


定时任务是一些可以在指定时间内自动运行的自动化操作，它们可以做很多事情。它们能在无人工介入的情况下自动执行数据库操作。在Odoo中创建定时任务十分简单：在表 ``ir.cron`` 中插入一行记录，Odoo就会按定义的参数自动执行。


**1. 创建模型和方法.**


.. code-block:: shell

        class model_name(models.Model):
            _name = "model.name"
            
	    # 字段定义...
	    
            def method_name(self, cr, uid, context=None): # 模型的方法
                # 你的其他代码

**2. 创建自动化操作**

    `如果在Odoo向导中创建的新模块，你应该在 <你的模块>/data/ 目录下增加一个XML文件并把自动化操作的代码增加到该文件。`

一个需要注意的地方就是自动化模块必须定义在一个 noupdate XML标签中，这样在更新模块时不会更新这个自动化操作的参数。

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
            	<field name="doal">1</field>
            	<!--<field name="nextcall" >2016-12-31 23:59:59</field>--> 
            	<field name="model" eval="'model.name '" />
            	<field name="function" eval="'method_name '" />
            	<field name="args" eval="" />
		<!--<field name="priority" eval="5" />--> 
            </record>
        </data>
    </openerp>

首先你会注意到在data标签中有个属性``noupdate="1"``, 它告诉Odoo在更新模块时不要更新此标签下的代码。

.. code-block:: xml

    <record id="unique_name" model="ir.cron">

id是这个自动化操作的唯一标识。称之为 ("ir.cron") 的是Odoo专门为自动化操作定义的模型，该模型中包含所有自动化操作，并且必须且只能这样指定。

.. code-block:: xml

    <field name="name">Name </field>

下一行就是自动化操作的名称。

.. code-block:: xml

    <field name="active" eval="True" />

用一个布尔值来指定当前自动化操作是否激活。

.. code-block:: xml

    <field name="user_id" ref="base.user_root"/>

指定一个执行自动化操作的用户，通常是base.user_root。

.. code-block:: xml

    <field name="interval_number">1</field>

指定自动化操作的执行频率（跟下面的interval_type配合使用）。

.. code-block:: xml

    <field name="interval_type">days</field>

间隔时间的单位.

间隔时间可选值为: ``minutes``, ``hours``, ``days``, ``weeks``, ``months``.

.. code-block:: xml

    <field name="numbercall">-1</field>

用一个正整数来指定该自动化操作最多执行次数，负值表示不限。

.. code-block:: xml

    <field name="doal">1</field>

doal指定在Odoo服务器重启之后是否执行那些因服务器停止而未被执行的自动化操作。

.. code-block:: xml

    <field name="nextcall" >2016-12-31 23:59:59</field> <!-- notice the date/time format -->

指定该自动化操作下一次执行时间

.. code-block:: xml

    <field name="model" eval="'model.name '" />

``model`` 指定在哪个模型上执行自动化操作。

.. code-block:: xml

    <field name="function" eval="'method_name '" />

指定自动化操作要执行的目标方法名称。

.. code-block:: xml

    <field name="args" eval="" />

传入被调用方法的参数。

.. code-block:: xml

    <field name="priority" eval="5" />

用一个正整数指定该自动化操作的优先级：0最高级，10最低级。


**默认值.**


+------------------+---------------------------------------------------------------+
| 名称             | 定义                                                           |
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
