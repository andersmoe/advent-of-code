from itertools import islice


def create_start_state(cargo_input, to_index):
    stack_numbers = [eval(x) for x in cargo_input[to_index-1].split()]
    stacks = [[] for _ in range(max(stack_numbers))]

    initial_stacks = reversed(cargo_input[0:to_index-1])

    for cargo_line in initial_stacks:
        iterator = iter(cargo_line)
        stack_number = 0
        while x := list(islice(iterator, 4)):
            z = list(filter(lambda i: i.isalpha(), x))
            if z:
                stacks[stack_number].append(z.pop())
            stack_number += 1
    return stacks


def parse_instruction(instruction):
    splitstruction = instruction.split(" ")
    return int(splitstruction[1]), int(splitstruction[3])-1, int(splitstruction[5])-1


def move_crates(stacks, instructions):
    for instruction in instructions:
        number, from_stack, to_stack = parse_instruction(instruction)
        new_from_stack, crates_to_move = stacks[from_stack][:-number], stacks[from_stack][-number:]
        stacks[from_stack] = new_from_stack
        stacks[to_stack].extend(crates_to_move)


def main():
    cargo_input = open('input').read().splitlines()
    separator_index = next(index for index, line in enumerate(cargo_input) if not line)

    stacks = create_start_state(cargo_input, separator_index)
    move_crates(stacks, cargo_input[separator_index+1:])
    print(stacks)

    answer = ""
    for i in range(len(stacks)):
        answer += stacks[i][-1]

    print("Answer: {}".format(answer))


main()
