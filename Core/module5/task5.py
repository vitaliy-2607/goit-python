# Напишите функцию get_phone_numbers_for_сountries, которая будет:
# Принимать список телефонных номеров.
# Санитизировать(нормализовать) полученный список телефонов клиентов с помощью нашей функции sanitize_phone_number.
# Сортировать телефонные номера по указанным в таблице странам.
# Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
# {
# "UA" : [ < здесь список телефонов > ],
# "JP": [ < здесь список телефонов > ],
# "TW": [ < здесь список телефонов > ],
# "SG": [ < здесь список телефонов > ]
# }
# Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен
# в список словаря с ключом "UA".
import re


def get_phone_numbers_for_countries(list_phones):
    jp, sg, tw, ua = [], [], [], []
    for i in list_phones:
        phone = re.sub("[^0-9]", "", i)
        if phone.startswith('81'):
            jp.append(phone)
        elif phone.startswith('65'):
            sg.append(phone)
        elif phone.startswith('886'):
            tw.append(phone)
        else:
            ua.append(phone)
    return {
        "UA": ua,
        "JP": jp,
        "TW": tw,
        "SG": sg
    }
