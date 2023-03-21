array = [6, 3, 7, 4, 8, 5, 9, 1, 2]

def quick(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]

    return quick(left) + [pivot] + quick(right)

print(quick(array))