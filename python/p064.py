from base import is_square
from math import gcd

ans = 0

for n in range(2, 10001):
    if is_square(n):
        continue
    
    p0 = int(n**0.5)
    a, b, c, d = p0, 1, -p0, 1
    p = p0
    period = 1
    while True:
        p = int(d / (b * n**0.5 + c))
        
        a2 = p
        d2 = b**2 * n - c**2
        b2 = b * d
        c2 = -c*d - a2*d2
        
        a, b, c, d = a2, b2, c2, d2
        
        g = gcd(b, c, d)
        b //= g
        c //= g
        d //= g
        
        if (b, c, d) == (1, -p0, 1):
            break
        period += 1

    if period % 2 == 1:
        ans += 1

print(ans)
