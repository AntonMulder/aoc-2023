import re
from collections import defaultdict

from utils.io import readlines


def run(puzzle_input):
    scores = defaultdict(lambda: 0)
    for card_id, numbers in enumerate(puzzle_input):
        scores[card_id] += 1
        _, numbers = numbers.split(":")
        winning_numbers, numbers_you_have = (
            set(re.findall(r"\d+", x)) for x in numbers.split("|")
        )
        overlap = winning_numbers.intersection(numbers_you_have)

        for next_card in range(1, len(overlap) + 1):
            scores[card_id + next_card] += scores[card_id]

    return sum(scores.values())


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
