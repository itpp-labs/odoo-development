====================================
 Overview: "Transformed the method"
====================================

Quite often when porting a module from 8.0 to 9.0 there is a situation, when 8.0 is a object, but there is no 9.0. And it is not clear - it is outdated and it was removed or it was renamed. In very advanced cases, an object can be renamed and changed almost beyond recognition.

To search you need to take several steps:

1. The default view that such an object exist, but it was renamed.

2. Look, what makes this object.

3. Search by name of methods that contains the given object, excluding common words (for example, init, start, destroy...).

4. If the result is not found that search by unique keywords which can be found by bringing the object.

5. If anything gave no results, then maybe the object is deleted as obsolete.

:doc:`Case <./cases/transformed_method>`

:doc:`Possible solution <./cases/answers/transformed_method>`
