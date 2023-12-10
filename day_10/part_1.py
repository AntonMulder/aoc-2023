from collections import defaultdict, deque

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

    answer = 0

    paths = deque([(start, 0)])
    visited = set()
    while paths:
        position, distance = paths.popleft()

        if position not in visited:
            visited.add(position)

            for neighbor in neighbors[position]:
                paths.append((neighbor, distance + 1))

            answer = max(answer, distance)

    return answer


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
