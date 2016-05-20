============
 RST format
============


Document Title / Subtitle
=========================

The title of the whole document is distinct from section titles and
may be formatted somewhat differently (e.g. the HTML writer by default
shows it as a centered heading).

To indicate the document title in reStructuredText, use a unique adornment
style at the beginning of the document.  To indicate the document subtitle,
use another unique adornment style immediately after the document title.  For
example::

    ================
     Document Title
    ================
    ----------
     Subtitle
    ----------

    Section Title
    =============

    ...

Note that "Document Title" and "Section Title" above both use equals
signs, but are distict and unrelated styles.  The text of
overline-and-underlined titles (but not underlined-only) may be inset
for aesthetics.


Sections
--------

* # with overline, for parts
* \*\  with overline, for chapters
* =, for sections
* -, for subsections
* ^, for subsubsections
* ", for paragraphs

Code block
---------------
Enter double colon (\::\)  and then empty line and then at least one space and finaly you can enter your code.

Also you can use ``inplace code reference`` by using \``\  \``\.

Selection
=========
* ``**bold**``
* ``*italic*``
* ````code````

Lists
=====
* \*\  - not numerated
* \#.\  - numerated
* 1,2,3, ... - numerated 


Links
=====

* internal link::

  :doc:`Link Text<../relative/path/to/article>`

* external link:: 
  
  `Link Text <https://google.com/>`_

More documentations
===================

* http://docutils.sourceforge.net/docs/user/rst/quickref.html
