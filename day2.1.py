with open("input2.txt") as f:
    lines = f.readlines()

maxColor = {
    "blue": 14,
    "red": 12,
    "green": 13,
}

sum = 0
for line in lines:
    gamenumber = int(line.split(":")[0].split()[1])
    draws = line.split(":")[1].split(";")
    gamePossible = True
    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            number, cube = color.split()
            if int(number) > maxColor[cube]:
                gamePossible = False
    if gamePossible:
        sum += gamenumber

print(sum)
