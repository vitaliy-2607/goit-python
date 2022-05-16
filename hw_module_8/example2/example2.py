'''
Задание#
Вам нужно реализовать полезную функцию для вывода списка коллег, которых надо поздравить с днём рождения на неделе.

У вас есть список словарей users, каждый словарь в нём обязательно имеет ключи name и birthday. Такая структура представляет модель списка пользователей с их именами и днями рождения. name — это строка с именем пользователя, а birthday — это datetime объект, в котором записан день рождения.

Ваша задача написать функцию get_birthdays_per_week, которая получает на вход список users и выводит в консоль (при помощи print) список пользователей, которых надо поздравить по дням.

Условия приёмки#
get_birthdays_per_week выводит именинников в формате:
Monday: Bill, Jill
Friday: Kim, Jan
Пользователей, у которых день рождения был на выходных, надо поздравить в понедельник.
Для отладки удобно создать тестовый список users и заполнить его самостоятельно.
Функция выводит пользователей с днями рождения на неделю вперед от текущего дня.
Неделя начинается с понедельника.
'''
import re
from datetime import datetime, date


def get_birthdays_per_week():
    week_bday = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
        'Next Monday': ''
    }
    today = date.today()

    file = open('example2/b-day.txt', 'r')
    for line in file:
        name = re.findall('[a-zA-Z]+', line)
        b_day = re.findall('\d+.\d+.\d+', line)
        birth = datetime.strptime(b_day[0], "%d.%m.%Y").date()
        new_birth = datetime(year=today.year, month=birth.month, day=birth.day)
        if today.month == new_birth.month:
            if new_birth.day in range(today.day+1, today.day+8):
                if new_birth.weekday() in (0, 5, 6):
                    week_bday['Monday'] += name[0]
                    week_bday['Monday'] += ', '

                if new_birth.weekday() == 1:
                    week_bday['Tuesday'] += name[0]
                    week_bday['Tuesday'] += ', '

                if new_birth.weekday() == 2:
                    week_bday['Wednesday'] += name[0]
                    week_bday['Wednesday'] += ', '

                if new_birth.weekday() == 3:
                    week_bday['Thursday'] += name[0]
                    week_bday['Thursday'] += ', '

                if new_birth.weekday() == 4:
                    week_bday['Friday'] += name[0]
                    week_bday['Friday'] += ', '

    file.close()
    for k, v in week_bday.items():
        if len(v) > 0:
            print(k+': ' + v[:-2])


get_birthdays_per_week()
