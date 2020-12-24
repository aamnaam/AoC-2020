def get_some_yes(group_answer):
    question_ids = [False]*26
    for x in group_answer:
        if x != '\n':
            question_ids[ord(x)-97] = True
    return question_ids.count(True)


def get_all_yes(group_answer):
    individual_answers = group_answer.split("\n")
    num_members = len(individual_answers)
    question_ids = [0]*26
    for each_answer in individual_answers:
        for x in each_answer:             # checking each question number
            question_ids[ord(x)-97] += 1
    return question_ids.count(num_members)


def main():
    some_yes_sum = 0
    all_yes_sum = 0
    input_file = open("Day6").read()
    group_inputs = input_file.split("\n\n")
    for each_input in group_inputs:
        some_yes_sum += get_some_yes(each_input)
        all_yes_sum += get_all_yes(each_input)
    print("Part 1: ", some_yes_sum)
    print("Part 2: ", all_yes_sum)


if __name__ == '__main__':
    main()
    
