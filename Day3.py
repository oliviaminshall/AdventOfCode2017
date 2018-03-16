# work out what layer current number is in
# no1 1 is layer 1 so 1 is highest value
# 3 x 3 is layer 2 so 9 is highest value
# 5 x 5 is layer 3 so 25 is highest value
# so work out highest value of each layer until above a max value that is higher than puzzle input - this defines what layer the puzzle input is in
# get steps from max value to puzzle input value


# part 1
puzinput = 361527
maxvalue = 1
layer = 0
rowlength = 1

while maxvalue < puzinput:
    layer = layer + 1
    rowlength = rowlength + 2
    maxvalue = rowlength * rowlength

distfromend = maxvalue - puzinput
side = int(distfromend / (rowlength-1)) # 0 = bottom, 1 = left, 2 = top, 3 = right
rem = distfromend % (rowlength-1)
x = rem + 1
y = 1 + (layer*2)
pos = (x,y)
origin = (layer,layer)
part1 = abs(pos[0] - origin[0]) + abs(pos[1] - origin[1])
print(part1)
