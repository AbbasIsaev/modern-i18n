from i18n.config import t

print(t('Привет'))  # -> Привет!
# Перевод с указанием локали
print(t('Привет', locale='en'))  # -> Hello!
# Перевод с указанием параметров
print(t('Итого {a}+{b}={total}', a=5, b=10, total=15))  # -> Итого 5+10=15.
print(t('Итого {a}+{b}={total}', locale='en', a=5, b=10, total=15))  # -> Total 5+10=15.
print(t('Ключ не существует'))  # Warning -> Ключ не существует
