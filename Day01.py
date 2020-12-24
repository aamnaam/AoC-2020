def two_nums(numbers):
    for front_num in numbers:
        for rear_num_index in range(len(numbers)-1, 0, -1):
            if front_num + numbers[rear_num_index] == 2020:
                return front_num * numbers[rear_num_index]


def three_nums(numbers):
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(len(numbers)-1, j, -1):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i] * numbers[j] * numbers[k]


def main():
    numbers = []
    with open("Day1", 'r') as f:
        [numbers.append(int(number)) for number in f.readlines()]
    numbers.sort()
    print("Part 1: ", two_nums(numbers))
    print("Part 2: ", three_nums(numbers))


if __name__ == '__main__':
    main()
