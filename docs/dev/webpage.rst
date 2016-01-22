Web page
========

**Common**


Open a new project:

.. code-block:: shell

    ./odoo.py scaffold newpage addons
	
Add  ``website`` as a dependency to ``newpage``: 

.. code-block:: shell

    'depends': '[website]'
	
then add the website=True flag on the controller, this sets up a few new variables 
on the request object and allows using the website layout in our template.

**Creating pages**

**1 way**

Write the following code in ``controllers.py``: 

.. code-block:: shell

    from openerp import http
        classNewPage(http.Controller):
	    @http.route('/new-page/',auth='public', website=True)
	    def index(self,**kw):
                return http.request.render('newpage.index')
			
The new web page will appear by adding - ``/new-page/``
``http.request.render('newpage.index')`` – downloading a tamplate for a new page 

A pattern ``templates.xml``

.. code-block:: shell

    <openerp>
	<data>
	    <templateid="index">
		<t t-call="website.layout">
	            <t t-set="title">New page</t>
			<div class="oe_structure">
			    <div class="container">
				<h1>My first web page</h1>
				<p>Hello, world!</p>
			    </div>
			</div>
		    </t>
	    </template>
	</data>
    </openerp>
	
``website.layout`` means that the elements of pattern website are used.

After restarting the server while updating the module (in order to update the manifest and template) 
access http://localhost:8069/new-page/. You will see a new page with a title *'My first web page'* and 
with text *'Hello, world!'* 

**2 way**

Write in pattern the following:

.. code-block:: shell

    <template name="Services page" id="website.services" page="True">
        <t t-call="website.layout">
	    <div id="wrap">
		<div class="container">
		    <h1>Our Services</h1>
		    <ul class="services">
		        <li>Cloud Hosting</li>
	  	        <li>Support</li>
		        <li>Unlimited space</li>
		    </ul>
	        </div>
	    </div>
        </t>
    </template>
	
``page="True"`` creates a page as follows below: 
http://localhost:8069/page/services/

If add in ``view.xml``: 

.. code-block:: shell

    <record id="services_page_link" model="website.menu">
	<field name="name">Services</field>
	<field name="url">/page/services</field>
	<field name="parent_id" ref="website.main_menu" />
	<field name="sequence" type="int">99</field>
    </record>

This code will add a link to the main menu.
