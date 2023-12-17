from typing import NamedTuple

from utils.io import readlines


class Point(NamedTuple):
    y: int
    x: int

    def __add__(self, b: "Point") -> "Point":
        return Point(self.y + b.y, self.x + b.x)


RIGHT, DOWN, LEFT, UP = range(4)
DIRECTIONS = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]


def energized_tiles(map: list[str], position: Point, direction: int) -> int:
    routes = [(position, direction)]
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


def run(puzzle_input):
    map = list(puzzle_input)

    results = []
    width = len(map)
    height = len(map[0])
    for y in range(height):
        for x in range(width):
            if y not in {0, height - 1} and x not in {0, width - 1}:
                continue

            directions = []
            directions.append(DOWN if y == 0 else UP)
            directions.append(LEFT if x == 0 else RIGHT)

            for direction in directions:
                results.append(energized_tiles(map, Point(y, x), direction))
    return max(results)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
