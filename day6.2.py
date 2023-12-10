import math

lines = open("input6.txt").read().splitlines()

time = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))

x = max(0, math.floor((time - math.sqrt(pow(time, 2) - 4 * distance)) / 2))
y = math.floor((time + math.sqrt(pow(time, 2) - 4 * distance)) / 2)
if y == (time + math.sqrt(pow(time, 2) - 4 * distance)) / 2:
    print(y - x - 1)
else:
    print(y - x)
