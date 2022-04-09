# Создайте функцию  format_string для форматирования строки. В функцию мы передаем строку string и length
# длину новой строки. Функция возвращает новую строку по следующему алгоритму:
# Если длина исходной строки больше или равна length, мы возвращаем ее в том же виде
# Если она меньше length, мы добавляем впереди строки пробелы в количестве(length - len(string)) // 2.

def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        return (" " * ((length - len(string)) // 2)) + string
