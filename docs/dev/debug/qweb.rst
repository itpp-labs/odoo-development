QWeb
====

The javascript QWeb implementation provides a few debugging hooks:

``t-log``
    takes an expression parameter, evaluates the expression during rendering
    and logs its result with ``console.log``::

        <t t-set="foo" t-value="42"/>
        <t t-log="foo"/>

    will print ``42`` to the console
``t-debug``
    triggers a debugger breakpoint during template rendering::

        <t t-if="a_test">
            <t t-debug="">
        </t>

    will stop execution if debugging is active (exact condition depend on the
    browser and its development tools)
``t-js``
    the node's body is javascript code executed during template rendering.
    Takes a ``context`` parameter, which is the name under which the rendering
    context will be available in the ``t-js``'s body::

        <t t-set="foo" t-value="42"/>
        <t t-js="ctx">
            console.log("Foo is", ctx.foo);
        </t>

`Source <https://www.odoo.com/documentation/8.0/reference/qweb.html#id4>`_
