#Реализуйте функцию add_employee_to_file(record, path), которая в файл (параметр path - путь к файлу)
#будет добавлять сотрудника (параметр record) в виде строки "Drake Mikelsson, 19".
def add_employee_to_file(record, path):
    file = open(path, 'a')
    file.write(record + '\n')
    file.close()
