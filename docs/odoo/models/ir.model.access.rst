=================
 ir.model.access
=================

Defines access to a whole model.

Each access control has a model to which it grants permissions, the
permissions it grants and optionally a group.

Access controls are additive, for a given model a user has access all
permissions granted to any of its groups: if the user belongs to one group
which allows writing and another which allows deleting, they can both write
and delete.

If no group is specified, the access control applies to all users, otherwise
it only applies to the members of the given group.

Available permissions are creation (``perm_create``), searching and reading
(``perm_read``), updating existing records (``perm_write``) and deleting
existing records (``perm_unlink``)

When there is no access records for a given model and a permission (e.g. *read*), then only Superuser has the permision.

See also:

* :doc:`Superuser rights <../../../dev/access/admin>`
* :doc:`ir.rule <ir.rule>`

Fields
======

.. code-block:: py

    name = fields.Char(required=True, index=True)
    active = fields.Boolean(default=True, help='If you uncheck the active field, it will disable the ACL without deleting it (if you delete a native ACL, it will be re-created when you reload the module).')
    model_id = fields.Many2one('ir.model', string='Object', required=True, domain=[('transient', '=', False)], index=True, ondelete='cascade')
    group_id = fields.Many2one('res.groups', string='Group', ondelete='cascade', index=True)
    perm_read = fields.Boolean(string='Read Access')
    perm_write = fields.Boolean(string='Write Access')
    perm_create = fields.Boolean(string='Create Access')
    perm_unlink = fields.Boolean(string='Delete Access')
