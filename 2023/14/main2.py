from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
ROCK = "O"
STOPPER = "#"
EMPTY = "."
CYCLES_COUNT = 1000000000 - 1


def tilt_north(platform) -> None:
    for y0 in range(len(platform)):
        for x0 in range(len(platform[0])):
            if platform[y0][x0] == ROCK:
                y = y0
                while y - 1 >= 0 and platform[y - 1][x0] == EMPTY:
                    y -= 1
                if y != y0:
                    platform[y0][x0] = EMPTY
                    platform[y][x0] = ROCK


def tilt_west(platform) -> None:
    for x0 in range(len(platform[0])):
        for y0 in range(len(platform)):
            if platform[y0][x0] == ROCK:
                x = x0
                while x - 1 >= 0 and platform[y0][x - 1] == EMPTY:
                    x -= 1
                if x != x0:
                    platform[y0][x0] = EMPTY
                    platform[y0][x] = ROCK


def tilt_south(platform) -> None:
    for y0 in range(len(platform) - 1, -1, -1):
        for x0 in range(len(platform[0])):
            if platform[y0][x0] == ROCK:
                y = y0
                while y + 1 < len(platform) and platform[y + 1][x0] == EMPTY:
                    y += 1
                if y != y0:
                    platform[y0][x0] = EMPTY
                    platform[y][x0] = ROCK


def tilt_east(platform) -> None:
    for x0 in range(len(platform[0]) - 1, -1, -1):
        for y0 in range(len(platform)):
            if platform[y0][x0] == ROCK:
                x = x0
                while x + 1 < len(platform[y0]) and platform[y0][x + 1] == EMPTY:
                    x += 1
                if x != x0:
                    platform[y0][x0] = EMPTY
                    platform[y0][x] = ROCK


def calc(platform) -> int:
    result = 0
    for y in range(len(platform)):
        for x in range(len(platform[0])):
            if platform[y][x] == ROCK:
                result += len(platform) - y
    return result


def hash_me(platform):
    return hash("".join(map(str, platform)))


def f(platform):
    results = list()
    calcs = list()
    for i in range(CYCLES_COUNT):
        tilt_north(platform)
        tilt_west(platform)
        tilt_south(platform)
        tilt_east(platform)
        current_hash = hash_me(platform)
        if current_hash not in results:
            results.append(current_hash)
            calcs.append(calc(platform))
        else:
            previous = results.index(current_hash)
            target = previous + (CYCLES_COUNT - previous) % (i - previous)
            return calcs[target]
    print("\n".join(map(lambda x: "".join(x), platform)))
    return calc(platform)


def main():
    platform = []
    with open(FILENAME, "r") as file:
        for line in file:
            platform.append(list(line.strip()))
    print(f(platform))


if __name__ == "__main__":
    main()
