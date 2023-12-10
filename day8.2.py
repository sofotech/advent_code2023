import math

lines = open("input8.txt").read().splitlines()

directions = lines[0]
dirmap = {"L": 0, "R": 1}

network = {}

locations = []

for line in lines[2:]:
    start = line[:3]
    left = line[7:10]
    right = line[12:15]
    network.update({start: (left, right)})

    if line[2] == "A":
        locations.append(start)

lcm = 1
for location in locations:
    new_location = location
    steps = 0
    while new_location[2] != "Z":
        new_location = network[new_location][
            dirmap[directions[steps % len(directions)]]
        ]
        print(new_location)
        steps += 1
    lcm = abs(lcm * steps) // math.gcd(lcm, steps)

print(lcm)
