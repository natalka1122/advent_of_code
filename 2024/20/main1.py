from __future__ import annotations

FILENAME, TIME = "demo.txt", 64  # expected 1
FILENAME, TIME = "demo.txt", 65  # expected 0
FILENAME, TIME = "demo.txt", 20  # expected 5
FILENAME, TIME = "input.txt", 100
START = "S"
END = "E"
EMPTY = "."
WALL = "#"
INF = 100500


def f(
    the_map: list[list[bool]],
    start: tuple[int, int],
    end: tuple[int, int],
    target: int = INF,
) -> int:
    Q = [start]
    dist: dict[tuple[int, int], int] = dict()
    dist[start] = 0
    while len(Q) > 0:
        y0, x0 = Q.pop(0)
        if dist[(y0, x0)] >= target:
            continue
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]) and the_map[y][x]:
                if (y, x) not in dist or dist[(y0, x0)] + 1 < dist[(y, x)]:
                    dist[(y, x)] = dist[(y0, x0)] + 1
                    if (y0, x0) == end:
                        break
                    Q.append((y, x))
    # print(dist)
    # for y in range(len(the_map)):
    #     for x in range(len(the_map[0])):
    #         if (y, x) in dist:
    #             print(dist[(y, x)] % 10, end="")
    #         elif the_map[y][x]:
    #             print(EMPTY, end="")
    #         else:
    #             print(WALL, end="")
    #     print()
    if end in dist:
        return dist[end]
    return INF


def main() -> None:
    the_map: list[list[bool]] = []
    start = None
    end = None
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append([])
            for x in line.strip():
                if x == WALL:
                    the_map[-1].append(False)
                else:
                    if x == START:
                        if start is not None:
                            raise NotImplementedError
                        start = (len(the_map) - 1, len(the_map[-1]))
                    elif x == END:
                        if end is not None:
                            raise NotImplementedError
                        end = (len(the_map) - 1, len(the_map[-1]))
                    elif x != EMPTY:
                        raise NotImplementedError
                    the_map[-1].append(True)
    if start is None or end is None:
        raise NotImplementedError
    base_value = f(the_map, start, end)
    result = 0
    for y in range(1, len(the_map) - 1):
        print(f"y = {y}")
        for x in range(1, len(the_map[0]) - 1):
            if not the_map[y][x]:
                the_map[y][x] = True
                current = f(the_map, start, end, target=base_value - TIME + 1)
                if current + TIME <= base_value:
                    result += 1
                the_map[y][x] = False
    print(result)


if __name__ == "__main__":
    main()
