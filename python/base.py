from functools import reduce

def is_square(n):
    return int(n**0.5)**2 == n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def all_primes_under(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]


def get_prime_factors(n):
    factors = []
    for p in all_primes_under(n):
        if n % p == 0:
            factors.append(p)
            n //= p
    return factors

if __name__ == "__main__":
    print(all_primes_under(100))