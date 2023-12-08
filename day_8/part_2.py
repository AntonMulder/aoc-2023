import math
import re

from utils.io import read


def run(puzzle_input):
    instructions, nodes = puzzle_input.split("\n\n")

    node_info = (
        re.search(r"(.+) = \((.+), (.+)\)", node).groups() for node in nodes.split("\n")
    )
    node_map = {id: {"L": left, "R": right} for id, left, right in node_info}

    nodes = [node for node in node_map.keys() if node.endswith("A")]
    number_of_start_nodes = len(nodes)

    steps = 0
    answer = []

    while len(answer) != number_of_start_nodes:
        step = instructions[steps % len(instructions)]

        steps += 1

        new_nodes = []
        for node in nodes:
            new_node = node_map[node][step]

            if new_node.endswith("Z"):
                answer.append(steps)
            else:
                new_nodes.append(new_node)

        nodes = new_nodes

    return math.lcm(*answer)


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
