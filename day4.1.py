import re, math

lines = open("input4.txt").read().splitlines()
sum = 0

for line in lines:
    winning, got = line.split(":")[1].split("|")
    winningNumbers = set(re.findall(r"\d+", winning))
    gotNumbers = set(re.findall(r"\d+", got))
    wins = winningNumbers.intersection(gotNumbers)
    if len(wins) > 0:
        sum += 1 * int(math.pow(2, len(wins) - 1))

print(sum)
