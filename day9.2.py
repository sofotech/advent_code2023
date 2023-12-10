lines = open("input9.txt").read().splitlines()

sum = 0

for line in lines:
    numbers = [int(n) for n in line.split()]
    diff_list = [[(numbers[i + 1] - numbers[i]) for i in range(len(numbers) - 1)]]
    while diff_list[-1][0] != 0 or len(set(diff_list[-1])) > 1:
        diff_list.append(
            [
                (diff_list[-1][i + 1] - diff_list[-1][i])
                for i in range(len(diff_list[-1]) - 1)
            ]
        )
    diff_list[-1].append(0)
    if len(diff_list) > 1:
        for i in range(2, len(diff_list) + 1):
            diff_list[-i].append(diff_list[-i][0] - diff_list[-i + 1][-1])
    sum += numbers[0] - diff_list[0][-1]

print(sum)
