from base import all_primes_under

primes = all_primes_under(int(1e8))
prime_set = set(primes)

ans = []
for p in primes:
    if str(p*p)[::-1] == str(p*p):
        continue
    q = int(str(p*p)[::-1]) ** 0.5
    if q == int(q) and int(q) in prime_set:
        ans.append(p)
        if len(ans) == 50:
            break

print(sum([x*x for x in ans]))