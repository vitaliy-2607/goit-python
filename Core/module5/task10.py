# Напишите функцию find_word, которая принимает два параметра: первый text и второй word.
# Функция выполняет поиск указанного слова word в тексте text с помощью функции search и возвращает словарь.
import re


def find_word(text, word):
    result = False
    start = None
    end = None
    if word in text:
        result = True
        search = re.search(word, text)
        start = search.start()
        end = search.end()
    return {
        'result': result,
        'first_index': start,
        'last_index': end,
        'search_string': word,
        'string': text
    }
