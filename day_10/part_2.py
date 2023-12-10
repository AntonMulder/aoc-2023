from collections import defaultdict, deque

from shapely.geometry import Point, Polygon

from utils.io import read


def get_start_data(area):
    neighbors = defaultdict(list)
    for y in range(len(area)):
        for x in range(len(area[0])):
            position = (y, x)
            match area[y][x]:
                case "-":
                    neighbors[position].extend(((y, x - 1), (y, x + 1)))
                case "7":
                    neighbors[position].extend(((y + 1, x), (y, x - 1)))
                case "|":
                    neighbors[position].extend(((y - 1, x), (y + 1, x)))
                case "J":
                    neighbors[position].extend(((y - 1, x), (y, x - 1)))
                case "L":
                    neighbors[position].extend(((y - 1, x), (y, x + 1)))
                case "F":
                    neighbors[position].extend(((y + 1, x), (y, x + 1)))
                case "S":
                    start = position
    return start, neighbors


def run(puzzle_input):
    area = puzzle_input.split("\n")
    start, neighbors = get_start_data(area)

    neighbors[start] = [x for x in list(neighbors) if start in neighbors[x]]

    paths = deque([start])
    visited = set()
    while paths:
        position = paths.popleft()

        if position not in visited:
            visited.add(position)
            paths.extend(x for x in neighbors[position])

    # Compute loop. Order is important for the Polygon.
    loop_order = [start]
    while len(loop_order) < len(visited):
        for neighbor in neighbors[loop_order[-1]]:
            if neighbor not in loop_order:
                loop_order.append(neighbor)

    # Get all points that are in the loop.
    points = []
    for y in range(len(area)):
        for x in range(len(area[0])):
            if (y, x) not in loop_order:
                points.append(Point(y, x))

    # Count all points that are in the Polygon.
    poly = Polygon(loop_order)
    valid_points = filter(lambda x: poly.contains(x), points)
    return sum(1 for _ in valid_points)


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
