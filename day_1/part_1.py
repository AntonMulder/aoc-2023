import re

from utils.io import readlines


def run(puzzle_input):
    numbers = (re.findall(r"\d", x) for x in puzzle_input)
    combined_numbers = (f"{x[0]}{x[-1]}" for x in numbers)
    integer_numbers = (int(x) for x in combined_numbers)

    return sum(integer_numbers)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
