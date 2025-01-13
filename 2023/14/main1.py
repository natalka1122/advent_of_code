from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
ROCK = "O"
STOPPER = "#"
EMPTY = "."


def f(platform):
    result = 0
    for y0 in range(len(platform)):
        for x0 in range(len(platform[0])):
            if platform[y0][x0] == ROCK:
                y = y0
                while y - 1 >= 0 and platform[y-1][x0] == EMPTY:
                    y -= 1
                if y != y0:
                    platform[y0][x0] = EMPTY
                    platform[y][x0] = ROCK
                result += len(platform) - y
    return result


def main():
    platform = []
    with open(FILENAME, "r") as file:
        for line in file:
            platform.append(list(line.strip()))
    print(f(platform))


if __name__ == "__main__":
    main()
