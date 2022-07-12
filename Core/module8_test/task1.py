# Разработайте функцию get_days_from_today(date), которая будет возвращать количество дней от
# текущей даты, где параметр date — это строка формата '2020-10-09' (год-месяц-день).
from datetime import datetime


def get_days_from_today(date):
    new_date = date.split('-')
    current_day = datetime.now()
    day1 = datetime(year=int(new_date[0]), month=int(
        new_date[1]), day=int(new_date[2]))
    day2 = datetime(year=current_day.year,
                    month=current_day.month, day=current_day.day)
    difference = day2 - day1
    return difference.days
