import re
from itertools import cycle

from utils.io import read


def run(puzzle_input):
    instructions, nodes = puzzle_input.split("\n\n")

    node_info = (
        re.search(r"(.+) = \((.+), (.+)\)", node).groups() for node in nodes.split("\n")
    )
    node_map = {id: {"L": left, "R": right} for id, left, right in node_info}

    answer = 0
    current_node = "AAA"
    cycle_instructions = cycle(instructions)
    while current_node != "ZZZ":
        step = next(cycle_instructions)
        current_node = node_map[current_node][step]
        answer += 1

    return answer


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
