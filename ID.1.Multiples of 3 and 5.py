def zarib(n):
    sum1 = 0
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            sum1 = sum1 + i
    return sum1
""" better solution:
ans = sum(x for x in range(1000) if (x % 3 == 0 and x % 5 == 0))
"""

print(zarib(1000))
