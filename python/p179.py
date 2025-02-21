from base import all_primes_under

N = 10 * 1000 * 1000

num_divisors = [1] * (N+1)

for p in all_primes_under(N):
    for i in range(p, N+1, p):
        j, cnt = i, 0
        while j % p == 0:
            j //= p
            cnt += 1
        num_divisors[i] *= (cnt+1)

ans = 0
for n in range(1, N):
    if num_divisors[n] == num_divisors[n+1]:
        ans += 1

print(ans)
