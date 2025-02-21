def orientation(x1, y1, x2, y2):
    t = x1*y2 - x2*y1
    return 0 if t == 0 else 1 if t > 0 else -1

triangles = []
cnt = 0

with open('0102_triangles.txt', 'r') as f:
    for line in f:
        x1,y1,x2,y2,x3,y3 = map(int, line.strip().split(','))
        triangles.append((x1,y1,x2,y2,x3,y3))
        if orientation(x1,y1,x2,y2) == orientation(x2,y2,x3,y3) == orientation(x3,y3,x1,y1):
            cnt += 1

print(cnt)
