x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x1 - x2
dy = y1 - y2

if(dx < 0):
    dx = -dx
if(dy < 0):
    dy = -dy

if(dx + dy == 1):
    print("YES")
else:
    if(dx + dy == 2 and dx == 1 and dy == 1):
        print("YES")
    else:
        print("NO")