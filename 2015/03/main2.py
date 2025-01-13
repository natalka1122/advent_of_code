from __future__ import annotations

# FILENAME = "demo2_1.txt"  # expected 3
# FILENAME = "demo2_2.txt"  # expected 3
# FILENAME = "demo2_3.txt"  # expected 11
FILENAME = "input.txt"
DIRECTIONS = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}


def main() -> None:
    y1, x1 = 0, 0
    y2, x2 = 0, 0
    visited = {(y1, x1)}
    with open(FILENAME, "r") as file:
        for line in file:
            for index, symbol in enumerate(line.strip()):
                dy, dx = DIRECTIONS[symbol]
                if index % 2 == 0:
                    y1 += dy
                    x1 += dx
                    visited.add((y1, x1))
                else:
                    y2 += dy
                    x2 += dx
                    visited.add((y2, x2))
    print(len(visited))


if __name__ == "__main__":
    main()
