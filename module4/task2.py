# При анализе данных часто возникает необходимость избавиться от экстремальных значений,
# прежде чем начать работать с данными дальше. Напишите функцию prepare_data, которая удаляет
# из переданного списка наибольшее и наименьшее значение, сортирует его в порядке возрастания
# и возвращает измененный список в качестве результата.

def prepare_data(data):
    min_number = min(data)
    max_number = max(data)
    data.remove(min_number)
    data.remove(max_number)
    new_data = sorted(data)
    return new_data