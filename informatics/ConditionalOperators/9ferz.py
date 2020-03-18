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

if (x1 == x2 or y1 == y2 or dx == dy):
    print("YES")
else:
    print("NO")