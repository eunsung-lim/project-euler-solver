n = 1

while True:
    if sorted(str(n)) == sorted(str(n*2)) == sorted(str(n*3)) == sorted(str(n*4)) == sorted(str(n*5)) == sorted(str(n*6)):
        print(n)
        break
    n += 1

# 142857