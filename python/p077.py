from base import all_primes_under

N = 100

primes = all_primes_under(N)

dp = [0] * (N+1)
dp[0] = 1

for p in primes:
    dp2 = [0] * (N+1)
    dp2[0] = 1
    for i in range(1, N+1):
        dp2[i] += sum(dp[i-j] for j in range(0, i+1, p))
    dp = dp2.copy()

for n in range(N+1):
    if dp[n] > 5000:
        print(n)
        break