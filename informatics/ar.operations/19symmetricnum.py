v = int(input())

a = v // 1000
b = v // 100 % 10
c = v // 10 % 10
d = v % 10

s1 = (a - d) ** 2
s2 = (c - b) ** 2

print(s1 + s2 + 1)