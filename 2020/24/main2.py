import re

FILENAME = "demo.txt"  # expected 2208
FILENAME = "input.txt"

DIRECTIONS = {"e": (0, 2), "w": (0, -2), "nw": (-1, -1), "ne": (-1, 1), "sw": (1, -1), "se": (1, 1)}
STEPS_COUNT = 100


def calc(line: list[str]) -> tuple[int, int]:
    y, x = 0, 0
    for item in line:
        dy, dx = DIRECTIONS[item]
        y += dy
        x += dx
    return y, x


def count_nei(y: int, x: int, tiles: set[tuple[int, int]]) -> int:
    result = 0
    for dy, dx in DIRECTIONS.values():
        if (y + dy, x + dx) in tiles:
            result += 1
    return result


def make_move(tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    visited: set[tuple[int, int]] = set()
    for tile in tiles:
        if tile not in visited:
            nei = count_nei(tile[0], tile[1], tiles)
            if 1 <= nei <= 2:
                result.add(tile)
        for dy, dx in DIRECTIONS.values():
            current = (tile[0] + dy, tile[1] + dx)
            if current in visited:
                continue
            nei = count_nei(current[0], current[1], tiles)
            if current in tiles:
                if 1 <= nei <= 2:
                    result.add(current)
            else:
                if nei == 2:
                    result.add(current)
    return result


def main() -> None:
    tiles: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.findall(r"e|se|sw|w|nw|ne", line.strip())
            current = calc(line_match)
            if current in tiles:
                tiles.remove(current)
            else:
                tiles.add(current)
    # print(len(tiles), sorted(tiles))
    for _ in range(STEPS_COUNT):
        tiles = make_move(tiles)
    print(len(tiles))


if __name__ == "__main__":
    main()
