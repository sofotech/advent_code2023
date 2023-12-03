import re

lines = open("input3.txt").read().splitlines()

numbers = set()
sum = 0
symbols = set()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if not (char.isdigit() or char == "."):
            symbols.add((i, j))

for i, line in enumerate(lines):
    for n in re.finditer(r"\d+", line):
        edge = set()
        for row in [i - 1, i, i + 1]:
            for column in range(n.start() - 1, n.end() + 1):
                edge.add((row, column))
        if len(edge.intersection(symbols)) > 0:
            sum += int(n.group(0))

print(sum)
