Xpath
=====

Add some attributes to node
---------------------------

Code::

    <xpath expr="//some/xpath" position="attributes">
        <attribute name="some_field">
    </xpath>

Qweb expression::

    <attribute name="t-att-another_field">website.get_another_field_value()</attribute>

After rendering it becomes regular attribute::

    <.... another_field="value" ...>

Important
^^^^^^^^^
Inside of ::

    <xpath expr="//some/xpath" position="attributes">
        ...
    </xpath>

you can put **only**  ``<attribute name= `` and nothing more.
