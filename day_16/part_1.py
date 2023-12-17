from typing import NamedTuple

from utils.io import readlines


class Point(NamedTuple):
    y: int
    x: int

    def __add__(self, b: "Point") -> "Point":
        return Point(self.y + b.y, self.x + b.x)


RIGHT, DOWN, LEFT, UP = range(4)
DIRECTIONS = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]


def run(puzzle_input):
    map = list(puzzle_input)

    position = Point(0, 0)
    routes = [(position, 0)]
    visited_positions = set()

    while routes:
        position, direction = routes.pop(0)

        if (position, direction) not in visited_positions:
            visited_positions.add((position, direction))

            match map[position.y][position.x]:
                case ".":
                    directions = [direction]
                case "\\":
                    directions = [(direction + (-1) ** direction)]
                case "/":
                    directions = [UP - direction]
                case "-":
                    directions = (
                        [RIGHT, LEFT] if direction in (DOWN, UP) else [direction]
                    )
                case "|":
                    directions = [direction] if direction in (DOWN, UP) else [DOWN, UP]

            for direction in directions:
                new_position = position + DIRECTIONS[direction]
                if 0 <= new_position.y < len(map) and 0 <= new_position.x < len(map):
                    routes.append((new_position, direction))

    return len({position for position, _ in visited_positions})


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
