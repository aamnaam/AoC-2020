with open("Day3", 'r') as f:
    tree_map = f.read().split('\n')
repetition_width = len(tree_map[0])


def trees_faced(right, down):
    num_trees = i = j = 0
    while i < len(tree_map):
        if tree_map[i][j] == '#':
            num_trees += 1
        i += down
        j = (j + right) % repetition_width
    return num_trees


def main():
    print("Part 1: ", trees_faced(3, 1))
    print("Part 2: ", trees_faced(1, 1) * trees_faced(3, 1) * trees_faced(5, 1) * trees_faced(7, 1) * trees_faced(1, 2))


if __name__ == '__main__':
    main()
