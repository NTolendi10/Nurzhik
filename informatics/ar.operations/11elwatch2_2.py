n = int(input())

hours = n // 3600
n -= hours * 3600

minutes = n // 60
n -= minutes * 60

seconds = n

print(str(hours % 24) + ":" + str(minutes // 10) + str(minutes % 10) + ":" + str(seconds // 10) + str(seconds % 10))