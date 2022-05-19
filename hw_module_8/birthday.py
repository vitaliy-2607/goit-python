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


from datetime import datetime, date


users = [
    {'name': 'Vitaliy', 'birthday': '26.07.1990'},
    {'name': 'Arsen', 'birthday': '17.05.1997'},
    {'name': 'Alex', 'birthday': '21.05.1999'},
    {'name': 'Victor', 'birthday': '23.05.1980'},
    {'name': 'Pavel', 'birthday': '05.12.1994'},
    {'name': 'Maria', 'birthday': '16.05.2000'},
    {'name': 'Alisa', 'birthday': '16.05.2000'},
    {'name': 'Kristina', 'birthday': '22.05.2000'},
]


def get_birthdays_per_week(users):
    week_bday = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
        'Next Monday': ''
    }
    today = date.today()

    for el in users:
        birth = datetime.strptime(el['birthday'], "%d.%m.%Y").date()
        new_birth = datetime(year=today.year, month=birth.month, day=birth.day)
        if today.month == new_birth.month:
            if new_birth.day in range(today.day, today.day+7):
                if new_birth.weekday() == 0:
                    week_bday['Monday'] += el['name']
                    week_bday['Monday'] += ', '

                if new_birth.weekday() == 1:
                    week_bday['Tuesday'] += el['name']
                    week_bday['Tuesday'] += ', '

                if new_birth.weekday() == 2:
                    week_bday['Wednesday'] += el['name']
                    week_bday['Wednesday'] += ', '

                if new_birth.weekday() == 3:
                    week_bday['Thursday'] += el['name']
                    week_bday['Thursday'] += ', '

                if new_birth.weekday() == 4:
                    week_bday['Friday'] += el['name']
                    week_bday['Friday'] += ', '

                if new_birth.weekday() in (5, 6):
                    week_bday['Next Monday'] += el['name']
                    week_bday['Next Monday'] += ', '

    for k, v in week_bday.items():
        if len(v) > 0:
            print(k+': ' + v[:-2])


if __name__ == '__main__':
    get_birthdays_per_week(users)
