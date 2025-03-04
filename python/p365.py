from math import comb
from collections import defaultdict

MOD = int(1e18)
N = int(1e18)
M = int(1e9)

# Calculate C(N,M) mod p for each prime p between 1000 and 5000
def lucas(n, k, p):
    # Lucas theorem for calculating nCk mod p
    if k > n:
        return 0
    if k == 0:
        return 1
    if k == 1:
        return n % p
    
    # Get base p representations
    np = []
    kp = []
    while n:
        np.append(n % p)
        n //= p
    while k:
        kp.append(k % p)
        k //= p
        
    # Pad with zeros
    while len(kp) < len(np):
        kp.append(0)
        
    # Apply Lucas theorem
    result = 1
    for ni, ki in zip(np, kp):
        if ki > ni:
            return 0
        result = (result * comb(ni, ki)) % p
    return result

# Find all primes between 1000-5000
primes_1k_5k = [p for p in range(1000, 5001) if all(p % i != 0 for i in range(2, int(p**0.5) + 1))]

# Calculate C(N,M) mod p for each prime
remainders = {}
for p in primes_1k_5k:
    remainders[p] = lucas(N, M, p)

# Find all combinations of 3 primes and their product
ans = 0
seen = set()
for i in range(len(primes_1k_5k)):
    p1 = primes_1k_5k[i]
    for j in range(i+1, len(primes_1k_5k)):
        p2 = primes_1k_5k[j]
        for k in range(j+1, len(primes_1k_5k)):
            p3 = primes_1k_5k[k]
            
            # Chinese Remainder Theorem
            n = p1 * p2 * p3
            if n in seen:
                continue
            seen.add(n)
            
            # Calculate coefficients
            n1 = n // p1
            n2 = n // p2 
            n3 = n // p3
            
            # Calculate modular multiplicative inverses
            v1 = pow(n1, p1-2, p1)
            v2 = pow(n2, p2-2, p2)
            v3 = pow(n3, p3-2, p3)
            
            # Apply CRT formula
            result = (remainders[p1] * n1 * v1 + 
                     remainders[p2] * n2 * v2 + 
                     remainders[p3] * n3 * v3) % n
            
            ans = (ans + result) % MOD

print(ans)
