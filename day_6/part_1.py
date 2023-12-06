import re

from utils.io import readlines


def run(puzzle_input):
    times = (int(x) for x in re.findall(r"\d+", next(puzzle_input)))
    distances = (int(x) for x in re.findall(r"\d+", next(puzzle_input)))
    races = (race for race in zip(times, distances))

    answer = 1
    for time, distance in races:
        travelled = ((time - x) * x for x in range(0, time + 1))
        new_records = filter(lambda x: x > distance, travelled)
        answer *= sum(1 for _ in new_records)

    return answer


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
