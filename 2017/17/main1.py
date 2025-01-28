from __future__ import annotations

FILENAME = "demo.txt"  # expected 638
FILENAME = "input.txt"

SPIN_COUNT = 2017


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
    for index in range(SPIN_COUNT):
        for _ in range(step_count):
            current_position = current_position.right
        current_position_right = current_position.right
        new_value = Value(index + 1, left=current_position, right=current_position_right)
        current_position.right = new_value
        current_position_right.left = new_value
        current_position = new_value
    print(new_value.right)
    return new_value.right.value


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line)))


if __name__ == "__main__":
    main()
