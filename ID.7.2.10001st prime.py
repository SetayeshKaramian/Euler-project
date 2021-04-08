import time


def is_prime(n):
    sqr = n ** .5
    for prime in primes:
        if prime > sqr:
            return True
        if n % prime == 0:
            return False
    return True


def check(n):
    if is_prime(n):
        primes.append(n)


start = time.time()
primes = [2, 3]
num = 6


while len(primes) < 10001:
    check(num - 1)
    check(num + 1)
    num += 6

print(primes[10000])
print(time.time() - start)
