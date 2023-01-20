def find_priority(character):
    if character.isupper():
        return ord(character)-38
    else:
        return ord(character)-96


def find_item(rucksack):
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for item in list(first_compartment):
        if item in second_compartment:
            return item


def main():
    rucksacks = open('input').read().splitlines()

    answer = sum(list(map(find_priority, list(map(find_item, rucksacks)))))

    print("Answer: {}".format(answer))


main()
