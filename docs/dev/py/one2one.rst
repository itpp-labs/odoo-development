=======================
 One2one field in odoo
=======================

Odoo ORM doesn't support ``One2one`` fields, but you can do them manually. In the example below we make one2one relationship between models ``fleet.vehicle`` and ``account.asset.asset``.

In short, you set normal ``Mane2one`` field (``vehicle_id`` in the example) in a one model (doesn't really matter which of the models you choose) and corresponding ``One2many`` field (``asset_ids`` in the example) in another model. Then we add virtural ``Many2one`` field (``asset_id`` in the example) with attributes ``compute`` and ``inverse``.

.. code-block:: python

    class Fleet(models.Model):

    _inherit = 'fleet.vehicle'
    ...
    asset_id = fields.Many2one('account.asset.asset', compute='compute_asset', inverse='asset_inverse')
    asset_ids = fields.One2many('account.asset.asset', 'vehicle_id')

    @api.one
    @api.depends('asset_ids')
    def compute_asset(self):
        if len(self.asset_ids) > 0:
            self.asset_id = self.asset_ids[0]

    @api.one
    def asset_inverse(self):
        if len(self.asset_ids) > 0:
            # delete previous reference
            asset = self.env['account.asset.asset'].browse(self.asset_ids[0].id)
            asset.vehicle_id = False
        # set new reference
        self.asset_id.vehicle_id = self


    class Asset(models.Model):
    _inherit = 'account.asset.asset'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')


TODO: replace ``@api.one`` to ``@api.multi``
