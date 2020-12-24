index_dict = {}
numbers = [0, 12, 6, 13, 20, 1, 17]
turn_num = 6
for i in range(turn_num):
    index_dict.update({numbers[i]: i})

print("Running: ")

while len(numbers) < 30000000:
    if numbers[turn_num] not in numbers[:-1]:
        numbers.append(0)
    else:
        numbers.append(turn_num - index_dict.get(numbers[turn_num]))
    index_dict.update({numbers[turn_num]: turn_num})
    turn_num += 1

print("Part 1: ", numbers[2020 - 1])
print("Part 2: ", numbers[30000000 - 1])
