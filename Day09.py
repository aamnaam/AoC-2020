number_list = []
with open("Day9", 'r') as f:
    for each_number in f.readlines():
        number_list.append(int(each_number))
preamble = 25
total_nums = len(number_list)

for i in range(preamble, total_nums):
    flag = False
    for j in range(i-preamble, i):
        for k in range(j, i):
            flag = flag or number_list[i] == number_list[j] + number_list[k]
            if flag:
                break
        if flag:
            break
    if not flag:
        part1 = number_list[i]
        break

for i in range(total_nums):
    num_terms = 2
    while i + num_terms < total_nums and sum(number_list[i:i+num_terms]) <= part1:
        num_terms += 1
    if sum(number_list[i:i+num_terms-1]) == part1:
        part2 = max(number_list[i:i+num_terms-1]) + min(number_list[i:i+num_terms-1])
        break

print("Part 1: ", part1)
print("Part 2: ", part2)
