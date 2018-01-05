Fields
======

*Based on:* http://odoo-new-api-guide-line.readthedocs.io/en/latest/fields.html

.. contents::
   :local:


Now fields are class property: ::

    from openerp import models, fields


    class AModel(models.Model):

        _name = 'a_name'

        name = fields.Char(
            string="Name",                   # Optional label of the field
            compute="_compute_name_custom",  # Transform the fields in computed fields
            store=True,                      # If computed it will store the result
            select=True,                     # Force index on field
            readonly=True,                   # Field will be readonly in views
            inverse="_write_name"            # On update trigger
            required=True,                   # Mandatory field
            translate=True,                  # Translation enable
            help='blabla',                   # Help tooltip text
            company_dependent=True,          # Transform columns to ir.property
            search='_search_function'        # Custom search function mainly used with compute
        )

       # The string key is not mandatory
       # by default it wil use the property name Capitalized

       name = fields.Char()  #  Valid definition


.. _fields_inherit:

Field inheritance
------------------

One of the new features of the API is to be able to change only one attribute of the field: ::

   name = fields.Char(string='New Value')

Field types
-----------

Boolean
#######

Boolean type field: ::

    abool = fields.Boolean()

Char
####

Store string with variable len.: ::

    achar = fields.Char()


Specific options:

 * size: data will be trimmed to specified size
 * translate: field can be translated

Text
####

Used to store long text.: ::

    atext = fields.Text()


Specific options:

 * translate: field can be translated

HTML
####

Used to store HTML, provides an HTML widget.: ::

    anhtml = fields.Html()


Specific options:

 * translate: field can be translated


Integer
#######

Store integer value. No NULL value support. If value is not set it returns 0: ::

    anint = fields.Integer()

Float
#####

Store float value. No NULL value support. If value is not set it returns 0.0
If digits option is set it will use numeric type: ::


    afloat = fields.Float()
    afloat = fields.Float(digits=(32, 32))
    afloat = fields.Float(digits=lambda cr: (32, 32))

Specific options:

  * digits: force use of numeric type on database. Parameter can be a tuple (int len, float len) or a callable that return a tuple and take a cursor as parameter

Date
####

Store date.
The field provides some helpers:

  * ``context_today`` returns current day date string based on tz
  * ``today`` returns current system date string
  * ``from_string`` returns datetime.date() from string
  * ``to_string`` returns date string from datetime.date

: ::

    >>> from openerp import fields

    >>> adate = fields.Date()
    >>> fields.Date.today()
    '2014-06-15'
    >>> fields.Date.context_today(self)
    '2014-06-15'
    >>> fields.Date.context_today(self, timestamp=datetime.datetime.now())
    '2014-06-15'
    >>> fields.Date.from_string(fields.Date.today())
    datetime.datetime(2014, 6, 15, 19, 32, 17)
    >>> fields.Date.to_string(datetime.datetime.today())
    '2014-06-15'

DateTime
########

Store datetime.
The field provide some helper:

  * ``context_timestamp`` returns current day date string based on tz
  * ``now`` returns current system date string
  * ``from_string`` returns datetime.date() from string
  * ``to_string`` returns date string from datetime.date

: ::

    >>> fields.Datetime.context_timestamp(self, timestamp=datetime.datetime.now())
    datetime.datetime(2014, 6, 15, 21, 26, 1, 248354, tzinfo=<DstTzInfo 'Europe/Brussels' CEST+2:00:00 DST>)
    >>> fields.Datetime.now()
    '2014-06-15 19:26:13'
    >>> fields.Datetime.from_string(fields.Datetime.now())
    datetime.datetime(2014, 6, 15, 19, 32, 17)
    >>> fields.Datetime.to_string(datetime.datetime.now())
    '2014-06-15 19:26:13'


Binary
######

Store file encoded in base64 in bytea column: ::

    abin = fields.Binary()

Selection
#########

Store text in database but propose a selection widget.
It induces no selection constraint in database.
Selection must be set as a list of tuples or a callable that returns a list of tuples: ::

    aselection = fields.Selection([('a', 'A')])
    aselection = fields.Selection(selection=[('a', 'A')])
    aselection = fields.Selection(selection='a_function_name')

Specific options:

  * selection: a list of tuple or a callable name that take recordset as input
  * size: the option size=1 is mandatory when using indexes that are integers, not strings

When extending a model, if you want to add possible values to a selection field,
you may use the `selection_add` keyword argument::

   class SomeModel(models.Model):
       _inherits = 'some.model'
       type = fields.Selection(selection_add=[('b', 'B'), ('c', 'C')])

Reference
#########

Store an arbitrary reference to a model and a row: ::

    aref = fields.Reference([('model_name', 'String')])
    aref = fields.Reference(selection=[('model_name', 'String')])
    aref = fields.Reference(selection='a_function_name')

Specific options:

  * selection: a list of tuple or a callable name that take recordset as input


Many2one
########

Store a relation against a co-model: ::

    arel_id = fields.Many2one('res.users')
    arel_id = fields.Many2one(comodel_name='res.users')
    an_other_rel_id = fields.Many2one(comodel_name='res.partner', delegate=True)


Specific options:

  * comodel_name: name of the opposite model
  * delegate: set it to ``True`` to make fields of the target model accessible from the current model (corresponds to ``_inherits``)

One2many
########

Store a relation against many rows of co-model: ::

    arel_ids = fields.One2many('res.users', 'rel_id')
    arel_ids = fields.One2many(comodel_name='res.users', inverse_name='rel_id')

Specific options:

  * comodel_name: name of the opposite model
  * inverse_name: relational column of the opposite model


Many2many
#########

Store a relation against many2many rows of co-model: ::

    arel_ids = fields.Many2many('res.users')
    arel_ids = fields.Many2many(comodel_name='res.users',
                                relation='table_name',
                                column1='col_name',
                                column2='other_col_name')


Specific options:

  * comodel_name: name of the opposite model
  * relation: relational table name
  * columns1: relational table left column name (reference to record in current table)
  * columns2: relational table right column name (reference to record in *comodel_name* table)


Name Conflicts
--------------

.. note::
   fields and method name can conflict.

When you call a record as a dict it will force to look on the columns.


Fields Defaults
---------------

Default is now a keyword of a field:

You can attribute it a value or a function

::

   name = fields.Char(default='A name')
   # or
   name = fields.Char(default=a_fun)

   #...
   def a_fun(self):
      return self.do_something()

Using a fun will force you to define function before fields definition.

Note. Default value cannot depend on values of other fields of a record, i.e. you cannot read other fields via ``self`` in the function.

Computed Fields
---------------
There is no more direct creation of fields.function.

Instead you add a ``compute`` kwarg. The value is the name of the function as a string or a function.
This allows to have fields definition atop of class: ::

    class AModel(models.Model):
        _name = 'a_name'

        computed_total = fields.Float(compute='compute_total')

        def compute_total(self):
            ...
            self.computed_total = x


The function can be void.
It should modify record property in order to be written to the cache: ::

  self.name = new_value

Be aware that this assignation will trigger a write into the database.
If you need to do bulk change or must be careful about performance,
you should do classic call to write

To provide a search function on a non stored computed field
you have to add a ``search`` kwarg on the field. The value is the name of the function
as a string or a reference to a previously defined method. The function takes the second
and third member of a domain tuple and returns a domain itself ::

        def search_total(self, operator, operand):
	    ...
            return domain  # e.g. [('id', 'in', ids)] 

Inverse
-------

The inverse key allows to trigger call of the decorated function
when the field is written/"created"


Multi Fields
------------
To have one function that compute multiple values: ::

    @api.multi
    @api.depends('field.relation', 'an_otherfield.relation')
    def _amount(self):
        for x in self:
            x.total = an_algo
            x.untaxed = an_algo


Related Field
-------------

There is not anymore ``fields.related`` fields.

Instead you just set the name argument related to your model: ::

  participant_nick = fields.Char(string='Nick name',
                                 related='partner_id.name')

The ``type`` kwarg is not needed anymore.

Setting the ``store`` kwarg will automatically store the value in database.
With new API the value of the related field will be automatically
updated, sweet. ::

  participant_nick = fields.Char(string='Nick name',
                                 store=True,
                                 related='partner_id.name')

.. note::
   When updating any related field not all
   translations of related field are translated if field
   is stored!!

Chained related fields modification will trigger invalidation of the cache
for all elements of the chain.


Property Field
--------------

There is some use cases where value of the field must change depending of
the current company.

To activate such behavior you can now use the `company_dependent` option.

A notable evolution in new API is that "property fields" are now searchable.

WIP copyable option
-------------------

There is a dev running that will prevent to redefine copy by simply
setting a copy option on fields: ::

  copy=False  # !! WIP to prevent redefine copy
