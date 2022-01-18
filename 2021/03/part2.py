def most_common_bit(column):
    counter = 0
    for c in column:
        if c == "0":
            counter -= 1
        else:
            counter += 1
    return "1" if counter >= 0 else "0"


def list_of_starts_with(input_list, starts_with):
    return list(filter(lambda x: "".join(x).startswith(starts_with), input_list))


def flip_bits(binary_string):
    return binary_string.translate(binary_string.maketrans("10", "01"))


def calculate_oxygen_rating(test_list, count, oxygen_rating):
    oxygenratingtest = oxygen_rating + most_common_bit(list(zip(*test_list))[count])
    newlist = list_of_starts_with(test_list, oxygenratingtest)
    if len(newlist) == 1:
        return "".join(newlist[0])
    count += 1
    return calculate_oxygen_rating(newlist, count, oxygenratingtest)


def calculate_co2_scrubber_rating(test_list, count, scrubber_rating):
    scubber_rating_test = scrubber_rating + flip_bits(most_common_bit(list(zip(*test_list))[count]))
    newlist = list_of_starts_with(test_list, scubber_rating_test)
    if len(newlist) == 1:
        return "".join(newlist[0])
    count += 1
    return calculate_co2_scrubber_rating(newlist, count, scubber_rating_test)


lines = open('input.txt').read().splitlines()
diagnosticInput = []
for line in lines:
    diagnosticInput.append([c for c in line])

oxygenRating = calculate_oxygen_rating(diagnosticInput, 0, "")
scrubberRating = calculate_co2_scrubber_rating(diagnosticInput, 0, "")

print("Answer: " + str(int(oxygenRating, 2) * int(scrubberRating, 2)))



