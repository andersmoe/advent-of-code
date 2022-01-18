def create_called_numbers(bingo_input):
    return [int(x) for x in bingo_input[0].split(",")]


def create_board(bingo_input, line_start):
    board = []
    for index in range(5):
        board.append([int(x) for x in bingo_input[line_start + index].split()])
    return board


def create_all_boards(bingo_input):
    boards = []
    current_line = 2

    while current_line < len(bingo_input):
        boards.append(create_board(bingo_input, current_line))
        current_line += 6

    return boards


def has_winning_row(board, called_numbers):
    for row in board:
        if all(number in called_numbers for number in row):
            return True
    return False


def has_winning_column(board, called_numbers):
    for column in list(zip(*board)):
        if all(number in called_numbers for number in column):
            return True
    return False


def sum_list(list_to_sum):
    total = 0
    for i in list_to_sum:
        total += i
    return total


def calculate_score(board, called_numbers):
    flat_board = sum(board, [])
    unmarked_numbers = list(set(flat_board).difference(called_numbers))
    return sum_list(unmarked_numbers) * called_numbers[-1]


def find_score_of_winning_board(boards, numbers_to_call):
    called_numbers = []
    for called_number in numbers_to_call:
        called_numbers.append(called_number)
        for board in boards:
            if has_winning_row(board, called_numbers):
                return calculate_score(board, called_numbers)
            elif has_winning_column(board, called_numbers):
                return calculate_score(board, called_numbers)


def main():
    bingo_input = open('input.txt').read().splitlines()

    called_numbers = create_called_numbers(bingo_input)
    boards = create_all_boards(bingo_input)

    winning_score = find_score_of_winning_board(boards, called_numbers)

    print("Answer: " + str(winning_score))


main()
