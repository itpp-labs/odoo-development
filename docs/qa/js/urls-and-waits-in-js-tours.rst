=================================
 How js tour works via phantomjs
=================================


The order is as following:

* OPEN *url_path* from python ``phantom_js`` method
* WAIT *ready* condition (Truthy or Falsy) from python ``phantom_js`` method
* OPEN *url* from tour's options in js file 
* WAIT *wait_for* (deferred object) from tour's options in js file
* DO first step from js tour

  * WAIT when *trigger* becomes visible
  * WAIT when *extra_trigger*  becomes visible (if extra_trigger* is presented)
  * EXECUTE action (*run* or click on *trigger*)

* DO NEXT step

  * ...

* STOP Running when:

  * error happens:

    * thrown via ``raise``
    * reported via ``console.log('error', ...)``
    * reported via ``console.error(...)``, etc.
    * reported by tour system if step takes more than 10 seconds (can be increased by value of *step_delay* in ``run`` js method)

  * ``'ok'`` is reported via ``console.log('ok')``

    * directly by code 
    * indirectly by tour system when all steps are done

  * timeout from python ``phantom_js`` method is occured (default is 60 sec)
  
