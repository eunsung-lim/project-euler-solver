from base import all_primes_under
from itertools import permutations

primes = all_primes_under(int(10**(4.5)))
prime_set = set(primes)

def is_prime(n):
    if n < 2:
        return False
    for p in primes:
        if p*p > n:
            return True
        if n % p == 0:
            return False
    return True

ans = set()

def f(current, previous):
    if not current:
        ans.add(tuple(sorted(previous)))
    for i in range(1, len(current)+1):
        if is_prime(int(current[:i])):
            f(current[i:], previous | {int(current[:i])})

for c in permutations(str(123456789)):
    c = "".join(c)
    f(c, set())

print(ans)
