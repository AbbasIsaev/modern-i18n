import json
import os
import warnings
from pathlib import Path

# Получаем корень проекта
project_root = Path(__file__).resolve().parent
# Указываем путь к директории с локализациями
LOCALE_PATH = project_root / 'locale'
DEFAULT_LOCALE = 'en'


class I18n:
    config = None
    tm = {}

    def __init__(self, config: dict):
        """
        Инициализация i18n.

        @param config: Конфигурация i18n.
        """
        self.config = {
            'locale_path': LOCALE_PATH,
            'locales': [DEFAULT_LOCALE],
            'default_locale': DEFAULT_LOCALE,
            'default_encoding': 'UTF-8'
        }
        if config and isinstance(config, dict):
            self.config.update(config)

        locales = self.config.get('locales')
        if not locales or not isinstance(locales, list):
            locales = [self.config.get('default_locale', DEFAULT_LOCALE)]

        for locale in locales:
            file_path = os.path.join(self.config.get('locale_path', LOCALE_PATH), locale, 'translation.json')
            if not os.path.exists(file_path):
                warnings.warn(f"Translation file '{file_path} not found, please check the file path or create it.",
                              category=UserWarning, stacklevel=2)
                continue
            try:
                with open(file_path, 'r', encoding=self.config.get('default_encoding', 'UTF-8')) as f:
                    if not self.tm.get(locale, {}):
                        self.tm[locale] = {}
                    load_dict = json.load(f)
                    self.tm[locale].update(load_dict)
            except Exception:
                raise

    def get_locale(self, locale: str = None):
        if not locale:
            return self.config.get('default_locale', DEFAULT_LOCALE)
        else:
            return locale

    def translate(self, key: str, locale: str = None, **params) -> str:
        """
        Поиск перевода по ключу.

        @param key: Ключ поиска.
        @param locale: Локализация.
        @param params: Параметры для форматирования сообщения.
        @return: Перевод сообщения с учетом параметров.
        """
        key = str(key)
        locale = self.get_locale(locale)
        locale_dict = self.tm.get(locale, {})

        # if locale not set, search in default_locale
        if not locale_dict:
            warnings.warn(f"Localization '{locale}' is not allowed.",
                          category=UserWarning, stacklevel=2)
            locale_dict = self.tm.get(self.get_locale(), {})
        if not locale_dict:
            return key

        message = locale_dict.get(key, None)
        if message is None:
            warnings.warn(f"Translation message '{key}' not found, please check the message or create it.",
                          category=UserWarning, stacklevel=2)
            return key

        try:
            return str(message).format(**params)
        except KeyError as e:
            warnings.warn(f"Parameter {e} is missing in translation message '{key}'",
                          category=UserWarning, stacklevel=2)
            return key
