# В модуле работы с функциями мы писали функцию get_fullname для составления полного имени.
# Выполним небольшое продолжение задачи и напишем функцию is_check_name, которая принимает
# два параметра (fullname, first_name) и возвращает логическое True или False. Это результат проверки,
# является ли строка first_name префиксом строки fullname. Функция is_check_name строго относится к регистру
# букв, то есть «Sam» и «sam» для неё разные имена.
def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)
