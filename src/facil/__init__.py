"""
facil - Simplified tech guides data from Facil.guide.

Access multilingual tech guides for seniors across 5 languages:
English, Spanish, French, Portuguese, and Italian.

    >>> import facil
    >>> guides = facil.guides(lang="en")
    >>> guides[0]["title"]
    'How to Set Up WhatsApp'

    >>> langs = facil.languages()
    >>> [l["name"] for l in langs]
    ['English', 'Spanish', 'French', 'Portuguese', 'Italian']

Full site: https://facil.guide
"""

__version__ = "0.1.0"
__author__ = "Facil Guide"
__url__ = "https://facil.guide"

from facil.data import guides, categories, languages, search

__all__ = [
    "guides",
    "categories",
    "languages",
    "search",
]
