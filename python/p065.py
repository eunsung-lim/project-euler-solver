a = [1] * 200
b = [2] + sum([[1, 2*i, 1] for i in range(1, 100)], [])

A = [1, b[0]]
B = [0, 1]
for i in range(1, 101):
    p = b[i] * A[-1] + a[i] * A[-2]
    q = b[i] * B[-1] + a[i] * B[-2]
    A.append(p)
    B.append(q)

print(sum(int(d) for d in str(A[100])))