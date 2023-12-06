import re

from utils.io import readlines


def run(puzzle_input):
    time = int("".join(x for x in re.findall(r"\d+", next(puzzle_input))))
    distance = int("".join(x for x in re.findall(r"\d+", next(puzzle_input))))

    travelled = ((time - x) * x for x in range(0, time + 1))
    new_records = filter(lambda x: x > distance, travelled)
    return sum(1 for _ in new_records)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
