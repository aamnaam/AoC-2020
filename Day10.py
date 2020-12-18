adapter_ratings = []
with open("Day10", 'r') as f:
    inputs = f.readlines()
    [adapter_ratings.append(int(adapter)) for adapter in inputs]


def count_diff():
    diff1 = 1
    diff3 = 1
    for i in range(1, len(adapter_ratings)):
        if adapter_ratings[i] - adapter_ratings[i-1] == 1:
            diff1 += 1
        elif adapter_ratings[i] - adapter_ratings[i-1] == 3:
            diff3 += 1
    return [diff1, diff3]


def count_combos(data, index):
    num = 0
    if index == len(data) - 1:
        num += 1
        return num
    if index <= len(data) - 2:
        if data[index+1] - data[index] <= 3:
            num += count_combos(data, index+1)
    if index <= len(data) - 3:
        if data[index+2] - data[index] <= 3:
            num += count_combos(data, index+2)
    if index <= len(data) - 4:
        if data[index+3] - data[index] <= 3:
            num += count_combos(data, index+3)
    return num


def main():
    adapter_ratings.sort()
    print("Part 1: ", count_diff())
    print("Part 2: ", count_combos(adapter_ratings, 0))


if __name__ == '__main__':
    main()
