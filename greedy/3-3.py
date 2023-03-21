n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minimal = min(data)
    result = max(result, minimal)

print(result)