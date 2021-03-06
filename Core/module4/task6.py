# У нас есть список показателей студентов группы — это список с полученными балами по тестированию.
# Необходимо список поделить на две части. Напишите функцию split_list, которая принимает
# список (целые числа), находит среднее значение балла в списке и делит его на два списка.
# В первый попадают значения меньше среднего, включая среднее значение, а во второй — строго больше среднего.
# Функция возвращает кортеж этих двух списков. Для пустого списка возвращаем два пустых списка.

def split_list(grade):
    a, b = [], []
    grade_len = len(grade)
    if grade_len == 0:
        return a, b
    else:
        grade_sum = sum(grade)
        average_value = grade_sum/grade_len
        for i in grade:
            if i <= average_value:
                a.append(i)
            else:
                b.append(i)
        return (a, b)
