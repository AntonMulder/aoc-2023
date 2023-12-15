import re
from functools import reduce

from utils.io import read


def run(puzzle_input):
    steps = puzzle_input.split(",")

    boxes = [{} for _ in range(256)]

    def _hash_algorithm(hash: str) -> int:
        return reduce(
            lambda previous, character: (previous + ord(character)) * 17 % 256, hash, 0
        )

    for step in steps:
        label, operation, focal_length = re.search(r"(\w+)(=|-)(\d*)", step).groups()
        box_number = _hash_algorithm(label)

        match operation:
            case "=":
                boxes[box_number][label] = int(focal_length)
            case "-":
                boxes[box_number].pop(label, None)

    answer = 0
    for box_number, box in enumerate(boxes, start=1):
        answer += sum(
            box_number * slot_number * int(lens_value)
            for slot_number, lens_value in enumerate(box.values(), start=1)
        )

    return answer


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
