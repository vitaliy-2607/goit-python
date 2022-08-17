from time import time


def factorize(*number):
    n = 0
    for num in number:
        list_for_result = []
        while n <= num:
            n += 1
            if num % n == 0:
                list_for_result.append(n)
            continue
        n = 0
        yield list_for_result


time_before = time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
time_after = time()
print(round(time_after-time_before, 3))
assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]