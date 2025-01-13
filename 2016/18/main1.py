from __future__ import annotations

FILENAME, ROWS = "demo1.txt", 3  # expected 6
FILENAME, ROWS = "demo2.txt", 10  # expected 38
FILENAME, ROWS = "input.txt", 40
EMPTY = "."
TRAP = "^"


def f(line: str) -> int:
    result = line.count(EMPTY)
    print(line)
    for _ in range(ROWS - 1):
        new_line = ""
        for x in range(len(line)):
            if x == 0:
                new_line += EMPTY if line[1] != TRAP else TRAP
            elif x == len(line) - 1:
                new_line += EMPTY if line[-2] != TRAP else TRAP
            else:
                new_line += EMPTY if line[x - 1] == line[x + 1] else TRAP
        line = new_line
        print(line)
        result += line.count(EMPTY)
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
