
def calculate_calories_per_elf(calories_list):
    calories_per_elf = []
    current_calories = 0
    for line in calories_list:
        if line:
            current_calories += int(line)
        else:
            calories_per_elf.append(current_calories)
            current_calories = 0

    return calories_per_elf


def sum_top_three_elves(calories_per_elf):
    calories_per_elf.sort(reverse=True)
    print(calories_per_elf)
    return sum(calories_per_elf[:3])


def main():
    calories_list = open('input').read().splitlines()
    calories_list.append("")
    calories_per_elf = calculate_calories_per_elf(calories_list)
    top_three_elves = sum_top_three_elves(calories_per_elf)

    print("Answer: {}".format(top_three_elves))


main()
