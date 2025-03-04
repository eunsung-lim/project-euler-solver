from math import factorial

def check(n):
    s = {n}
    while True:
        m = sum(factorial(int(i)) for i in str(n))
        if m in s:
            return len(s)
        s.add(m)
        n = m
        if len(s)>60:
            return s

ans = 0
for i in range(1, 1000000):
    if check(i)==60:
        ans+=1
print(ans)