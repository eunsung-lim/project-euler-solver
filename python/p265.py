ans = []
N = 5
s0 = "0"*N

def f(s, t):
    if len(s) == (1<<N):
        for i in range(1, N):
            t.add(s[-i:]+"0"*(N-i))
        if len(t) == (1<<N):
            ans.append(s)
            return
    s0 = s[-N+1:]+"0"
    if s0 not in t:
        f(s+"0", t|{s0})
    s1 = s[-N+1:]+"1"
    if s1 not in t:
        f(s+"1", t|{s1})
    return

f(s0, {s0})
print(sum(int(x, 2) for x in ans))
# 209110240768