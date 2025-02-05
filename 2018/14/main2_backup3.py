from __future__ import annotations

FILENAME = "demo2.txt"  # expected 5 9 18 2018
# FILENAME = "demo2_5.txt"  # expected 5
FILENAME = "input.txt"

START1 = 3
START2 = 7
FIVE = 5


class Node:
    def __init__(
        self, value: int, index: int, left: Node | None = None, right: Node | None = None
    ) -> None:
        self.value = value
        self.index = index
        if left is None:
            self.left = self
        else:
            self.left = left
        if right is None:
            self.right = self
        else:
            self.right = right

    def __repr__(self):
        return f"({self.left.value},{self.left.index})->Node({self.value},{self.index})->({self.right.value},{self.right.index})"

    @property
    def get_prev_str(self) -> str:
        node = self
        result = ""
        for _ in range(FIVE):
            result += str(node.value)
            node = node.left
        return result[::-1]

    def add_node(self, value: int, index: int) -> Node:
        new_node = Node(value, index, left=self, right=self.right)
        self.right.left = new_node
        self.right = new_node
        return new_node


def f(target: str) -> int:
    start_node = Node(START1, 0)
    end_node = start_node.add_node(START2, 1)
    elf1 = start_node
    elf2 = end_node
    length = 2
    while end_node.get_prev_str != target:
        next_recipe = elf1.value + elf2.value
        if next_recipe >= 10:
            if next_recipe > 18:
                raise NotImplementedError
            end_node = end_node.add_node(next_recipe // 10, length)
            length += 1
        end_node = end_node.add_node(next_recipe % 10, length)
        length += 1
        for _ in range(elf1.value + 1):
            elf1 = elf1.right
        for _ in range(elf2.value + 1):
            elf2 = elf2.right
        if length % 1000000 in [0,1]:
            print(length)

        # line += next_recipe
        # index1 = (index1 + line[index1] + 1) % len(line)
        # index2 = (index2 + line[index2] + 1) % len(line)
        # print(line, line[-len(target) :], target, len(line)-len(target))
        # i += 1
    return length - len(target)


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
