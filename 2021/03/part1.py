def most_common_bit(column):
    counter = 0
    for c in column:
        if c == "0":
            counter -= 1
        else:
            counter += 1
    return "1" if counter > 0 else "0"


def flip_bits(binary_string):
    return binary_string.translate(binary_string.maketrans("10", "01"))


lines = open('input.txt').read().splitlines()
diagnosticInput = []
for line in lines:
    diagnosticInput.append([c for c in line])

columns = list(zip(*diagnosticInput))

gammaRateBinary = ""
for column in columns:
    gammaRateBinary += most_common_bit(column)
epsilonRateBinary = flip_bits(gammaRateBinary)

print("Answer " + str(int(gammaRateBinary, 2) * int(epsilonRateBinary, 2)))
