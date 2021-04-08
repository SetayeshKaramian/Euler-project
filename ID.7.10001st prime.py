import time


def primes(n):
    primes_list = [2]
    num = 3
    while len(primes_list) != n:
        if all(num % i != 0 for i in range(2, int(num ** .5) + 1)):
            primes_list.append(num)
        num = num + 2
    return primes_list[-1]


start = time.time()
print(primes(10001))
print(time.time() - start)
