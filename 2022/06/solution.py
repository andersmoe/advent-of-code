def find_marker(signal, marker_length):
    for i in range(len(signal) - marker_length + 1):
        if len(set(signal[i:i+marker_length])) == marker_length:
            return i + marker_length


def main():
    signal_input = open('input').read()
    print(signal_input)
    part1_answer = find_marker(signal_input, 4)

    part2_answer = find_marker(signal_input, 14)

    print("Answer part 1: {}".format(part1_answer))
    print("Answer part 2: {}".format(part2_answer))


main()
