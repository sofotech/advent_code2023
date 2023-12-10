import math

lines = open("input6.txt").read().splitlines()

times = [int(t) for t in lines[0].split()[1:]]
distances = [int(d) for d in lines[1].split()[1:]]

power = 1
for i, t in enumerate(times):
    x = max(0, math.floor((t - math.sqrt(pow(t, 2) - 4 * distances[i])) / 2))
    y = math.floor((t + math.sqrt(pow(t, 2) - 4 * distances[i])) / 2)
    if y == (t + math.sqrt(pow(t, 2) - 4 * distances[i])) / 2:
        power *= y - x - 1
    else:
        power *= y - x

print(power)
