from base import is_palindrome

ans = set()
N = int(1e8)
sqN = int(N**0.5)
sq_sum = [i*(i+1)*(2*i+1)//6 for i in range(sqN+1)]

for i in range(sqN+1):
    for j in range(i+2, sqN+1):
        p = sq_sum[j] - sq_sum[i]
        if is_palindrome(p) and p < N:
            ans.add(p)

print(sum(ans))
