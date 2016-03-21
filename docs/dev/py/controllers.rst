Web controllers
===============
Send values to web page
-----------------------

If you need to transmit on rendering page some vars, you need to put that vars in dictionary and place it as second argument::

    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):
    ...
    values['order'] = order
    return request.website.render("website_sale.checkout", values)
