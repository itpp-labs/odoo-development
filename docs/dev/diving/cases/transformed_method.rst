=================================
 Case: "Transformed the method"
=================================

Context
=======

When porting module mail_move_message in the file static/src/js/mail_move_message.js there is a method `session.web.form.FormOpenPopup(this) <https://github.com/yelizariev/mail-addons/blob/9.0/mail_move_message/static/src/js/mail_move_message.js#L64>`_.

Problem
=======

In 9.0 not found such object. What object would be the analogue of the object? What you need to do to find this object?

Solution
========

:doc:`Possible solution <./answers/transformed_method>`
