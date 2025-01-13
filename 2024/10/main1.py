from __future__ import annotations
from typing import Optional

# FILENAME = "demo1_1.txt"  # expected 1
# FILENAME = "demo1_2.txt"  # expected 36
# FILENAME = "demo1_3.txt"  # expected 2
# FILENAME = "demo1_4.txt"  # expected 4
# FILENAME = "demo1_5.txt"  # expected 3
FILENAME = "input.txt"
START = 0
END = 9
EMPTY = "."


# def f(
#     y0: int, x0: int, path: list[tuple[int, int]], the_map: list[list[Optional[int]]]
# ) -> int:
#     if the_map[y0][x0] == END:
#         print(f"path = {path} + {(y0, x0)}")
#         return 1
#     result = 0
#     for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         y = y0 + dy
#         x = x0 + dx
#         if (
#             0 <= y < len(the_map)
#             and 0 <= x < len(the_map)
#             and isinstance(the_map[y][x], int)
#             and the_map[y][x] != EMPTY
#             and the_map[y][x] - the_map[y0][x0] == 1
#         ):
#             result += f(y, x, path + [(y0, x0)], the_map)
#     return result


def f(
    y0: int, x0: int, path: list[tuple[int, int]], the_map: list[list[Optional[int]]]
) -> set[tuple[int, int]]:
    if the_map[y0][x0] == END:
        print(f"path = {path} + {(y0, x0)}")
        return {(y0, x0)}
    result = set()
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        y = y0 + dy
        x = x0 + dx
        if (
            0 <= y < len(the_map)
            and 0 <= x < len(the_map)
            and isinstance(the_map[y][x], int)
            and the_map[y][x] != EMPTY
            and the_map[y][x] - the_map[y0][x0] == 1
        ):
            result.update(f(y, x, path + [(y0, x0)], the_map))
    return result


def main() -> None:
    the_map: list[list[Optional[int]]] = list()
    trailheads = set()
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append([])
            for index, symbol in enumerate(line.strip()):
                if symbol.isdigit():
                    the_map[-1].append(int(symbol))
                    if the_map[-1][index] == START:
                        trailheads.add((len(the_map) - 1, index))
                elif symbol == EMPTY:
                    the_map[-1].append(None)
    print(the_map)
    print(f"trailheads = {trailheads}")
    result = 0
    for y, x in trailheads:
        result += len(f(y, x, [], the_map))
    print(result)
    # print(len(result))


if __name__ == "__main__":
    main()
