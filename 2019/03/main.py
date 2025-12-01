# from __future__ import annotations

FILENAME = "demo1.txt"  # expected 6
FILENAME = "demo2.txt"  # expected 159
FILENAME = "demo3.txt"  # expected 135
# FILENAME = "input.txt"


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            print(line)
    print(result)


if __name__ == "__main__":
    main()
