from functools import reduce

def f(n):
    # return n**3
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

u = [f(n) for n in range(11)]

def op(k):
    # g(k) = u(k) for k in [1, 2, ..., k]
    def g(x):
        return sum([
			u[i] * reduce(lambda p, q: p*q, [(x-j)/(i-j) for j in range(1, k+1) if i != j], 1)
			for i in range(1, k+1)
		])
    return g

print(sum(round(op(i)(i+1)) for i in range(1, 11)))
# 37076114526