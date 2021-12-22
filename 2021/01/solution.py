lines = open('input').read().splitlines()
int_lines = [int(i) for i in lines]

count = 0
lastline = int_lines.pop(0)

for nextline in int_lines:
    if nextline > lastline:
        count += 1
    lastline = nextline

print("Answer: {}".format(count))

