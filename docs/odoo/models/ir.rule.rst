=========
 ir.rule
=========

Record rules are conditions that records must satisfy for an operation (create, read, write or delete) to be allowed. Example of a condition: *User can update Task that assigned to him*.

Group field defines for which group rule is applied. If Group is not specified, then rule is *global* and applied for all users.

Domain field defines conditions for records.

Boolean fields (read, write, create, delete) of ir.rule mean *Apply this rule for this kind of operation*. They do **not** mean *restrict access for this kind of operation*.

Checking access algorithm
=========================
To check either user has access for example to *read* a record, system do as following:

* Check access according to :doc:`ir.model.access <ir.model.access>` records. If it doesn't pass, then user **doesn't get** access

* Find and check global rules for the **model** and for *read* operation

  * if the record **doesn't satisfy** (doesn't fit to domain) for at least one of the global rules, then user **doesn't get** access

* Find and check non-global rules for the **model**, which *perm_read* equal True and ``groups`` that intersect with current user groups.

  * if there are no such rules, then user **get** access
  * if the record **satisfy** (fit to domain) for **at least one** of the non-global rules, then user **get** access
  * if the record **doesn't satisfy** for **all**  non-global rules, then user **doesn't get** access

See also:

* :doc:`Superuser rights <../../../dev/access/admin>`

Fields
======


.. code-block:: py

    name = fields.Char(index=True)
    active = fields.Boolean(default=True, help="If you uncheck the active field, it will disable the record rule without deleting it (if you delete a native record rule, it may be re-created when you reload the module).")
    model_id = fields.Many2one('ir.model', string='Object', index=True, required=True, ondelete="cascade")
    groups = fields.Many2many('res.groups', 'rule_group_rel', 'rule_group_id', 'group_id')
    domain_force = fields.Text(string='Domain')
    domain = fields.Binary(compute='_force_domain', string='Domain')
    perm_read = fields.Boolean(string='Apply for Read', default=True)
    perm_write = fields.Boolean(string='Apply for Write', default=True)
    perm_create = fields.Boolean(string='Apply for Create', default=True)
    perm_unlink = fields.Boolean(string='Apply for Delete', default=True)

