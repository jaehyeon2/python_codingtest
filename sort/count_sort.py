array = [6, 3, 7, 4, 8, 5, 9, 1, 2, 128, 234, 234, 254, 142]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")