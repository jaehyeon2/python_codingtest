INF=int(1e9)

n, m = map(int, input().split())

array = [[INF]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            array[a][b]=0

for i in range(m):
    start, end = map(int, input().split())
    array[start][end]=1
    array[end][start]=1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            array[a][b] = min(array[a][b], array[a][k]+array[k][b])

x, k = map(int, input().split())

distance = array[1][k]+array[k][x]

if distance>=INF:
    print("-1")
else:
    print(distance)