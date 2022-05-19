#Выполним теперь обратную задачу и создадим функцию read_employees_from_file(path),
#которая будет читать данные из файла и возвращать список сотрудников в виде:
#['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']


def read_employees_from_file(path):
    fh = open(path, 'r')
    result = []
    while True:
        line = fh.readline().strip()
        if not line:
            break
        result.append(line)
    fh.close()
    return result
