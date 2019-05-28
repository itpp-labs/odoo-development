One2one organization
====================

You need two records of different models have referred to each other.

Changing the reference in one place requires also changing it in another.

Follow this code:

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
        new_asset = self.env['account.asset.asset'].browse(self.asset_id.id)
        if len(self.asset_ids) > 0:
            asset = self.env['account.asset.asset'].browse(self.asset_ids[0].id)
            asset.vehicle_id = False
        new_asset.vehicle_id = self


    class Asset(models.Model):
    _inherit = 'account.asset.asset'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')


