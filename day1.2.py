import re

with open("input1.txt") as f:
    lines = f.readlines()

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

calibration_values = []
for line in lines:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for val in numbers.keys():
            if line[i:].startswith(val):
                digits.append(numbers[val])
    calibration_values += [int(digits[0] + digits[-1])]

print(sum(calibration_values))
