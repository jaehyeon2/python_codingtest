# n, m = map(int, input().split())
# spot_x, spot_y, direction = map(int, input().split())

# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# visited = [[0] * m for _ in range(n)]
# visited[spot_x][spot_y] = 1

# move_x = [-1, 0, 1, 0]
# move_y = [0, 1, 0, -1]

# visit_count=1
# ttime=0
# while (True):
#     direction = (direction+3)%4
    
#     temp_x = spot_x+move_x[direction]
#     temp_y = spot_y+move_y[direction]

#     if array[temp_x][temp_y]==0 & visited[temp_x][temp_y]==0:
#         spot_x=temp_x
#         spot_y=temp_y
#         ttime=0
#         visited[spot_x][spot_y]=1
#         visit_count+=1
#         continue
#     else:
#         ttime+=1
    
#     if ttime==4:
#         temp_x = spot_x-move_x[direction]
#         temp_y = spot_y-move_y[direction]
#         if array[temp_x][temp_y]==0:
#             spot_x = temp_x
#             spot_y = temp_y
#         else:
#             break
#         ttime=0
    
#     print(spot_x, spot_y)

# print(visit_count)

n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_time=0
visit_count=1
while True:
    direction = (direction+3)%4
    nx = x+dx[direction]
    ny = y+dy[direction]
    if d[nx][ny]==0 and array[nx][ny]==0:
        x=nx
        y=ny
        turn_time=0
        d[x][y]=1
        visit_count+=1
    else:
        turn_time+=1
    
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if(array[nx][ny]==1):
            break
        else:
            x=nx
            y=ny
        turn_time=0

print(visit_count)