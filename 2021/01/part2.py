lines = open('input').read().splitlines()
int_lines = [int(i) for i in lines]

count = 0
for i in range(len(int_lines)-3):
    if sum(int_lines[i+1:i+4]) > sum(int_lines[i:i+3]):
        count += 1

print("Answer: {}".format(count))
