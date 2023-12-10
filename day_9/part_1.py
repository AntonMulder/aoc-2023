from utils.io import readlines


def run(puzzle_input):
    answer = 0

    sequences = ([int(y) for y in x.split(" ")] for x in puzzle_input)

    def _get_differences(x: list[int]) -> list[int]:
        return [x[i] - x[i - 1] for i in range(1, len(x))]

    for sequence in sequences:
        difference = _get_differences(sequence)
        sub_sequences = [sequence, difference]

        while not all(x == 0 for x in difference):
            new_difference = _get_differences(difference)
            sub_sequences.append(new_difference)
            difference = new_difference

        answer += sum(x[-1] for x in sub_sequences)

    return answer


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
