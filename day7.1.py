lines = open("input7.txt").read().splitlines()

types = [[] for _ in range(7)]

for line in lines:
    hand, bid = line.split()
    nr_dif = len(set(hand))
    if nr_dif == 1:
        types[6].append(line)
    elif nr_dif == 2:
        if hand.count(hand[0]) % 3 == 1:
            types[5].append(line)
        else:
            types[4].append(line)
    elif nr_dif == 3:
        if hand.count(hand[0]) == 2 or hand.count(hand[1]) == 2:
            types[2].append(line)
        else:
            types[3].append(line)
    elif nr_dif == 4:
        types[1].append(line)
    else:
        types[0].append(line)

lists = []
for type in types:
    lists.append(
        sorted(
            type,
            key=lambda word: ["AKQJT9876543210 ".index(c) for c in word],
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
