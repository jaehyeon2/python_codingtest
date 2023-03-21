move_row = [2, 2, 1, 1, -1, -1, -2, -2]
move_col = [1, -1, 2, -2, 1, -1, 2, -2]

spot = input()
spot_row = int(spot[1])
spot_col = int(ord(spot[0])-ord('a')+1)

count = 0

for i in range(8):
    if ((spot_row+move_row[i]<1)|(spot_row+move_row[i]>8)|(spot_col+move_col[i]<1)|(spot_col+move_col[i]>8)):
        continue
    count+=1

print(count)
