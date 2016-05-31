========================
 Transformed the method
========================

Context
=======

Quite often when porting a module from 8.0 to 9.0 there is a situation, when 8.0 is a object, but there is no 9.0. And it is not clear - it is outdated and it was removed or it was renamed. In very advanced cases, an object can be renamed and changed almost beyond recognition.

For example, when porting module mail_move_message in the file static/src/js/mail_move_message.js there is a method `session.web.form.FormOpenPopup(this) <https://github.com/yelizariev/mail-addons/blob/9.0/mail_move_message/static/src/js/mail_move_message.js#L64>`_.

To search you need to take several steps:

1. The default view that such an object exist, but it was renamed.

2. Look, what makes this object.

3. Search by name of methods that contains the given object, excluding common words (for example, init, start, destroy...).

4. If the result is not found that search by unique keywords which can be found by bringing the object.

5. If anything gave no results, then maybe the object is deleted as obsolete.


Problem
=======

In 9.0 not found such object. What object would be the analogue of the object? What you need to do to find this object?

Solution
========

:doc:`Possible solution <./answers/transformed_method>`
