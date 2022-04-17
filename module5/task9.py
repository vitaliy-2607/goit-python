# Поработаем немного со спецификацией в форматировании строк. Напишите функцию formatted_numbers,
# которая возвращает список отформатированных строк
# Как вы уже поняли, функция formatted_numbers выводит таблицу чисел от 0 до 15 в десятичном,
# шестнадцатеричном и двоичном формате.
def formatted_numbers():
    list = []
    list.append("|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary'))
    for i in range(16):
        list.append("|{:<10}|{:^10}|{:>10}|".format(
            i, str(hex(i)[2:]), str(bin(i)[2:])))
    return list
