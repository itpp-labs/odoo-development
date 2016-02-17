Dynamic records
===============

While :doc:`XML <../xml/index>`  allows you  create only *static* records, there is a way to create record dynamically. You need dynamic records, for example, to add support both for enterprise and community releases or to add some records to each company in database etc.

Here is the example from ``web_debranding`` module. To create records in ``ir.model.data`` we use name ``_web_debranding``, because otherwise odoo considers such records as ones, which were in xml files, but now deleted. It also means, that odoo will not delete such records on uninstallation, so we need to do it manually via ``uninstall_hook``.


.. contents::


python file
-----------

.. code-block:: python
    
    from openerp import SUPERUSER_ID, models, tools, api
    
    MODULE = '_web_debranding'
    
    class view(models.Model):
        _inherit = 'ir.ui.view'
    
        def _create_debranding_views(self, cr, uid):
    
            self._create_view(cr, uid, 'menu_secondary', 'web.menu_secondary', '''
            <xpath expr="//div[@class='oe_footer']" position="replace">
               <div class="oe_footer"></div>
           </xpath>''')
    
        def _create_view(self, cr, uid, name, inherit_id, arch, noupdate=False, type='qweb'):
            registry = self.pool
            view_id = registry['ir.model.data'].xmlid_to_res_id(cr, SUPERUSER_ID, "%s.%s" % (MODULE, name))
            if view_id:
                registry['ir.ui.view'].write(cr, SUPERUSER_ID, [view_id], {
                    'arch': arch,
                })
                return view_id
    
            try:
                view_id = registry['ir.ui.view'].create(cr, SUPERUSER_ID, {
                    'name': name,
                    'type': type,
                    'arch': arch,
                    'inherit_id': registry['ir.model.data'].xmlid_to_res_id(cr, SUPERUSER_ID, inherit_id, raise_if_not_found=True)
                })
            except:
                import traceback
                traceback.print_exc()
                return
            registry['ir.model.data'].create(cr, SUPERUSER_ID, {
                'name': name,
                'model': 'ir.ui.view',
                'module': MODULE,
                'res_id': view_id,
                'noupdate': noupdate,
            })
            return view_id


yaml file
---------

.. code-block:: yaml

    -
      !python {model: ir.ui.view}: |
        self._create_debranding_views(cr, uid)

__openerp__.py
--------------

.. code-block:: python

    'uninstall_hook': 'uninstall_hook',
    'data': [
        'path/to/file.yml'
    ]

__init__.py
--------------

.. code-block:: python

    from openerp import SUPERUSER_ID
    
    MODULE = '_web_debranding'
    def uninstall_hook(cr, registry):
        registry['ir.model.data']._module_data_uninstall(cr, SUPERUSER_ID, [MODULE])
