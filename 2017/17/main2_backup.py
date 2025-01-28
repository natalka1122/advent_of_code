from __future__ import annotations

FILENAME = "demo.txt"  # expected ?
FILENAME = "input.txt"

SPIN_COUNT = 50000000


class Value:
    def __init__(self, value: int, left: Value | None = None, right: Value | None = None):
        self.value = value
        if left is None:
            left = self
        if right is None:
            right = self
        self.left: Value = left
        self.right: Value = right

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return f"Value({self.value})"
        if self.left is not None and self.right is None:
            return f"{self.left.value}->Value({self.value})"
        if self.left is None and self.right is not None:
            return f"Value({self.value})->{self.right.value}"
        if self.left is not None and self.right is not None:
            return f"{self.left.value}->Value({self.value})->{self.right.value}"
        raise NotImplementedError


def f(step_count: int) -> int:
    current_position = Value(0)
    zero_position = current_position
    for index in range(SPIN_COUNT):
        for _ in range(step_count):
            current_position = current_position.right
        current_position_right = current_position.right
        new_value = Value(index + 1, left=current_position, right=current_position_right)
        current_position.right = new_value
        current_position_right.left = new_value
        current_position = new_value
        if index % 100000 == 0:
            print(index,zero_position.right)
        if current_position.left == zero_position:
            print(index,current_position)
    print(zero_position.right)
    return zero_position.right.value


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line)))


if __name__ == "__main__":
    main()
