import re

from utils.io import readlines


def run(puzzle_input):
    pattern = r"\d|one|two|three|four|five|six|seven|eight|nine"
    all_matches = (re.finditer(f"(?=({pattern}))", x) for x in puzzle_input)
    raw_numbers = ((match.group(1) for match in matches) for matches in all_matches)

    mapper = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    all_as_numbers = ([mapper[y] if y in mapper else y for y in x] for x in raw_numbers)
    combined_numbers = (f"{x[0]}{x[-1]}" for x in all_as_numbers)
    integer_numbers = (int(x) for x in combined_numbers)

    return sum(integer_numbers)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
