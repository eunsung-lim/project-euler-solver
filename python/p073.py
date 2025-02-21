from base import prime_factors

ans = 0
N = 12000

for d in range(4, N+1):
    relative = [True] * (d+1)
    for p in prime_factors(d):
        for i in range(p, d//2+1, p):
            relative[i] = False

    for i in range(d//3+1, d//2+1):
        if relative[i] and 2*i < d < 3*i:
            ans += 1

print(ans)
