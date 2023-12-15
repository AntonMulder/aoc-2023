from functools import reduce

from utils.io import read


def run(puzzle_input):
    steps = puzzle_input.split(",")

    def _hash_algorithm(hash: str) -> int:
        return reduce(
            lambda previous, character: (previous + ord(character)) * 17 % 256, hash, 0
        )

    return sum(_hash_algorithm(step) for step in steps)


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
