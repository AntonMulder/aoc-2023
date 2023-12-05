import re
from dataclasses import dataclass

from utils.io import read


@dataclass
class Rule:
    destination: int
    source: int
    length: int

    def in_range(self, x):
        if self.source <= x < self.source + self.length:
            offset = x - self.source
            return self.destination + offset
        return None


def run(puzzle_input):
    data = puzzle_input.split("\n\n")

    # Get the seed numbers.
    seeds = [int(x) for x in re.findall(r"\d+", data.pop(0))]

    # Make rules
    set_of_rules = []
    for mapping in data[:7]:
        raw_rules = mapping.split("\n")[1:]
        rules = []
        for rule in raw_rules:
            destination, source, length = (int(x) for x in re.findall(r"\d+", rule))
            rules.append(Rule(destination, source, length))
        set_of_rules.append(rules)

    # Find the lowest location.
    locations = []
    for seed in seeds:
        for rules in set_of_rules:
            for rule in rules:
                if new_seed := rule.in_range(seed):
                    seed = new_seed
                    break
        locations.append(seed)

    return min(locations)


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
