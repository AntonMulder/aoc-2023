import re
from collections import defaultdict
from functools import reduce
from itertools import product

from utils.io import readlines


def run(puzzle_input):
    data = list(puzzle_input)

    def _get_neighbors(y, x):
        for delta_y, delta_x in product(range(-1, 2), range(-1, 2)):
            neighbor_y = y - delta_y
            neighbor_x = x - delta_x
            if (
                not (
                    (neighbor_y == y and neighbor_x == x)
                    or (neighbor_y < 0 or neighbor_y >= len(data))
                    or (neighbor_x < 0 or neighbor_x >= len(data[0]))
                )
                and data[neighbor_y][neighbor_x] == "*"
            ):
                yield ((neighbor_y, neighbor_x), data[neighbor_y][neighbor_x])

    gears = defaultdict(list)
    for y, row in enumerate(data):
        for number in re.finditer(r"\d+", row):
            for x in range(number.span()[0], number.span()[1]):
                try:
                    if gear := next(_get_neighbors(y, x)):
                        gears[gear[0]].append(int(number.group()))
                        break
                except StopIteration:
                    pass

    valid_gears = filter(lambda x: len(x) > 1, gears.values())
    answer = sum(reduce((lambda x, y: x * y), gear) for gear in valid_gears)
    return answer


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
