lines = open("input11.txt").read().splitlines()

empty_columns = []
for i in range(len(lines[0])):
    column = [line[i] for line in lines]
    if column.count(".") == len(column):
        empty_columns += [i]

empty_rows = []
for i, line in enumerate(lines):
    if line.count(".") == len(line):
        empty_rows += [i]

# expand columns
new_lines = []
for line in lines:
    new_line = list(line)
    for c in range(1, len(empty_columns) + 1):
        new_line.insert(empty_columns[-c], ".")
    new_lines.append(new_line)

# expand rows
for r in range(1, len(empty_rows) + 1):
    new_lines.insert(empty_rows[-r], ["."] * len(line))

galaxies = []
for i, line in enumerate(new_lines):
    for j, char in enumerate(line):
        if char == "#":
            galaxies += [(i, j)]

sum = 0
for i, galaxy in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
        sum += abs(galaxy[0] - galaxies[j][0])
        sum += abs(galaxy[1] - galaxies[j][1])
        dist = abs(galaxy[0] - galaxies[j][0])
        dist += abs(galaxy[1] - galaxies[j][1])
        print(dist)
print(sum)
