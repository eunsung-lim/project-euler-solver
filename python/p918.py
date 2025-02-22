a_dict = {0: 4, 1: 1}

def a(n):
    if n in a_dict:
        return a_dict[n]
    if n%2 == 0:
        a_dict[n] = a(n//2) * 2
    else:
        a_dict[n] = a(n//2) - 3 * a(n//2+1)
    return a_dict[n]

def S(n):
    if n%2 == 0:
        return a(0) - a(n//2)
    else:
        return a(0) - a(n//2) + a(n)

print(S(int(1e12)))