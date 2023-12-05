import re
import sys

from utils.io import read


def run(puzzle_input):
    data = puzzle_input.split("\n\n")

    # Get the seed numbers.
    seeds = [int(x) for x in re.findall(r"\d+", data.pop(0))]

    # Make rules
    set_of_rules = []
    for mapping in data:
        raw_rules = mapping.split("\n")[1:]
        rules = []
        for rule in raw_rules:
            destination, source, length = (int(x) for x in re.findall(r"\d+", rule))
            rules.append((destination, source, length))
        set_of_rules.append(rules)

    answer = sys.maxsize
    for range_start, length in zip(*[iter(seeds)] * 2):
        ranges = [(range_start, range_start + length)]
        for rules in set_of_rules:
            changed_ranges = []
            for destination, source, length in rules:
                new_ranges = []
                while ranges:
                    range_start, range_end = ranges.pop(0)

                    # Part before rule range.
                    if min(range_end, source) > range_start:
                        new_ranges.append((range_start, min(range_end, source)))

                    # Part in rule range.
                    in_rule_range = (
                        max(range_start, source),
                        min(source + length, range_end),
                    )
                    if in_rule_range[1] > in_rule_range[0]:
                        changed_ranges.append(
                            (
                                in_rule_range[0] - source + destination,
                                in_rule_range[1] - source + destination,
                            )
                        )

                    # Part after rule range.
                    if range_end > max(source + length, range_start):
                        new_ranges.append(
                            (max(source + length, range_start), range_end)
                        )

                ranges = new_ranges
            ranges += changed_ranges
        answer = min(answer, min(ranges)[0])
    return answer


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
