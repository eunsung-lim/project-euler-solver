ans = 0

for n in range(1, 101):
    k = 1
    for r in range(n):
        k = k * (n - r) // (r + 1)
        if k > 1000000:
            ans += 1

print(ans)