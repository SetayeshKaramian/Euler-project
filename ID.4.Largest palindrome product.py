import time

def check_palindrome(number):
    palindrome = bool
    number = str(number)
    if number[::-1] == number:
        palindrome = True
    return palindrome


def primes(number):
    lst_primes = []
    for i in range(2, int(number ** 0.5 + 1)):
        while number % i == 0:
            number = number / i
            lst_primes.append(i)
    return lst_primes

start = time.time()
for n in range(999999, 99999, -1):
    if check_palindrome(n) == True:
        x = 1
        y = 1
        lst = primes(n)
        lst = lst[::-1]
        for i in lst:
            if x * i < 1000:
                x = x * i
            else:
                y = y * i
        if y < 1000 and y > 900:
            print(x, y)
            print(n)
            break
print(time.time() - start)
