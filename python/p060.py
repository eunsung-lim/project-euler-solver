from itertools import combinations
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def concat_prime(p1, p2):
    # Check if concatenating p1,p2 and p2,p1 both give primes
    n1 = int(str(p1) + str(p2))
    n2 = int(str(p2) + str(p1))
    return is_prime(n1) and is_prime(n2)

def find_prime_pairs():
    # Generate primes up to reasonable limit
    primes = [p for p in range(3, 10000, 2) if is_prime(p)]
    
    # Find pairs that work
    pairs = []
    for p1, p2 in combinations(primes, 2):
        if concat_prime(p1, p2):
            pairs.append((p1, p2))
    
    # Build graph of compatible pairs
    graph = {}
    for p1, p2 in pairs:
        if p1 not in graph:
            graph[p1] = set()
        if p2 not in graph:
            graph[p2] = set()
        graph[p1].add(p2)
        graph[p2].add(p1)
    
    # Find set of 5 primes
    min_sum = float('inf')
    for p1 in graph:
        for p2 in graph[p1]:
            common2 = graph[p1] & graph[p2]
            for p3 in common2:
                common3 = common2 & graph[p3]
                for p4 in common3:
                    common4 = common3 & graph[p4]
                    for p5 in common4:
                        # Verify all pairs work
                        group = {p1, p2, p3, p4, p5}
                        if all(concat_prime(x, y) for x, y in combinations(group, 2)):
                            min_sum = min(min_sum, sum(group))
    
    return min_sum

print(find_prime_pairs())
