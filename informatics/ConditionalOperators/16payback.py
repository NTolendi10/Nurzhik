r1, k1, r2, k2 = int(input()), int(input()), int(input()), int(input())

r3 = r2 - r1
k3 = k2 - k1
if (k3 < 0):
    k3 = k3 + 100
    r3 = r3 - 1
print(r3, k3)