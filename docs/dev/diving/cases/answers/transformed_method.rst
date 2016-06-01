============================================
 Solution for case "Transformed the method"
============================================

First consider what makes the object `session.web.form.FormOpenPopup() <https://github.com/yelizariev/mail-addons/blob/9.0/mail_move_message/static/src/js/mail_move_message.js#L64>`_.

.. code-block:: js

    var pop = new session.web.form.FormOpenPopup(this);
    pop.show_element(
        related_field.field.relation,
        false,
        context,
        {
            title: _t("Create new record"),
        }
    );
    pop.on('closed', self, function () {
        self.force_disabled = false;
        self.check_disable();
    });
    pop.on('create_completed', self, function(id) {
        related_field.set_value(id);
        if(self.field_manager.fields['filter_by_partner']) {
            self.field_manager.fields['filter_by_partner'].set_value(true);
        }
    });

Assume, in this case, that we got nothing.

Then we try search by methods of `object <https://github.com/odoo/odoo/blob/8.0/addons/web/static/src/js/view_form.js#L5373>`_. In this case, **init_popup**, **display_popup**, **init_dataset** and **setup_form_view**. Successfully. Method init_dataset is in object `FormViewDialog <https://github.com/odoo/odoo/blob/9.0/addons/web/static/src/js/views/form_common.js#L850>`_. The object behaves similar to the one that we need.

If this step did not give us anything, that we can try search by unique keywords.
For example, in this case, we see arguments of pop.on() methods: 'closed' and 'created_completed'.

Например, в данном случае мы видим слова, переданные в метод pop.on() в качестве аргументов: **'closed'** и **'create_completed'**. The word 'closed' does not suit us, as it can occur often enough. But the word 'create_completed' rare and we can serch by it. And now we again find the object `FormViewDialog <https://github.com/odoo/odoo/blob/9.0/addons/web/static/src/js/views/form_common.js#L850>`_.

:doc:`Source Diving Index <../../index>`
