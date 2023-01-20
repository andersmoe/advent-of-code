def contains(assignment):
    int_assignments = [eval(i) for i in assignment]
    start1, end1, start2, end2 = int_assignments
    return ((start1 >= start2 and end1 <= end2) or
            (start1 <= start2 and end1 >= end2))


def main():
    cleaning_input = open('input').read().splitlines()

    assignments = [assignments.replace(",", "-").split("-") for assignments in cleaning_input]

    answer = len(list(filter(contains, assignments)))

    print("Answer: {}".format(answer))


main()
