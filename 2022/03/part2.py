from itertools import islice


def find_priority(character):
    if character.isupper():
        return ord(character)-38
    else:
        return ord(character)-96


def find_badge(sack_group):
    first_sack, second_sack, third_sack = sack_group[0], sack_group[1], sack_group[2]
    for item in list(first_sack):
        if item in second_sack and item in third_sack:
            return item


def group_sacks(rucksacks):
    groups = []
    iterator = iter(rucksacks)
    while group := list(islice(iterator, 3)):
        groups.append(group)
    return groups


def main():
    rucksacks = open('input').read().splitlines()

    answer = sum(list(map(find_priority, list(map(find_badge, group_sacks(rucksacks))))))

    print("Answer: {}".format(answer))


main()
