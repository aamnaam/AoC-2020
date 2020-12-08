instructions = open("Day8", 'r').read().split("\n")
num_instructions = len(instructions)


def run_instructions():
    has_run = [False] * num_instructions
    acc = 0
    i = 0
    while 0 <= i < num_instructions:
        if has_run[i]:
            return "Non-terminating"        # break for part-1
        command = instructions[i][:3]
        parameter = int(instructions[i][4:])
        has_run[i] = True
        if command == "acc":
            acc += parameter
        elif command == "jmp":
            if 0 <= parameter + i <= num_instructions:
                i += parameter-1
        i += 1
    return f"{acc}"


def interchange():
    for i in range(num_instructions):
        original = instructions
        if instructions[i][:3] == "jmp":
            instructions[i] = instructions[i].replace("jmp", "nop")
            result = run_instructions()
            if result.isnumeric():
                break
            else:
                instructions[i] = instructions[i].replace("nop", "jmp")
        elif instructions[i][:3] == "nop":
            instructions[i] = instructions[i].replace("nop", "jmp")
            result = run_instructions()
            if result.isnumeric():
                break
            else:
                instructions[i] = instructions[i].replace("jmp", "nop")
    return result


def main():
    print(interchange())


if __name__ == '__main__':
    main()
