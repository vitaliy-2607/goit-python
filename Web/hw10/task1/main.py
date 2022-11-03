import timeit
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


@cache
def Fibonacci_cache_redis(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    start_time = timeit.default_timer()
    result = Fibonacci(n)
    print(f'Result: {result}\nDuration without cache: {timeit.default_timer() - start_time} sec')

    print('<'+'-' * 50+'>')

    start_time = timeit.default_timer()
    result_cache = Fibonacci_cache_redis(n)
    print(f'Result: {result_cache}\nDuration with Redis cache: {timeit.default_timer() - start_time} sec')