from __future__ import annotations

FILENAME = "demo2_1.txt"  # expected 1
FILENAME = "demo2_2.txt"  # expected 5
FILENAME = "input.txt"
BASEMENT = -1
UP = "("
DOWN = ")"


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            floor = 0
            for index, symbol in enumerate(line):
                if symbol == UP:
                    floor += 1
                elif symbol == DOWN:
                    floor -= 1
                if floor == BASEMENT:
                    print(index + 1)
                    break


if __name__ == "__main__":
    main()
