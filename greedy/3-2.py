n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

count=0
result=0

first = data[n-1]
second = data[n-2]

while(m!=0):
    if (count==k):
        count=0
        result+=second
    else:
        result+=first
        count+=1
    m-=1

print(result)
