N = int(1e6)

def f(n, s):
    if n == s:
        return True
    if n < s or s < 0:
        return False
    n = str(n)
    l = len(n)
    return any(f(int(n[i:]), s-int(n[:i])) for i in range(1, l))

ans = 0
for n in range(4, N+1):
    if f(n*n, n):
        ans += n*n

print(ans)
