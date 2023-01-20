def overlap(assignment):
    int_assignments = [eval(i) for i in assignment]
    start1, end1, start2, end2 = int_assignments
    return not (end1 < start2 or end2 < start1)


def main():
    cleaning_input = open('input').read().splitlines()

    assignments = [assignments.replace(",", "-").split("-") for assignments in cleaning_input]

    answer = len(list(filter(overlap, assignments)))

    print("Answer: {}".format(answer))


main()
