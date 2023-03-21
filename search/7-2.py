#binary_search
# n = int(input())
# array = list(map(int, input().split()))
# m = int(input())
# find = list(map(int, input().split()))

# def binary(array, target, start, end):
#     while start<=end:
#         mid = (start+end)//2
#         if array[mid]==target:
#             return 'yes'
#         elif array[mid]>target:
#             end=mid-1
#         else:
#             start=mid+1
#     return 'no'

# array.sort()

# for i in find:
#     print(binary(array, i, 0, n-1), end=" ")

#counting_sort
n = int(input())
array = [0]*1000001

for i in input().split():
    array[int(i)]=1

m=int(input())
for i in input().split():
    if array[int(i)]==1:
        print('yes', end=" ")
    else:
        print('no', end=" ")