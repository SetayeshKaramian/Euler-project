def prime(number):
    state = bool
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            state = False
            break
    return state
n = 600851475143
s = int(n ** 0.5) + 1
for a in range(s, 1, -2):
    print(a)
    if prime(a) != False:
        if n % a == 0:
            print(a)
            break

