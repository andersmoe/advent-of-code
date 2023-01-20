scores = {'A X': 4,
          'A Y': 8,
          'A Z': 3,
          'B X': 1,
          'B Y': 5,
          'B Z': 9,
          'C X': 7,
          'C Y': 2,
          'C Z': 6}


def main():
    game_input = open('input').read().splitlines()

    total_score = 0
    for game in game_input:
        total_score += scores[game]

    print("Answer: {}".format(total_score))


main()
