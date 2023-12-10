from matplotlib.path import Path

grid = open("input10.txt").read().splitlines()
for r, row in enumerate(grid):
    if "S" in row:
        s = (r, row.index("S"))

prev = s
cycle = [s]
if s[1] < len(grid[0]) - 1 and grid[s[0]][s[1] + 1] in "-J7":
    cycle.append((s[0], s[1] + 1))
elif s[0] < len(grid) - 1 and grid[s[0] + 1][s[1]] in "|LJ":
    cycle.append((s[0] + 1, s[1]))
elif s[1] > 0 and grid[s[0]][s[1] - 1] in "-LF":
    cycle.append((s[0], s[1] - 1))
else:
    cycle.append((s[0] - 1, s[1]))

while True:
    direction = grid[cycle[-1][0]][cycle[-1][1]]
    if direction == "-":
        if cycle[-1][1] > cycle[-2][1]:
            cycle.append((cycle[-1][0], cycle[-1][1] + 1))
        else:
            cycle.append((cycle[-1][0], cycle[-1][1] - 1))
    elif direction == "|":
        if cycle[-1][0] > cycle[-2][0]:
            cycle.append((cycle[-1][0] + 1, cycle[-1][1]))
        else:
            cycle.append((cycle[-1][0] - 1, cycle[-1][1]))
    elif direction == "L":
        if cycle[-1][0] == cycle[-2][0]:
            cycle.append((cycle[-1][0] - 1, cycle[-1][1]))
        else:
            cycle.append((cycle[-1][0], cycle[-1][1] + 1))
    elif direction == "J":
        if cycle[-1][0] == cycle[-2][0]:
            cycle.append((cycle[-1][0] - 1, cycle[-1][1]))
        else:
            cycle.append((cycle[-1][0], cycle[-1][1] - 1))
    elif direction == "7":
        if cycle[-1][0] == cycle[-2][0]:
            cycle.append((cycle[-1][0] + 1, cycle[-1][1]))
        else:
            cycle.append((cycle[-1][0], cycle[-1][1] - 1))
    elif direction == "F":
        if cycle[-1][0] == cycle[-2][0]:
            cycle.append((cycle[-1][0] + 1, cycle[-1][1]))
        else:
            cycle.append((cycle[-1][0], cycle[-1][1] + 1))
    elif direction == "S":
        break

tiles = 0
path = [(c[1], c[0]) for c in cycle]
p = Path(path)
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r, c) in cycle:
            continue
        if p.contains_point((c, r)):
            tiles += 1

print(tiles)
