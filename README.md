[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Source of https://odoo-development.readthedocs.io/ website

# How to contribute

## Initialization

* Fork this repo
* Clone to your machine
* Install dependencies:

      sudo pip install sphinx sphinx-autobuild
      sudo pip install sphinx_rtd_theme

## Contribution

* Edit files in the repo. Check documentations:

  * http://www.sphinx-doc.org/en/stable/rest.html
  * http://www.sphinx-doc.org/en/stable/domains.html
  * http://www.sphinx-doc.org/en/stable/markup/index.html
  * [images.md](images.md)

* Try it out:

      cd /path/to/odoo-development/docs
      make html

      # (check warningn and errors in compilation logs and fix them if needed)

      # open result
      google-chrome _build/html/index.html

* Make commits, push, create Pull Request

# Translation

ReadTheDocs doc: https://docs.readthedocs.io/en/stable/guides/manage-translations.html

To update translation make PR with updates in ``docs/locales`` folder.

To activate new language send PR with update of ``.github/workflow/translations.yml``. Then the new language must be [activated in ReadTheDocs admin panel](https://docs.readthedocs.io/en/stable/localization.html#project-with-multiple-translations).
