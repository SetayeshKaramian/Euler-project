fibonacci = [1, 2]
m = 2
i = fibonacci[-1]
while i < 4000000:
    i = (fibonacci[-1] + fibonacci[-2])
    fibonacci.append(i)
    if i % 2 == 0:
        m += i
print(m)
