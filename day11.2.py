lines = open("input11.txt").read().splitlines()

empty_columns = []
for i in range(len(lines[0])):
    column = [line[i] for line in lines]
    if column.count(".") == len(column):
        empty_columns += [i]

empty_rows = []
galaxies = []
for i, line in enumerate(lines):
    if line.count(".") == len(line):
        empty_rows += [i]
    else:
        for j, char in enumerate(line):
            if char == "#":
                galaxies += [(i, j)]

sum = 0
for i, galaxy in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
        sum += abs(galaxy[0] - galaxies[j][0]) + abs(galaxy[1] - galaxies[j][1])
        for row in empty_rows:
            if min(galaxy[0], galaxies[j][0]) < row < max(galaxy[0], galaxies[j][0]):
                sum += 999999
        for column in empty_columns:
            if min(galaxy[1], galaxies[j][1]) < column < max(galaxy[1], galaxies[j][1]):
                sum += 999999
print(sum)
