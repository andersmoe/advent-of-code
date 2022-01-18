lines = open('input.txt').read().splitlines()
commands = [line.split(" ") for line in lines]

horizontal = 0
depth = 0
aim = 0

for commandLine in commands:
    command = commandLine[0]
    number = int(commandLine[1])

    if command == 'forward':
        horizontal += number
        depth += number * aim
    elif command == 'up':
        aim -= number
    elif command == 'down':
        aim += number

print("Answer: " + str(horizontal * depth))
