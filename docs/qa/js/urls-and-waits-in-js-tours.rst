=================================
 How js tour works via phantomjs
=================================


The order is as following:

* OPEN *url_path* from **python** :doc:`phantom_js <phantom_js>` method
* WAIT *ready* condition (Truthy or Falsy) from **python** :doc:`phantom_js <phantom_js>` method
* OPEN *url* from :doc:`tour <../../description/js_tour>`'s options in **js** file 
* WAIT *wait_for* (deferred object) from :doc:`tour <../../description/js_tour>`'s options in **js** file
* DO first step from **js** :doc:`tour <../../description/js_tour>`

  * WAIT when *trigger* becomes visible
  * WAIT when *extra_trigger*  becomes visible (if *extra_trigger* is presented)
  * EXECUTE action (*run* or click on *trigger*)

* DO NEXT step

  * ...

* STOP Running when:

  * error happens:

    * thrown via ``raise``
    * reported via ``console.log('error', ...)``
    * reported via ``console.error(...)``, etc.
    * reported by tour system on **timeout** for initial *ready* condition. `Timeout value is 10 sec <https://github.com/odoo/odoo/blob/98f72ef/odoo/tests/phantomtest.js#L7-L8>`__ and `it cannot be changed <https://github.com/odoo/odoo/blob/98f72ef/odoo/tests/phantomtest.js#L118-L135>`__. The PR to odoo 12 to make it customizable: https://github.com/odoo/odoo/pull/24514
    * reported by tour system on step **timeout**.

  * ``'ok'`` is reported via ``console.log('ok')``

    * directly by code 
    * indirectly by tour system when all steps are done

  * **timeout** from **python** :doc:`phantom_js <phantom_js>` method is occured. Default is 60 sec
  
