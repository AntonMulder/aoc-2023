import re

from utils.io import readlines

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


def run(puzzle_input):
    answer = 0
    for data in puzzle_input:
        green_numbers = (int(x) for x in re.findall(r"(\d+) green", data))
        blue_numbers = (int(x) for x in re.findall(r"(\d+) blue", data))
        red_numbers = (int(x) for x in re.findall(r"(\d+) red", data))

        if (
            all(x <= GREEN_CUBES for x in green_numbers)
            and all(x <= BLUE_CUBES for x in blue_numbers)
            and all(x <= RED_CUBES for x in red_numbers)
        ):
            game_id = re.search(r"Game (\d+):", data).group(1)
            answer += int(game_id)

    return answer


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
