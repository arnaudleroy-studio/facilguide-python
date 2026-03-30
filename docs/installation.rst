Installation
============

Install from PyPI
-----------------

.. code-block:: bash

   pip install facilguide

Requirements
------------

- Python 3.9 or later
- Zero runtime dependencies

Install from Source
-------------------

.. code-block:: bash

   git clone https://github.com/arnaudleroy-studio/facilguide-python.git
   cd facilguide-python
   pip install -e .

Verify Installation
-------------------

.. code-block:: python

   import facil
   print(facil.__version__)  # 0.1.0

   # Quick test -- list available languages
   languages = facil.languages()
   for lang in languages:
       print(f"{lang['name']}: {lang['url']}")

Browse all guides at `facil.guide <https://facil.guide>`_.
