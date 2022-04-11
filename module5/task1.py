# Напишите функцию real_len, которая подсчитывает и возвращает длину строки без следующих управляющих
# символов: [\n, \f, \r, \t, \v]
def real_len(text):
    return len(text)-text.count('\n')-text.count('\t')-text.count('\f')-text.count('\v')-text.count('\r')
