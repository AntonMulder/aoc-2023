from utils.io import read


def run(puzzle_input):
    data = puzzle_input.split("\n")

    galaxies = [
        (y, x)
        for y, row in enumerate(data)
        for x, value in enumerate(row)
        if value == "#"
    ]

    rows_with_galaxies = {x[0] for x in galaxies}
    rows_to_expand = [x for x in range(len(data[0])) if x not in rows_with_galaxies]

    columns_with_galaxies = {x[1] for x in galaxies}
    columns_to_expand = [
        x for x in range(len(data[0])) if x not in columns_with_galaxies
    ]

    answer = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            y_1, x_1 = galaxies[i]
            y_2, x_2 = galaxies[j]

            w = abs(x_1 - x_2)
            h = abs(y_1 - y_2)

            x_1, x_2 = sorted([x_1, x_2])
            cols = sum(1 for x in range(x_1, x_2) if x in columns_to_expand)

            y_1, y_2 = sorted([y_1, y_2])
            rows = sum(1 for y in range(y_1, y_2) if y in rows_to_expand)

            answer += w + h + 1 * (cols + rows)

    return answer


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
