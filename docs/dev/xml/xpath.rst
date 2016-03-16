Xpath
=====

Add some attributes to tag
--------------------------
Code::

    <xpath expr="//div[@class='container oe_website_sale']" position="attributes">
        <attribute name="t-att-foobar">order.foobar and '1' or '0'</attribute>
    </xpath>

Important
^^^^^^^^^
Inside of ::

    <xpath expr="//div[@class='container oe_website_sale']" position="attributes">
        ...
    </xpath>

you can put **only**  ``<attribute name= `` and nothing more.

For example::

    <xpath expr="//div[@class='container oe_website_sale']" position="attributes">
        <attribute name="t-att-bill_enabled">not 'nobill' in website_sale_order.buy_way and '1' or '0'</attribute>
        <attribute name="t-att-ship_enabled">not 'noship' in website_sale_order.buy_way and '1' or '0'</attribute>
    </xpath>
