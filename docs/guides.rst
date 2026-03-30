Guide Catalog
=============

The ``facil`` package includes the full catalog of tech guides for seniors from
`Facil.guide <https://facil.guide>`_. Guides are available in up to 5 languages and
organized by category and difficulty level.

Categories
----------

The guide catalog is organized into 8 categories:

- **Smartphone** -- Phone setup, apps, and everyday use
- **Tablet** -- iPad and Android tablet guides
- **Computer** -- Desktop and laptop essentials
- **Internet** -- Web browsing, email, and online safety
- **Social Media** -- Facebook, WhatsApp, and staying connected
- **Security** -- Passwords, scams, and digital safety
- **Photos & Video** -- Taking, storing, and sharing photos
- **Health Apps** -- Health tracking and telehealth

.. code-block:: python

   categories = facil.categories()
   for cat in categories:
       print(f"{cat['name']}: {cat['description']}")

Languages
---------

All guides are available in multiple languages:

- **English** -- `facil.guide/en/ <https://facil.guide/en/>`_
- **Spanish** -- `facil.guide/es/ <https://facil.guide/es/>`_
- **French** -- `facil.guide/fr/ <https://facil.guide/fr/>`_
- **Portuguese** -- `facil.guide/pt/ <https://facil.guide/pt/>`_
- **Italian** -- `facil.guide/it/ <https://facil.guide/it/>`_

.. code-block:: python

   # Get guides available in Portuguese
   pt_guides = facil.guides(lang="pt")

   # Get all language URLs
   for lang in facil.languages():
       print(f"{lang['name']}: {lang['url']}")

Difficulty Levels
-----------------

Guides are tagged with difficulty levels to help seniors progress:

- **beginner** -- Basic concepts, step-by-step with screenshots
- **intermediate** -- Builds on basics, more features

.. code-block:: python

   # Beginner guides in Spanish
   beginner_es = [
       g for g in facil.guides(lang="es")
       if g["difficulty"] == "beginner"
   ]

Example: Building a Guide Finder
---------------------------------

.. code-block:: python

   import facil

   def find_guide(topic, lang="en"):
       \"\"\"Find a guide by topic in a specific language.\"\"\"
       results = facil.search(topic, lang=lang)
       if results:
           guide = results[0]
           print(f"Found: {guide['title']}")
           print(f"Category: {guide['category']}")
           print(f"Difficulty: {guide['difficulty']}")
           # Build the URL
           print(f"Read at: https://facil.guide/{lang}/{guide['slug']}/")
       else:
           print(f"No guide found for '{topic}' in {lang}")

   find_guide("whatsapp", lang="es")
   # Found: How to Set Up WhatsApp
   # Category: social
   # Difficulty: beginner
   # Read at: https://facil.guide/es/setup-whatsapp/

Browse the full guide library at `Facil.guide <https://facil.guide>`_.
