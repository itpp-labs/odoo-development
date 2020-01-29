=======================================
 How to overwrite built-in translation
=======================================

You may need to change built-in translation via a module. You could be done via data xml files by calling ``_set_ids`` method. For example, for menus it could look as following:

.. code-block:: xml

    <function
        model="ir.translation"
        name="_set_ids"
        eval="('ir.ui.menu,name', 'model', 'ru_RU', [ref('project.menu_main_pm')], 'Проекты Компании', 'Project')"/>

