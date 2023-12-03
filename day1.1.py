import re

with open("input1.txt") as f:
    lines = f.readlines()

calibration_values = []
for line in lines:
    digits = []
    for i, c in enumerate(line):
        digits = re.findall(r"\d", line)
    calibration_values += [int(digits[0] + digits[-1])]

print(sum(calibration_values))
