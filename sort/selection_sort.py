array = [6, 3, 7, 4, 8, 5, 9, 1, 2]

for i in range(len(array)):
    min_index=i
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[min_index], array[i] = array[i], array[min_index]

print(array)