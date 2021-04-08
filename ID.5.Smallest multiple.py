lst_total = []
for number in range(20, 0, -1):
    lst = list()
    for i in range(2, number + 1):
        while number % i == 0:
            number = number / i
            lst.append(i)
    print(lst)
    for i in lst:
        if lst.count(i) > lst_total.count(i):
            t = lst.count(i) - lst_total.count(i)
            for n in range(0, t):
                lst_total.append(i)
        print(lst_total)

x = 1
for i in lst_total:
    x = x * i
print(x)
