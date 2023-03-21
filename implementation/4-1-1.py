# L_x, R_x, U_x, D_x = [0, 0, -1, 1]
# L_y, R_y, U_y, D_y = [-1, 1, 0, 0]
spot_x = 1
spot_y = 1

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

move = ['L', 'R', 'U', 'D']
# spot = (1, 1)

n = int(input())
direct = map(str, input().split())

for i in direct:
    
    for j in range(len(move)):
        if (i==move[j]):
            spot_x+=move_x[j]
            if((spot_x>n)|(spot_x<1)):
                spot_x-=move_x[j]
            spot_y+=move_y[j]
            if((spot_y>n)|(spot_y<1)):
                spot_y-=move_y[j]

print(spot_x, spot_y)