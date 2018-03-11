Python decorators
=================
Original article
----------------
http://odoo-new-api-guide-line.readthedocs.org/en/latest/decorator.html

@api.one
--------
api.one is meant to be used when method is called only on one record. It makes sure, that there are no multiple records when calling method with api.one decorator. Let say you got record partner =  res.partner(1,). It is only one record and there is method for example (in res.partner)::

  @api.one
  def get_name(self):
    return self.name #self here means one record

calling it like this works::

  partner.get_name()

But if there would be more records, like:: 

  partners = res.partner(1, 2,)

calling it, would raise Warning, telling you that you can only call it on one record.


@api.multi
----------

something. For example::

  @api.multi
  def get_partner_names(self):
    names = []
    for rec in self:
    names.append(rec.name)
    return ', '.join(names)

And api.model is considered to be used when you need to do something with model itself and don't need to modify/check some exact model's record/records. For example there could be method that returns some meta info about model's structure or some helper methods, etc. Also in documentation it is said that this api is good to use when migrating from old api, because it "politely" converts code to new api. Also in my own experience, if you need method to return something, model decorator is good for it. api.one returns empty list, so it might lead to unexpected behavior when using api.one on method when it is supposed to return something.
