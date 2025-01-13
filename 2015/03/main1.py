from __future__ import annotations

# FILENAME = "demo1_1.txt"  # expected 2
# FILENAME = "demo1_2.txt"  # expected 4
# FILENAME = "demo1_3.txt"  # expected 2
FILENAME = "input.txt"
DIRECTIONS = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}


def main() -> None:
    y, x = 0, 0
    visited = {(y, x)}
    with open(FILENAME, "r") as file:
        for line in file:
            for symbol in line.strip():
                dy, dx = DIRECTIONS[symbol]
                y += dy
                x += dx
                visited.add((y, x))
    print(len(visited))


if __name__ == "__main__":
    main()
