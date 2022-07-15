# Напишите регулярное выражение для функции find_all_phones, которая будет в тексте (параметр text)
# находить все телефонные номера указанного шаблона и возвращать список полученных из текста совпадений.
import re


def find_all_phones(text):
    result = re.findall(
        r'\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{3}-\d{4}', text)
    return result