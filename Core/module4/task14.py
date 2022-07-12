# Создайте функцию parse_args, которая возвращает строку, составленную из аргументов командной строки,
# разделенных пробелами. Например, если скрипт был вызван командой: python run.py first second,
# то функция parse_args должна вернуть строку следующего вида "first second".
import sys


def parse_args():
    result = []
    for arg in sys.argv[1:]:
        result.append(arg)
    return (" ".join(result))
