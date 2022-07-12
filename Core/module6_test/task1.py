#Разработайте функцию total_salary(path)(параметр path - путь к файлу), которая будет разбирать
#построчно файл и возвращать общую сумму заработной платы всех разработчиков компании.

def total_salary(path):
    fh = open(path, 'r')
    result = 0
    while True:
        line = fh.readline()
        if not line:
            break
        result += float(line.split(',')[1])
    fh.close()
    return result
