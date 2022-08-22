from multiprocessing import Process, Pool, cpu_count
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


if __name__ == '__main__':
    star = time()
    first = Process(target=factorize, args=(128,))
    second = Process(target=factorize, args=(256,))
    third = Process(target=factorize, args=(99999,))
    fourth = Process(target=factorize, args=(10651060,))

    first.start()
    second.start()
    third.start()
    fourth.start()

    first.join()
    second.join()
    third.join()
    fourth.join()

    end = time()
    print(end-star)