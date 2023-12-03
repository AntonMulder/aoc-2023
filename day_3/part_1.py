import re
from itertools import product

from utils.io import readlines

ALLOWED_CHARACTERS = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def run(puzzle_input):
    data = list(puzzle_input)

    def _get_neighbors(y, x):
        for delta_y, delta_x in product(range(-1, 2), range(-1, 2)):
            neighbor_y = y - delta_y
            neighbor_x = x - delta_x
            if not (
                (neighbor_y == y and neighbor_x == x)
                or (neighbor_y < 0 or neighbor_y >= len(data))
                or (neighbor_x < 0 or neighbor_x >= len(data[0]))
            ):
                yield data[neighbor_y][neighbor_x]

    answer = 0
    for y, row in enumerate(data):
        for number in re.finditer(r"\d+", row):
            for x in range(number.span()[0], number.span()[1]):
                if not all(x in ALLOWED_CHARACTERS for x in _get_neighbors(y, x)):
                    answer += int(number.group())
                    break
    return answer


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
