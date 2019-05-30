===========================
 Adding ``js`` file to POS
===========================

Adding **javascript file** opens a new set of possibilities in Odoo.

Let take the example of the ``POS Debt & Credit notebook`` `module: <https://github.com/it-projects-llc/pos-addons/blob/15a6853768a888bb7c3fbfd3690ce0cb7537ff3e/pos_debt_notebook/data.xml#L16-L20::>`__

.. code-block:: XML

    <template id="assets" inherit_id="point_of_sale.assets">
      <xpath expr="." position="inside">
      <script type="text/javascript" src="/pos_debt_notebook/static/src/js/pos.js" />
        <link rel="stylesheet" href="/pos_debt_notebook/static/src/css/pos.css" id="pos_debt_notebook-stylesheet" />
      </xpath>
    </template>
