x2many values filling
=====================

To fill or manipulate one2many or many2many field with according values (records) you need to use special command as says below.

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

Based on https://github.com/odoo/odoo/blob/master/odoo/models.py
