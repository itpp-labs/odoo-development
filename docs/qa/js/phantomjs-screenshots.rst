================================
 Screenshots in PhantomJS tests
================================

Open file ``odoo/tests/phantomtest.js`` and after the line

.. code-block:: js

    console.log("PhantomTest.run: execution launched, waiting for console.log('ok')...");

add following

.. code-block:: js

                    i=1;
                    setInterval(function(){
                        self.page.render('/tmp/phantomjs-'+i+'.png');
                        i++;
                    }, 1000);

It will create screenshot every 1 second (you can update it if needed)
