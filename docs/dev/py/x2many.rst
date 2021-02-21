x2many values filling
=====================

To fill or manipulate one2many or many2many field with according values (records) you need to use special command as says below.


Odoo 15.0+
----------

First import ``fields``

.. code-block:: python

    from odoo import fields
    # or Command directly:
    # from odoo.fields import Command

Then assign list of following commands to a x2many field:

* ``fields.Command.create(values)``
* ``fields.Command.update(id, values)``
* ``fields.Command.delete(id)``
* ``fields.Command.unlink(id)``
* ``fields.Command.link(id)``
* ``fields.Command.clear()``
* ``fields.Command.set(ids)``

Based on https://github.com/odoo/odoo/blob/84f89d6ff887e750ea79656328362333cfce27fd/odoo/fields.py#L2868-L2982

Odoo 14.0-
----------

This format is a list of triplets executed sequentially, where each triplet is a command to execute on the set of records. Not all
commands apply in all situations. Possible commands are:

 * **(0, _, values)** adds a new record created from the provided **value** dict.
 * **(1, id, values)** updates an existing record of id **id** with the values in **values**. Can not be used in `~.create`.
 * **(2, id, _)** removes the record of id **id** from the set, then deletes it (from the database). Can not be used in `~.create`.
 * **(3, id, _)** removes the record of id **id** from the set, but does not delete it. Can not be used on `~openerp.fields.One2many`. Can not be used in `~.create`.
 * **(4, id, _)** adds an existing record of id **id** to the set. Can not be used on `~openerp.fields.One2many`.
 * **(5, _, _)** removes all records from the set, equivalent to using the command **3** on every record explicitly. Can not be used on `~openerp.fields.One2many`. Can not be used in `~.create`.
 * **(6, _, ids)** replaces all existing records in the set by the **ids** list, equivalent to using the command **5** followed by a command **4** for each **id** in **ids**. Can not be used on `~openerp.fields.One2many`.

.. note:: Values marked as **_** in the list above are ignored and can be anything, generally **0** or **False**.

Based on https://github.com/odoo/odoo/blob/14.0/odoo/models.py
