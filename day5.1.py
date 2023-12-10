lines = open("input5.txt").read().splitlines()

sources = [int(n) for n in lines[0].split(":")[1].split()]

maps = []
for l, line in enumerate(lines[1:]):
    if len(line) > 0 and line[0].isalpha():
        maps += [l + 1]
maps += [len(lines) + 1]

for i in range(len(maps) - 1):
    rangeslist = []
    for line in lines[maps[i] + 1 : maps[i + 1] - 1]:
        rangeslist.append([int(n) for n in line.split()])
    for s, source in enumerate(sources):
        for ranges in rangeslist:
            if ranges[1] <= source < ranges[1] + ranges[2]:
                sources[s] += ranges[0] - ranges[1]

print(min(sources))
