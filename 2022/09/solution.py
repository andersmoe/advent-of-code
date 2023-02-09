motions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def tuple_subtract(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))


def main():
    motion_input = open('input').read().splitlines()
    instructions = [line.split(" ") for line in motion_input]

    positions = [(0, 0)] * 10
    first_tail_postitions = set()
    last_tail_positions = set()

    for direction, number in instructions:
        for _ in range(int(number)):
            positions[0] = tuple(map(sum, zip(positions[0], motions[direction])))

            for i in range(1, len(positions)):
                before = positions[i-1]
                current = positions[i]

                head_tail_distance = tuple_subtract(before, current)
                if (abs(head_tail_distance[0]) > 1) or (abs(head_tail_distance[1]) > 1):
                    new_tail_x = current[0] + int(head_tail_distance[0] / max(1, abs(head_tail_distance[0])))
                    new_tail_y = current[1] + int(head_tail_distance[1] / max(1, abs(head_tail_distance[1])))
                    positions[i] = (new_tail_x, new_tail_y)

            first_tail_postitions.add(positions[1])
            last_tail_positions.add(positions[9])

    print("Answer part 1: {}".format(len(first_tail_postitions)))
    print("Answer part 2: {}".format(len(last_tail_positions)))


main()
