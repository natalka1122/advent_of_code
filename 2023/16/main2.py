from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def f(the_map: list[list[str]], start: tuple[int, int, int, int]) -> int:
    visited = set()
    energized = set()
    Q = [start]
    while len(Q) > 0:
        y0, x0, dy0, dx0 = Q.pop()
        if y0 < 0 or y0 >= len(the_map) or x0 < 0 or x0 >= len(the_map[0]):
            continue
        if (y0, x0, dy0, dx0) in visited:
            continue
        energized.add((y0, x0))
        visited.add((y0, x0, dy0, dx0))
        if the_map[y0][x0] == ".":
            Q.append((y0 + dy0, x0 + dx0, dy0, dx0))
        elif the_map[y0][x0] == "/":
            if (dy0, dx0) == (1, 0):
                Q.append((y0, x0 - 1, 0, -1))
            elif (dy0, dx0) == (-1, 0):
                Q.append((y0, x0 + 1, 0, 1))
            elif (dy0, dx0) == (0, 1):
                Q.append((y0 - 1, x0, -1, 0))
            elif (dy0, dx0) == (0, -1):
                Q.append((y0 + 1, x0, 1, 0))
            else:
                raise NotImplementedError
        elif the_map[y0][x0] == "\\":
            if (dy0, dx0) == (1, 0):
                Q.append((y0, x0 + 1, 0, 1))
            elif (dy0, dx0) == (-1, 0):
                Q.append((y0, x0 - 1, 0, -1))
            elif (dy0, dx0) == (0, 1):
                Q.append((y0 + 1, x0, 1, 0))
            elif (dy0, dx0) == (0, -1):
                Q.append((y0 - 1, x0, -1, 0))
            else:
                raise NotImplementedError
        elif the_map[y0][x0] == "-":
            if (dy0, dx0) == (1, 0):
                Q.append((y0, x0 + 1, 0, 1))
                Q.append((y0, x0 - 1, 0, -1))
            elif (dy0, dx0) == (-1, 0):
                Q.append((y0, x0 + 1, 0, 1))
                Q.append((y0, x0 - 1, 0, -1))
            elif (dy0, dx0) == (0, 1):
                Q.append((y0 + dy0, x0 + dx0, dy0, dx0))
            elif (dy0, dx0) == (0, -1):
                Q.append((y0 + dy0, x0 + dx0, dy0, dx0))
            else:
                raise NotImplementedError
        elif the_map[y0][x0] == "|":
            if (dy0, dx0) == (1, 0):
                Q.append((y0 + dy0, x0 + dx0, dy0, dx0))
            elif (dy0, dx0) == (-1, 0):
                Q.append((y0 + dy0, x0 + dx0, dy0, dx0))
            elif (dy0, dx0) == (0, 1):
                Q.append((y0 - 1, x0, -1, 0))
                Q.append((y0 + 1, x0, 1, 0))
            elif (dy0, dx0) == (0, -1):
                Q.append((y0 - 1, x0, -1, 0))
                Q.append((y0 + 1, x0, 1, 0))
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError
        # for y in range(len(the_map)):
        #     for x in range(len(the_map[0])):
        #         if (y, x) in energized:
        #             print("#", end="")
        #         else:
        #             print(the_map[y][x], end="")
        #     print()
    return len(energized)


def main() -> None:
    the_map = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(line.strip()))
    result = -1
    for i in range(len(the_map)):
        result = max(result, f(the_map, (i, 0, 0, 1)))
        result = max(result, f(the_map, (i, len(the_map[0]) - 1, 0, -1)))
    for i in range(len(the_map[0])):
        result = max(result, f(the_map, (0, i, 1, 0)))
        result = max(result, f(the_map, (len(the_map) - 1, i, -1, 0)))
    print(result)


if __name__ == "__main__":
    main()
