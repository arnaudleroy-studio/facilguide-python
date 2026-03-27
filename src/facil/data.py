"""Facil.guide data and guide catalog.

Access the catalog of simplified tech guides for seniors,
available in 5 languages.

    >>> import facil
    >>> guides = facil.guides(lang="es")
    >>> facil.categories()

Full site: https://facil.guide
"""

from __future__ import annotations


LANGUAGES = [
    {"code": "en", "name": "English", "url": "https://facil.guide/en/"},
    {"code": "es", "name": "Spanish", "url": "https://facil.guide/es/"},
    {"code": "fr", "name": "French", "url": "https://facil.guide/fr/"},
    {"code": "pt", "name": "Portuguese", "url": "https://facil.guide/pt/"},
    {"code": "it", "name": "Italian", "url": "https://facil.guide/it/"},
]

CATEGORIES = [
    {"slug": "smartphone", "name": "Smartphone", "description": "Phone setup, apps, and everyday use"},
    {"slug": "tablet", "name": "Tablet", "description": "iPad and Android tablet guides"},
    {"slug": "computer", "name": "Computer", "description": "Desktop and laptop essentials"},
    {"slug": "internet", "name": "Internet", "description": "Web browsing, email, and online safety"},
    {"slug": "social", "name": "Social Media", "description": "Facebook, WhatsApp, and staying connected"},
    {"slug": "security", "name": "Security", "description": "Passwords, scams, and digital safety"},
    {"slug": "photos", "name": "Photos & Video", "description": "Taking, storing, and sharing photos"},
    {"slug": "health", "name": "Health Apps", "description": "Health tracking and telehealth"},
]

GUIDES = [
    {"slug": "setup-whatsapp", "title": "How to Set Up WhatsApp", "category": "social", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "video-call-family", "title": "Video Call Your Family", "category": "social", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "strong-password", "title": "Create a Strong Password", "category": "security", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "spot-scam-email", "title": "How to Spot a Scam Email", "category": "security", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "send-photos", "title": "Send Photos to Family", "category": "photos", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "organize-photos", "title": "Organize Your Photos", "category": "photos", "difficulty": "intermediate", "languages": ["en", "es", "fr"]},
    {"slug": "setup-wifi", "title": "Connect to Wi-Fi", "category": "internet", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "online-banking", "title": "Safe Online Banking", "category": "security", "difficulty": "intermediate", "languages": ["en", "es", "fr"]},
    {"slug": "smartphone-basics", "title": "Smartphone Basics", "category": "smartphone", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "install-app", "title": "How to Install an App", "category": "smartphone", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "tablet-setup", "title": "Set Up Your New Tablet", "category": "tablet", "difficulty": "beginner", "languages": ["en", "es", "fr"]},
    {"slug": "email-basics", "title": "Email for Beginners", "category": "internet", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
    {"slug": "health-tracking", "title": "Health Apps Guide", "category": "health", "difficulty": "intermediate", "languages": ["en", "es"]},
    {"slug": "facebook-basics", "title": "Facebook for Beginners", "category": "social", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt"]},
    {"slug": "zoom-basics", "title": "How to Use Zoom", "category": "social", "difficulty": "beginner", "languages": ["en", "es", "fr", "pt", "it"]},
]


def guides(*, lang: str | None = None, category: str | None = None) -> list[dict]:
    """Get tech guides for seniors.

    Args:
        lang: Filter by language code (en, es, fr, pt, it).
        category: Filter by category slug.

    Returns:
        List of guide dicts.

    Examples:
        >>> import facil
        >>> spanish = facil.guides(lang="es")
        >>> security = facil.guides(category="security")

    Browse all: https://facil.guide
    """
    result = GUIDES
    if lang:
        result = [g for g in result if lang in g["languages"]]
    if category:
        result = [g for g in result if g["category"] == category]
    return result


def categories() -> list[dict]:
    """Get all guide categories.

    Returns:
        List of category dicts with slug, name, and description.
    """
    return list(CATEGORIES)


def languages() -> list[dict]:
    """Get all available languages.

    Returns:
        List of language dicts with code, name, and URL.
    """
    return list(LANGUAGES)


def search(query: str, *, lang: str | None = None) -> list[dict]:
    """Search guides by title.

    Args:
        query: Search term (case-insensitive).
        lang: Filter by language.

    Returns:
        List of matching guides.

    Examples:
        >>> facil.search("whatsapp")
        [{'title': 'How to Set Up WhatsApp', ...}]
    """
    q = query.lower()
    results = guides(lang=lang)
    return [g for g in results if q in g["title"].lower()]
