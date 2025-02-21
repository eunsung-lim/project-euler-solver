from base import is_palindrome

ans = 0

for n in range(1, 10000):
    cnt = 0
    x = n
    for _ in range(50):
        y = x + int(str(x)[::-1])
        if is_palindrome(y):
            break
        x = y
        cnt += 1
    if cnt == 50:
        ans += 1

print(ans)