lines = open("input8.txt").read().splitlines()

directions = lines[0]
dirmap = {"L": 0, "R": 1}

network = {}

for line in lines[2:]:
    start = line[:3]
    left = line[7:10]
    right = line[12:15]
    network.update({start: (left, right)})

searching = True
steps = 0
location = "AAA"
while searching:
    for char in directions:
        steps += 1
        location = network[location][dirmap[char]]
        if location == "ZZZ":
            searching = False
            break

print(steps)
