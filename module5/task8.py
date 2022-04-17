# Напишите функцию formatted_grades, которая принимает на вход словарь оценивания студентов по предмету.
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    count = 1
    for key, value in students.items():
        print('{:>4}{}{:<10}{}{:^5}{}{:^5}'.format(
            count, '|', key, '|', value, '|', grades.get(value)))
        count += 1
