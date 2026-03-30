API Reference
=============

This page documents the public API of the ``facil`` package (installed as ``facilguide``).
For the full guide library, visit `Facil.guide <https://facil.guide>`_.

Guide Functions
---------------

``facil.guides(*, lang=None, category=None)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get tech guides for seniors. Optionally filter by language or category.

**Parameters:**

- ``lang`` (str, optional) -- Filter by language code: ``'en'``, ``'es'``, ``'fr'``, ``'pt'``, ``'it'``.
- ``category`` (str, optional) -- Filter by category slug (see :func:`categories`).

**Returns:** List of guide dicts with ``slug``, ``title``, ``category``, ``difficulty``, and ``languages``.

.. code-block:: python

   import facil

   # All guides
   all_guides = facil.guides()

   # Spanish guides only
   spanish = facil.guides(lang="es")

   # Security guides in French
   security_fr = facil.guides(lang="fr", category="security")
   # Browse at: https://facil.guide/fr/

``facil.categories()``
^^^^^^^^^^^^^^^^^^^^^^

Get all guide categories.

**Returns:** List of category dicts with ``slug``, ``name``, and ``description``.

Available categories:

- ``smartphone`` -- Phone setup, apps, and everyday use
- ``tablet`` -- iPad and Android tablet guides
- ``computer`` -- Desktop and laptop essentials
- ``internet`` -- Web browsing, email, and online safety
- ``social`` -- Facebook, WhatsApp, and staying connected
- ``security`` -- Passwords, scams, and digital safety
- ``photos`` -- Taking, storing, and sharing photos
- ``health`` -- Health tracking and telehealth

.. code-block:: python

   categories = facil.categories()
   for cat in categories:
       print(f"{cat['name']}: {cat['description']}")

``facil.languages()``
^^^^^^^^^^^^^^^^^^^^^

Get all available languages with their `Facil.guide <https://facil.guide>`_ URLs.

**Returns:** List of language dicts with ``code``, ``name``, and ``url``.

.. code-block:: python

   languages = facil.languages()
   # [
   #   {'code': 'en', 'name': 'English', 'url': 'https://facil.guide/en/'},
   #   {'code': 'es', 'name': 'Spanish', 'url': 'https://facil.guide/es/'},
   #   {'code': 'fr', 'name': 'French', 'url': 'https://facil.guide/fr/'},
   #   {'code': 'pt', 'name': 'Portuguese', 'url': 'https://facil.guide/pt/'},
   #   {'code': 'it', 'name': 'Italian', 'url': 'https://facil.guide/it/'},
   # ]

``facil.search(query, *, lang=None)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Search guides by title (case-insensitive).

**Parameters:**

- ``query`` (str) -- Search term.
- ``lang`` (str, optional) -- Filter results by language.

**Returns:** List of matching guide dicts.

.. code-block:: python

   results = facil.search("whatsapp")
   # [{'title': 'How to Set Up WhatsApp', ...}]

   results_es = facil.search("whatsapp", lang="es")

See Also
--------

- `Facil.guide <https://facil.guide>`_ -- Main website
- `English Guides <https://facil.guide/en/>`_ -- Full English guide catalog
- `Guias en Espanol <https://facil.guide/es/>`_ -- Full Spanish guide catalog
