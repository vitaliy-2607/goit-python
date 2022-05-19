#Реализуйте функцию записи данных о сотрудниках компании в файл, чтобы информация о каждом
#сотруднике начиналась с новой строки.
def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for _ in employee_list:
        for people in _:
            fh.write(people + '\n')
    fh.close()
