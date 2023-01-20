scores = {'A X': 3,
          'A Y': 4,
          'A Z': 8,
          'B X': 1,
          'B Y': 5,
          'B Z': 9,
          'C X': 2,
          'C Y': 6,
          'C Z': 7}


def main():
    game_input = open('input').read().splitlines()

    total_score = 0
    for game in game_input:
        total_score += scores[game]

    print("Answer: {}".format(total_score))


main()
