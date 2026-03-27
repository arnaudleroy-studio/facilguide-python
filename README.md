# facilguide

Python access to [Facil.guide](https://facil.guide) -- simplified tech guides for seniors in 5 languages: English, Spanish, French, Portuguese, and Italian.

## Install

```bash
pip install facilguide
```

## Quick Start

```python
import facil

# Browse all guides
all_guides = facil.guides()
print(f"{len(all_guides)} guides available")

# Filter by language
spanish = facil.guides(lang="es")
french = facil.guides(lang="fr")

# Filter by category
security = facil.guides(category="security")
social = facil.guides(category="social")

# Search guides
facil.search("whatsapp")
# [{'title': 'How to Set Up WhatsApp', 'category': 'social', ...}]

# Available languages
facil.languages()
# [{'code': 'en', 'name': 'English', 'url': 'https://facil.guide/en/'}, ...]

# Guide categories
facil.categories()
# [{'slug': 'smartphone', 'name': 'Smartphone', ...}, ...]
```

## Categories

| Category | Description |
|----------|------------|
| Smartphone | Phone setup, apps, and everyday use |
| Tablet | iPad and Android tablet guides |
| Computer | Desktop and laptop essentials |
| Internet | Web browsing, email, and online safety |
| Social Media | Facebook, WhatsApp, and staying connected |
| Security | Passwords, scams, and digital safety |
| Photos & Video | Taking, storing, and sharing photos |
| Health Apps | Health tracking and telehealth |

## Languages

- English -- [facil.guide/en](https://facil.guide/en/)
- Spanish -- [facil.guide/es](https://facil.guide/es/)
- French -- [facil.guide/fr](https://facil.guide/fr/)
- Portuguese -- [facil.guide/pt](https://facil.guide/pt/)
- Italian -- [facil.guide/it](https://facil.guide/it/)

## Links

- [Facil.guide](https://facil.guide) -- Main site
- [English Guides](https://facil.guide/en/) -- All guides in English
- [Guides en Espanol](https://facil.guide/es/) -- Guias en espanol

## License

MIT
