array = [6, 3, 7, 4, 8, 5, 9, 1, 2]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
print(array)