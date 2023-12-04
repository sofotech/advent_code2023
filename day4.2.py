import re, math

lines = open("input4.txt").read().splitlines()
cards = [1] * len(lines)

for l, line in enumerate(lines):
    winning, got = line.split(":")[1].split("|")
    winningNumbers = set(re.findall(r"\d+", winning))
    gotNumbers = set(re.findall(r"\d+", got))
    wins = winningNumbers.intersection(gotNumbers)
    for i in range(len(wins)):
        if l + i + 1 < len(cards):
            cards[l + i + 1] += cards[l]


print(sum(cards))
