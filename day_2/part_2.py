import re

from utils.io import readlines


def run(puzzle_input):
    answer = 0
    for data in puzzle_input:
        green_numbers = (int(x) for x in re.findall(r"(\d+) green", data))
        blue_numbers = (int(x) for x in re.findall(r"(\d+) blue", data))
        red_numbers = (int(x) for x in re.findall(r"(\d+) red", data))

        power_of_cubes = max(green_numbers) * max(red_numbers) * max(blue_numbers)
        answer += power_of_cubes

    return answer


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
