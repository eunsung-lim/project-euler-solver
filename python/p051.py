from base import all_primes_under

N = 1000 * 1000

all_primes = all_primes_under(N)
all_primes_set = set(all_primes)

ans = 0

for p in all_primes:
    p_str = list(str(p))
    for c in set(p_str):
        
        cnt = []
        for k in range(10):
            if k == 0 and p_str[0] == c:
                continue
            if int("".join(p_str).replace(c, str(k))) in all_primes_set:
                cnt.append(k)
        
        if len(cnt) >= 8:
            print(p, cnt, c)
            ans = p
            break
    
    if ans:
        break

print(ans)
