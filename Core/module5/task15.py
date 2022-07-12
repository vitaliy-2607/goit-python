# Напишите регулярное выражение для функции find_all_links, которая будет в тексте (параметр text)
# находить все линки и возвращать список полученных из текста совпадений.
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r'https?://\w{3}\.?(?:\w+\.)*\w{2,5}', text)
    for match in iterator:
        result.append(match.group())
    return result
