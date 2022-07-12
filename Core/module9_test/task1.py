'''
Реализуйте функцию высшего порядка get_student_grade, которая принимает параметр option.
Если он равен значению "grade", то функция возвращает функцию get_grade, а если его значение
равно "description", то возвращает функцию get_description. Если параметр по значению не совпал с
заданными, то функция get_student_grade должна возвращать значение None.
'''


def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "отлично",
        "B": "очень хорошо",
        "C": "хорошо",
        "D": "удовлетворительно",
        "E": "достаточно",
        "FX": "неудовлетворительно",
        "F": "неудовлетворительно",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == 'grade':
        return get_grade
    elif option == 'description':
        return get_description
