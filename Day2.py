def is_valid_p1(min_num, max_num, character, pw):
    if min_num <= pw.count(character) <= max_num:
        return True
    return False


def is_valid_p2(index1, index2, character, pw):
    if (pw[index1 - 1] == character and pw[index2 - 1] != character) or (
            pw[index1 - 1] != character and pw[index2 - 1] == character):
        return True
    return False


def main():
    part1 = part2 = 0
    with open("Day2", 'r') as f:
        passwords = f.readlines()

    for password in passwords:
        hyphen = password.index('-')
        colon = password.index(':')
        param1 = int(password[:hyphen])
        param2 = int(password[hyphen + 1: colon - 2])
        character = password[colon - 1]
        pw = password[colon + 2:]
        if is_valid_p1(param1, param2, character, pw):
            part1 += 1
        if is_valid_p2(param1, param2, character, pw):
            part2 += 1

    print("Part 1: ", part1)
    print("Part 2: ", part2)


if __name__ == '__main__':
    main()
