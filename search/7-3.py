n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def cutting(array, target, start, end):
    while start<=end:
        total=0
        mid = (start+end)//2
        for i in array:
            if i>mid:
                total+=(i-mid)
        if total==target:
            return mid
        elif total>target:
            start=mid+1
        else:
            end=mid-1

print(cutting(array, target, 0, max(array)))