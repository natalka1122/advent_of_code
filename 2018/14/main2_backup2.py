from __future__ import annotations

FILENAME = "demo2.txt"  # expected 9 5 18 2018
FILENAME = "input.txt"

START_LINE = [3, 7]
TEN = 5


class Node:
    def __init__(self, value: int, left: Node | None) -> None:
        self.value = value
        self


def f(target: str) -> str:
    target_tuple = tuple(map(int, target))
    index1 = 0
    index2 = 1
    line = list(START_LINE)
    while len(line) <= len(target) or tuple(line[-len(target) :]) != target_tuple:
        next_recipe = list(map(int, str(line[index1] + line[index2])))
        line += next_recipe
        index1 = (index1 + line[index1] + 1) % len(line)
        index2 = (index2 + line[index2] + 1) % len(line)
        # print(line, line[-len(target) :], target, len(line)-len(target))
        # i += 1
    return len(line) - len(target)


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
