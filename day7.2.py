from collections import Counter

lines = open("input7.txt").read().splitlines()

types = [[] for _ in range(7)]

for line in lines:
    hand, bid = line.split()
    nr_dif = len(set(hand))
    nr_jok = hand.count("J")
    most_common = Counter(hand).most_common(2)
    if most_common[0][1] == 5:
        nr_high = 5
    elif most_common[0][0] == "J":
        nr_high = most_common[1][1]
    else:
        nr_high = most_common[0][1]
    if nr_jok > 0 and nr_dif > 1:
        nr_dif -= 1
    if nr_dif == 1:
        types[6].append(line)
    elif nr_dif == 2:
        if nr_jok + nr_high == 4:
            types[5].append(line)
        else:
            types[4].append(line)
    elif nr_dif == 3:
        if nr_jok + nr_high == 3:
            types[3].append(line)
        else:
            types[2].append(line)
    elif nr_dif == 4:
        types[1].append(line)
    else:
        types[0].append(line)

lists = []
for type in types:
    lists.append(
        sorted(
            type,
            key=lambda word: ["AKQT98765432J10 ".index(c) for c in word],
            reverse=True,
        )
    )

total = 0
rank = 1
for t, type in enumerate(lists):
    if len(type) > 0:
        for line in type:
            hand, bid = line.split()
            total += int(bid) * rank
            rank += 1

print(total)
