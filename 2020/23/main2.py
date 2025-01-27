from __future__ import annotations

FILENAME, CUPS_COUNT, MOVES_COUNT = "demo.txt", 9, 100  # expected 42
FILENAME, CUPS_COUNT, MOVES_COUNT = "input.txt", 9, 100  # expected 63
FILENAME, CUPS_COUNT, MOVES_COUNT = "demo.txt", 1000000, 10000000  # expected 149245887792
FILENAME, CUPS_COUNT, MOVES_COUNT = "input.txt", 1000000, 10000000

ONE = 1


class Cup:
    def __init__(self, value: int, left: Cup | None = None, right: Cup | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return f"Cup({self.value})"
        if self.left is None and self.right is not None:
            return f"Cup({self.value})->{self.right.value}"
        if self.left is not None and self.right is None:
            return f"{self.left.value}->Cup({self.value})"
        if self.left is not None and self.right is not None:
            return f"{self.left.value}->Cup({self.value})->{self.right.value}"
        raise NotImplementedError


def do_the_needful(current_cup: Cup, cups_dict: dict[int, Cup]) -> Cup:
    three_cups_start = current_cup.right
    three_cups_end = three_cups_start.right.right
    three_cups_value = [three_cups_start.value, three_cups_start.right.value, three_cups_end.value]
    current_cup.right = three_cups_end.right
    three_cups_end.right.left = current_cup
    destitation_label = current_cup.value - 1
    if destitation_label not in cups_dict:
        destitation_label = max(cups_dict)
    while destitation_label in three_cups_value:
        destitation_label -= 1
        if destitation_label not in cups_dict:
            destitation_label = max(cups_dict)
    destitation_cup = cups_dict[destitation_label]
    after_destination = destitation_cup.right

    three_cups_start.left = destitation_cup
    destitation_cup.right = three_cups_start

    after_destination.left = three_cups_end
    three_cups_end.right = after_destination

    return current_cup.right


def main() -> None:
    cups_dict: dict[int, Cup] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            cups_init = tuple(map(lambda x: int(x), line))
    for index, cup in enumerate(cups_init):
        if cup in cups_dict:
            raise NotImplementedError
        if index == 0:
            cups_dict[cup] = Cup(cup)
            first_cup = cups_dict[cup]
        else:
            cups_dict[cup] = Cup(cup, left=last_cup)
            last_cup.right = cups_dict[cup]
        last_cup: Cup = cups_dict[cup]
    for index in range(len(cups_init) + 1, CUPS_COUNT + 1):
        cups_dict[index] = Cup(index, left=last_cup)
        last_cup.right = cups_dict[index]
        last_cup = cups_dict[index]
    last_cup.right = first_cup
    first_cup.left = last_cup
    current_cup = first_cup
    for _ in range(MOVES_COUNT):
        current_cup = do_the_needful(current_cup, cups_dict)
    one_cup = cups_dict[ONE]
    print(one_cup.right.value * one_cup.right.right.value)


if __name__ == "__main__":
    main()
