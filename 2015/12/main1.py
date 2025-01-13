import re

# FILENAME = "demo1.txt"
FILENAME = "input.txt"


def f(line: str) -> int:
    return sum(map(int, re.findall(r"(-?\d+)", line)))


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
