from collections import Counter

from utils.io import readlines


def run(puzzle_input):
    hands = (x.split(" ") for x in puzzle_input)

    def _add_order_to_cards(x: str) -> str:
        return (
            x.replace("T", "a")
            .replace("J", "1")
            .replace("Q", "c")
            .replace("K", "d")
            .replace("A", "e")
        )

    ordered_cards = ((_add_order_to_cards(x[0]), x[1]) for x in hands)

    def _fix_joker(cards: str) -> str:
        counts = sorted(Counter(cards).most_common(), key=lambda x: x[1], reverse=True)
        best_card = counts[0][0]

        if "1" in cards:
            if best_card == "1":
                for card in counts:
                    best_card = card[0]
                    if best_card != "1":
                        break
            cards = cards.replace("1", best_card)
        return cards

    fixed_cards = ((_fix_joker(x[0]), x[0], x[1]) for x in ordered_cards)

    def _get_score(cards: str) -> int:
        counts = sorted(Counter(cards).values())
        match counts:
            case [5]:  # Full house.
                return 6
            case [1, 4]:  # 4 of a kind.
                return 5
            case [2, 3]:  # Full house.
                return 4
            case [1, 1, 3]:  # 3 of a kind.
                return 3
            case [1, 2, 2]:  # 2 pairs.
                return 2
            case [1, 1, 1, 2]:  # 1 pair.
                return 1
            case _:  # Nothing.
                return 0

    scored_hands = ((_get_score(x[0]), x[1], x[2]) for x in fixed_cards)
    sorted_scored_hands = sorted(scored_hands, key=lambda x: (x[0], x[1]))

    answer = sum(
        idx * int(value)
        for idx, (_, _, value) in enumerate(sorted_scored_hands, start=1)
    )

    return answer


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
