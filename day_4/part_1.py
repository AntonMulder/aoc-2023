import re

from utils.io import readlines


def run(puzzle_input):
    cards = (game.split(":")[1] for game in puzzle_input)
    splitted_cards = (x.split("|") for x in cards)

    def _get_numbers(x):
        return set(re.findall(r"\d+", x))

    unique_numbers = ((_get_numbers(x[0]), _get_numbers(x[1])) for x in splitted_cards)
    overlap = (x[0].intersection(x[1]) for x in unique_numbers)
    matches = filter(lambda x: x, overlap)
    score = sum(2 ** (len(x) - 1) for x in matches)

    return score


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
