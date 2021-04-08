ans = 0
for i in range(1, 101):
    el = sum(x * i * 2 for x in range(i + 1, 101))
    ans += el
print(ans)