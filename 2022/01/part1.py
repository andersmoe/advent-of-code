lines = open('input').read().splitlines()
lines.append("")

max_calories = 0
current_calories = 0

for line in lines:
    if line:
        current_calories += int(line)
    else:
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0

print("Answer: {}".format(max_calories))

