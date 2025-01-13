from __future__ import annotations

FILENAME, TIME = "demo.txt", 76  # expected 3
# FILENAME, TIME = "demo.txt", 7  # expected ?
# FILENAME, TIME = "demo.txt", 77  # expected 0
# FILENAME, TIME = "demo.txt", 74  # expected 4
# FILENAME, TIME = "input.txt", 100
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
    cheat_start: int = INF,
    target: int = INF,
) -> int:
    result = 0
    Q = {start}
    dist: dict[tuple[int, int], int] = dict()
    dist[start] = 0
    Q_before_cheat = set()
    while len(Q) > 0:
        y0, x0 = Q.pop()
        if (y0, x0) == end:
            if dist[(y0, x0)] <= target:
                result += 1
        if dist[(y0, x0)] == cheat_start:
            Q_before_cheat.add((y0, x0))
            continue
        if dist[(y0, x0)] > cheat_start:
            raise NotImplementedError
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
    if cheat_start == INF:
        return dist[end]
    # print(dist)
    # print(f"result = {result} Q_before_cheat = {Q_before_cheat}")
    # print_the_map(the_map, dist)
    # Q = set()
    # for y0, x0 in Q_before_cheat:
    #     for dy in range(-TIME, TIME + 1):
    #         y = y0 + dy
    #         if 0 <= y < len(the_map):
    #             # print(f"dy = {dy}")
    #             for dx in range(-TIME + abs(dy), TIME - abs(dy) + 1):
    #                 x = x0 + dx
    #                 if 0 <= x < len(the_map[0]):
    #                     # print(f"dy = {dy} dx = {dx}")
    #                     p = abs(dy) + abs(dx)
    #                     if the_map[y][x] and dist[(y0, x0)] + p <= target:
    #                         if (y, x) not in dist or dist[(y0, x0)] + p < dist[(y, x)]:
    #                             Q.add((y, x))
    #                             dist[(y, x)] = dist[(y0, x0)] + p
    #                             # if (y, x) == end:
    #                             #     if dist[(y, x)] <= target:
    #                             #         result += 1
    # print(f"result = {result} Q = {Q}")
    # print_the_map(the_map, dist)
    # while len(Q) > 0:
    #     y0, x0 = Q.pop()
    #     if (y0, x0) == end:
    #         if dist[(y0, x0)] <= target:
    #             result += 1
    #     if dist[(y0,x0)] > target:
    #         raise NotImplementedError
    #     if dist[(y0,x0)] == target:
    #         continue
    #     # if dist[(y0, x0)] == cheat_start:
    #     #     Q_before_cheat.add((y0, x0))
    #     #     continue
    #     # if dist[(y0, x0)] > cheat_start:
    #     #     raise NotImplementedError
    #     for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #         y = y0 + dy
    #         x = x0 + dx
    #         if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]) and the_map[y][x]:
    #             if (y, x) not in dist or dist[(y0, x0)] + 1 < dist[(y, x)]:
    #                 dist[(y, x)] = dist[(y0, x0)] + 1
    #                 Q.add((y, x))
    # print(f"result = {result} dist[end] = {dist[end]}")
    # return result


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
    dist = f(the_map, start, end)
    result = 0
    for t in range(base_value - TIME):
        current = f(the_map, start, end, cheat_start=t, target=base_value - TIME)
        print(f"t = {t} current = {current}")
        result += current
        raise NotImplementedError
    print(result)


if __name__ == "__main__":
    main()
