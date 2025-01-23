import re

FILENAME = "demo.txt"  # expected 10
FILENAME = "input.txt"

DIRECTIONS = {"e": (0, 2), "w": (0, -2), "nw": (-1, -1), "ne": (-1, 1), "sw": (1, -1), "se": (1, 1)}


def f(line: list[str]) -> tuple[int, int]:
    y, x = 0, 0
    for item in line:
        dy, dx = DIRECTIONS[item]
        y += dy
        x += dx
    return y, x


def main() -> None:
    result: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.findall(r"e|se|sw|w|nw|ne", line.strip())
            current = f(line_match)
            if current in result:
                result.remove(current)
            else:
                result.add(current)
    print(len(result))


if __name__ == "__main__":
    main()
