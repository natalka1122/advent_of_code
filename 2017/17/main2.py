from __future__ import annotations

FILENAME = "demo.txt"  # expected ?
FILENAME = "input.txt"

SPIN_COUNT = 50000000


def f(step_count: int) -> int:
    current_position = 1
    current_length = 2
    current_value = 1
    result = 0
    for index in range(1, SPIN_COUNT):
        current_position = 1 + (current_position + step_count) % current_length
        current_length += 1
        current_value = index + 1
        if current_position == 1:
            result = current_value
            print(result)
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line)))


if __name__ == "__main__":
    main()
