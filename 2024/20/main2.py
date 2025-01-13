from __future__ import annotations

# FILENAME, TIME = "demo.txt", 76  # expected 3
# FILENAME, TIME = "demo.txt", 7  # expected ?
# FILENAME, TIME = "demo.txt", 77  # expected 0
# FILENAME, TIME = "demo.txt", 74  # expected 4
FILENAME, TIME = "input.txt", 100
START = "S"
END = "E"
EMPTY = "."
WALL = "#"
INF = 100500
CHEAT_LENGTH = 20


def print_the_map(the_map: list[list[bool]], dist: dict[tuple[int, int], int]) -> None:
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            if (y, x) in dist:
                print(dist[(y, x)] % 10, end="")
            elif the_map[y][x]:
                print(EMPTY, end="")
            else:
                print(WALL, end="")
        print()


def f(
    the_map: list[list[bool]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> dict[tuple[int, int], int]:
    Q = {start}
    dist: dict[tuple[int, int], int] = dict()
    dist[start] = 0
    while len(Q) > 0:
        y0, x0 = Q.pop()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
                if the_map[y][x]:
                    if (y, x) not in dist or dist[(y0, x0)] + 1 < dist[(y, x)]:
                        dist[(y, x)] = dist[(y0, x0)] + 1
                        if (y0, x0) == end:
                            break
                        Q.add((y, x))
    return dist


def main() -> None:
    the_map: list[list[bool]] = []
    start = None
    end = None
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append([])
            for symbol in line.strip():
                if symbol == WALL:
                    the_map[-1].append(False)
                else:
                    if symbol == START:
                        if start is not None:
                            raise NotImplementedError
                        start = (len(the_map) - 1, len(the_map[-1]))
                    elif symbol == END:
                        if end is not None:
                            raise NotImplementedError
                        end = (len(the_map) - 1, len(the_map[-1]))
                    elif symbol != EMPTY:
                        raise NotImplementedError
                    the_map[-1].append(True)
    if start is None or end is None:
        raise NotImplementedError
    dist = f(the_map, start, end)
    base_value = dist[end]
    target_value = base_value - TIME
    result = set()
    for y0 in range(len(the_map)):
        for x0 in range(len(the_map[0])):
            if the_map[y0][x0] and dist[(y0, x0)] <= target_value:
                for dy in range(-CHEAT_LENGTH, CHEAT_LENGTH + 1):
                    y = y0 + dy
                    if 0 <= y < len(the_map):
                        for dx in range(
                            -CHEAT_LENGTH + abs(dy), CHEAT_LENGTH - abs(dy) + 1
                        ):
                            x = x0 + dx
                            if 0 <= x < len(the_map[0]) and the_map[y][x]:
                                p = abs(dy) + abs(dx)
                                if dist[(y, x)] - dist[(y0, x0)] - p >= TIME:
                                    result.add((y0, x0, y, x))
    # print(result)
    print(len(result))


if __name__ == "__main__":
    main()
