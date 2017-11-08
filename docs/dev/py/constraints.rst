Model constraints
=================

Odoo provides two ways to set up automatically verified invariants:
`Python constraints <openerp.api.constrains>` and
`SQL constraints <openerp.models.Model._sql_constraints>`.

A Python constraint is defined as a method decorated with
`~openerp.api.constrains`, and invoked on a recordset. The decorator
specifies which fields are involved in the constraint, so that the constraint is
automatically evaluated when one of them is modified. The method is expected to
raise an exception if its invariant is not satisfied::

    from openerp.exceptions import ValidationError

    @api.constraints('age')
    def _check_something(self):
        for record in self:
            if record.age > 20:
                raise ValidationError("Your record is too old: %s" % record.age)
        # all records passed the test, don't return anything


SQL constraints are defined through the model attribute
`~openerp.models.Model._sql_constraints`. The latter is assigned to a list
of triples of strings ``(name, sql_definition, message)``, where ``name`` is a
valid SQL constraint name, ``sql_definition`` is a ``table_constraint_`` expression,
and ``message`` is the error message.
