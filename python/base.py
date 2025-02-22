from functools import reduce
from math import gcd


def is_square(n):
    return int(n**0.5)**2 == n

def totient(n):
    for p in prime_factors(n):
        n *= p-1
        n //= p
    return n

def mobius(n):
    if n == 1:
        return 1
    pf = prime_factors(n)
    if n == reduce(lambda x, y: x*y, pf):
        return int((-1)**len(pf))
    return 0

# https://en.wikipedia.org/wiki/Totient_summatory_function
def totient_summatory(n):
    return sum(totient(i) for i in range(1, n+1))

def totient_summatory_fast(n):
    return sum(mobius(i) * (n//i) * (1+(n//i)) // 2 for i in range(1, n+1))


def is_coprime(a, b):
    return gcd(a, b) == 1

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def all_primes_under(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]


def prime_factors(n):
    factors = []
    for p in all_primes_under(n):
        if n % p == 0:
            factors.append(p)
            n //= p
    return factors

if __name__ == "__main__":
    print(all_primes_under(100))