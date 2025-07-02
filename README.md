# modern-i18n

Modern-i18n is a modern library for internationalization (i18n) in Python projects.

### Installation

```shell scipt
pip install modern-i18n
```

### Project Structure

Here is an example of the typical project structure after setting up the `modern-i18n` library:

```
project/
├── i18n/                # 📁 Internationalization module
│   └── config.py        # 📄 Configuration file: default language, path to translations, etc.
│
├── locale/              # 📁 Directory with translations (localizations)
│   ├── en/              # 📁 English locale
│   │   └── translation.json  # 📄 Translation file for English
│   └── ru/              # 📁 Russian locale
│       └── translation.json  # 📄 Translation file for Russian
│
└── example.py           # 📄 Example of using the translation function
```

### Configuration

All library settings are located in the `i18n/config.py` file. Here is an example of a basic configuration:

```python
import os
from pathlib import Path

from modern_i18n.i18n import I18n

project_root = Path(__file__).resolve().parent.parent
LOCALE_PATH = os.path.join(project_root, 'locale')

config = {
    'locale_path': LOCALE_PATH,  # Path to the directory with translations
    'locales': ['ru', 'en'],  # List of available languages
    'default_locale': 'ru',  # Default language
    'default_encoding': 'UTF-8'  # Default encoding for translation files is 'UTF-8'
}

i18n = I18n(config)
t = i18n.translate
```

- In the `i18n/config.py` file, you can configure main parameters such as the list of supported languages, the default
  language, the path to the translation directory, and additional options.
- All translations are stored in JSON format inside the `locale` directory, where each locale has its own folder.

### Examples of `translation.json` content

JSON files store key-value pairs, where the **key** is the original phrase, and the **value** is its translation into
the target language.

`locale/en/translation.json`:

```json
{
  "Привет": "Hello!",
  "Итого {a}+{b}={total}": "Total {a}+{b}={total}."
}
```

`locale/ru/translation.json`:

```json
{
  "Привет": "Привет!",
  "Итого {a}+{b}={total}": "Итого {a}+{b}={total}."
}
```

> ⚠️ Note that the original keys must be the same across all language files to ensure correct matching.

### Usage

Example of basic usage of the translation function `t`:

```python
from i18n.config import t

print(t('Привет'))  # -> Привет!
# Translation with specified locale
print(t('Привет', locale='en'))  # -> Hello!
# Translation with parameters
print(t('Итого {a}+{b}={total}', a=5, b=10, total=15))  # -> Итого 5+10=15.
print(t('Итого {a}+{b}={total}', locale='en', a=5, b=10, total=15))  # -> Total 5+10=15.
print(t('Ключ не существует'))  # Warning -> Ключ не существует
```