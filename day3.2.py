import re, math

lines = open("input3.txt").read().splitlines()

numbers = set()
sum = 0

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "*":
            gearset = set()
            for rowNumber in [i - 1, i, i + 1]:
                for columnNumber in [j - 1, j, j + 1]:
                    if (
                        rowNumber >= 0
                        and columnNumber >= 0
                        and rowNumber < len(lines)
                        and columnNumber < len(lines[rowNumber])
                        and lines[rowNumber][columnNumber].isdigit()
                    ):
                        while (
                            columnNumber > 0
                            and lines[rowNumber][columnNumber - 1].isdigit()
                        ):
                            columnNumber -= 1
                        gearset.add((rowNumber, columnNumber))
            if len(gearset) == 2:
                gearratio = 1
                for number in gearset:
                    gearratio *= int(
                        re.search(r"\d+", lines[number[0]][number[1] :]).group(0)
                    )
                sum += gearratio

print(sum)
