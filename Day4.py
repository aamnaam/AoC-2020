import re
HEXDIGITS = ''.join(map(str, range(10))) + 'abcdef'
delimiters = '\n', ' ', ':'
regexPattern = '|'.join(map(re.escape, delimiters))
eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def part1(passport, ids):
    for idType in ids:
        if idType not in passport:
            return False
    return True


def part2(passport, ids):
    details = re.split(regexPattern, passport)
    for i in range(0, len(details), 2):
        if details[i] == "byr":
            if not 1920 <= int(details[i+1]) <= 2002:
                return False
        elif details[i] == "iyr":
            if not 2010 <= int(details[i+1]) <= 2020:
                return False
        elif details[i] == "eyr":
            if not 2020 <= int(details[i+1]) <= 2030:
                return False
        elif details[i] == "hgt":
            if details[i+1][-2:] == "in":
                if not 59 <= int(details[i + 1][:-2]) <= 76:
                    return False
            elif details[i+1][-2:] == "cm":
                if not 150 <= int(details[i + 1][:-2]) <= 193:
                    return False
        elif details[i] == "hcl":
            if not check_hcl(details[i+1]):
                return False
        elif details[i] == "ecl":
            if details[i+1] not in eye_colours:
                return False
        else:
            if not (details[i+1].isnumeric() and len(details[i+1]) == 9):
                return False
    return True


def check_hcl(hcl):
    return hcl[0] == '#' and all(map(lambda char: char in HEXDIGITS, hcl[1:]))


def main():
    passport_file = open("Day4", 'r').read()
    passports = passport_file.split('\n\n')
    num_of_valid1 = num_of_valid2 = 0
    ids = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for passport in passports:
        if part1(passport, ids):
            num_of_valid1 += 1
            if part2(passport, ids):
                num_of_valid2 += 1

    print("Part 1: ", num_of_valid1)
    print("Part 2: ", num_of_valid2)


if __name__ == '__main__':
    main()
