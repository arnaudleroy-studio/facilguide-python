facilguide -- Simplified Tech Guides for Seniors
=================================================

**facilguide** is the official Python package for `Facil.guide <https://facil.guide>`_, a
multilingual platform providing clear, step-by-step tech guides for seniors in 5 languages:
English, Spanish, French, Portuguese, and Italian.

Use this package to browse the guide catalog, filter by language or category, and
integrate senior-friendly tech content into your applications.

Quick Start
-----------

.. code-block:: python

   import facil

   # Browse guides in Spanish
   guides = facil.guides(lang="es")
   for g in guides:
       print(g["title"])

   # Get all categories
   categories = facil.categories()

   # Search guides
   results = facil.search("whatsapp")

   # Available languages
   languages = facil.languages()
   for lang in languages:
       print(f"{lang['name']}: {lang['url']}")

Browse all guides at `facil.guide <https://facil.guide>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   api
   guides

Links
-----

- **Website**: `facil.guide <https://facil.guide>`_
- **English Guides**: `facil.guide/en/ <https://facil.guide/en/>`_
- **Guias en Espanol**: `facil.guide/es/ <https://facil.guide/es/>`_
- **Guides en Francais**: `facil.guide/fr/ <https://facil.guide/fr/>`_
- **PyPI**: `pypi.org/project/facilguide/ <https://pypi.org/project/facilguide/>`_
- **GitHub**: `github.com/arnaudleroy-studio/facilguide-python <https://github.com/arnaudleroy-studio/facilguide-python>`_

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
