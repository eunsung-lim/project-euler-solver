b = [i * (i+1) // 2 for i in range(2001)]

m = 2e6
p, q = 0, 0

for x in range(1, 2001):
    for y in range(1, 2001):
        if abs(b[x]*b[y] - 2e6) < m:
            p, q = x, y
            m = abs(b[x]*b[y] - 2e6)
            print(p, q)

print(p*q)