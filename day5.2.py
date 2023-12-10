lines = open("input5.txt").read().splitlines()

sources = [int(n) for n in lines[0].split(":")[1].split()]
intervals = []
for i in range(len(sources) // 2):
    intervals.append((sources[2 * i], sources[2 * i] + sources[2 * i + 1] - 1))

maps = []
for l, line in enumerate(lines[1:]):
    if len(line) > 0 and line[0].isalpha():
        maps += [l + 1]
maps += [len(lines) + 1]

for i in range(len(maps) - 1):
    rangeslist = []
    for line in lines[maps[i] + 1 : maps[i + 1] - 1]:
        rangeslist.append([int(n) for n in line.split()])
    newcoordinateappendlist = []
    for ranges in rangeslist:
        removelist = []
        appendlist = []
        for interval in intervals:
            if interval[0] >= ranges[1] + ranges[2] or interval[1] < ranges[1]:
                continue
            elif interval[0] >= ranges[1] and interval[1] < ranges[1] + ranges[2]:
                # keep 1 part
                newcoordinateappendlist.append(
                    (
                        interval[0] + ranges[0] - ranges[1],
                        interval[1] + ranges[0] - ranges[1],
                    )
                )
            elif interval[0] >= ranges[1] and interval[1] >= ranges[1] + ranges[2]:
                # split in 2 parts
                newcoordinateappendlist.append(
                    (interval[0] + ranges[0] - ranges[1], ranges[0] + ranges[2] - 1)
                )
                appendlist.append((ranges[1] + ranges[2], interval[1]))
            elif interval[0] < ranges[1] and interval[1] < ranges[1] + ranges[2]:
                # split in 2 parts
                appendlist.append((interval[0], ranges[1] - 1))
                newcoordinateappendlist.append(
                    (ranges[0], interval[1] + ranges[0] - ranges[1])
                )
            elif interval[0] < ranges[1] and interval[1] >= ranges[1] + ranges[2]:
                # split in 3 parts
                appendlist.append((interval[0], ranges[1] - 1))
                newcoordinateappendlist.append((ranges[0], ranges[0] + ranges[2] - 1))
                appendlist.append((ranges[1] + ranges[2], interval[1]))
            removelist.append(interval)
        for j in removelist:
            if j in intervals:
                intervals.remove(j)
        for j in appendlist:
            intervals.append(j)
    for j in newcoordinateappendlist:
        intervals.append(j)
    if len(intervals) > 1:
        intervals.sort(key=lambda tup: tup[0])
        intervals2 = [intervals[0]]
        for interval in intervals[1:]:
            if intervals2[-1][0] <= interval[0] <= intervals2[-1][1]:
                poppedinterval = intervals2.pop()
                intervals2.append(
                    (poppedinterval[0], max(poppedinterval[1], interval[1]))
                )
            else:
                intervals2.append(interval)
        intervals = intervals2

minimum = intervals[0][0]
for interval in intervals:
    if interval[0] < minimum:
        minimum = interval[0]
print(minimum)
