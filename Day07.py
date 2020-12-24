all_rules = open("Day7", 'r').read().split("\n")
rule_map = {rule.split(" contain ")[0][:-5]: rule.split(" contain ")[1] for rule in all_rules}


def contains_sg(colour):
    if "no other bag" not in rule_map[colour]:
        if "shiny gold" in rule_map[colour]:
            return True
        bags = rule_map[colour].split(', ')
        colours = []
        for each_bag in bags:
            x = each_bag.split(' ')
            colours.append(x[1] + ' ' + x[2])
        for bag_colour in colours:
            if contains_sg(bag_colour):
                return True
    return False


def count_bags(n):
    if "no other bag" not in rule_map[n]:
        bags = rule_map[n].split(", ")
        total = 0
        for each_bag in bags:
            x = each_bag.split(' ')
            total += int(x[0]) + (int(x[0])*count_bags(x[1] + ' ' + x[2]))
        return total
    return 0


def main():
    total = 0
    for x in rule_map.keys():
        if contains_sg(x):
            total += 1
    print("Part 1: ", total)
    print("Part 2: ", count_bags("shiny gold"))


if __name__ == '__main__':
    main()
