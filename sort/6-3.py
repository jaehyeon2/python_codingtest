n = int(input())

array = []
for i in range(n):
    value = input().split()
    array.append((value[0], int(value[1])))

array = sorted(array, key=lambda x:x[1])
for x in array:
    print(x[0], end=" ")