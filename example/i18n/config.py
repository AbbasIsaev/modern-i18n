import os
from pathlib import Path

from modern_i18n.i18n import I18n

project_root = Path(__file__).resolve().parent.parent
LOCALE_PATH = os.path.join(project_root, 'locale')

config = {
    'locale_path': LOCALE_PATH,  # Путь к директории с переводами
    'locales': ['ru', 'en'],  # Список доступных языков
    'default_locale': 'ru',  # Язык по умолчанию
    'default_encoding': 'UTF-8'  # Кодировка для файлов перевода по умолчанию 'UTF-8'
}

i18n = I18n(config)
t = i18n.translate
