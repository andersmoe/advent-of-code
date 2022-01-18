lines = open('input.txt').read().splitlines()
commands = [line.split(" ") for line in lines]

horizontal = 0
depth = 0
for command in commands:
    if command[0] == 'forward':
        horizontal = horizontal + int(command[1])
    elif command[0] == 'up':
        depth = depth - int(command[1])
    elif command[0] == 'down':
        depth = depth + int(command[1])

print("Horizontal: " + str(horizontal))
print("Depth: " + str(depth))
print("Answer: " + str(horizontal * depth))
