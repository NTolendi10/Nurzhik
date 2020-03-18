n = int(input())
k = 0

for i in range(1, n + 1):
    m = int(input())
    if m == 0:
        k += 1

print(k)