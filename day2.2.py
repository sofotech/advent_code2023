with open("input2.txt") as f:
    lines = f.readlines()

sumOfPowers = 0
for line in lines:
    draws = line.split(":")[1].split(";")
    requiredCubes = {
        "blue": 0,
        "red": 0,
        "green": 0,
    }
    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            number, cube = color.split()
            requiredCubes[cube] = max(int(number), requiredCubes[cube])
    power = requiredCubes["blue"] * requiredCubes["red"] * requiredCubes["green"]
    sumOfPowers += power

print(sumOfPowers)
