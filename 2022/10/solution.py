import math

interesting_cycle = [20, 60, 100, 140, 180, 220]


def update_signal_strength(register_x, current_cycle, signal_strength):
    if current_cycle in interesting_cycle:
        return signal_strength + (current_cycle * register_x)
    return signal_strength


def draw_pixel(register_x, cycle, crt_line):
    cycle_in_line = cycle - (crt_line * 40)
    if cycle_in_line - 1 in list(range(register_x - 1, register_x + 2)):
        return "#"
    return "."


def main():
    instructions_input = open('input').read().splitlines()
    signal_strength = 0
    crt = [[], [], [], [], [], []]

    current_cycle = 0
    register_x = 1
    for instruction in instructions_input:
        if instruction.startswith("noop"):
            current_cycle += 1
            signal_strength = update_signal_strength(register_x, current_cycle, signal_strength)
            crt_line = math.floor((current_cycle-1)/40)
            crt[crt_line].append(draw_pixel(register_x, current_cycle, crt_line))
        else:
            _, value = instruction.split(" ")
            current_cycle += 1
            signal_strength = update_signal_strength(register_x, current_cycle, signal_strength)
            crt_line = math.floor((current_cycle-1)/40)
            crt[crt_line].append(draw_pixel(register_x, current_cycle, crt_line))
            current_cycle += 1
            signal_strength = update_signal_strength(register_x, current_cycle, signal_strength)
            crt_line = math.floor((current_cycle-1)/40)
            crt[crt_line].append(draw_pixel(register_x, current_cycle, crt_line))
            register_x += int(value)

    print("Answer part 1: {}".format(signal_strength))

    print("Answer part 2: ")
    for crt_line in crt:
        print(''.join(crt_line))


main()
