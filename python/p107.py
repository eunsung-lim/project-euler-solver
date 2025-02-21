distance = []

with open('0107_network.txt', 'r') as f:
    for line in f:
        row = []
        for x in line.strip().split(','):
            if x == '-':
                row.append(-1)
            else:
                row.append(int(x))
        distance.append(row)

n = len(distance)
total = 0
used = [False] * n
min_cost = [float('inf')] * n
min_cost[0] = 0

for _ in range(n):
    # Find minimum cost vertex not yet used
    u = -1
    for i in range(n):
        if not used[i] and (u == -1 or min_cost[i] < min_cost[u]):
            u = i
    
    used[u] = True
    
    # Update minimum costs
    for v in range(n):
        if distance[u][v] != -1 and not used[v]:
            min_cost[v] = min(min_cost[v], distance[u][v])

# Calculate total cost saved
original = 0
for i in range(n):
    for j in range(i+1, n):
        if distance[i][j] != -1:
            original += distance[i][j]

mst_cost = sum(min_cost[1:])
print(original - mst_cost)
