from __future__ import annotations

# FILENAME = "demo1.txt"  # expected 9021
# FILENAME = "demo2.txt"  # expected ???
# FILENAME = "demo3.txt"  # expected ???
FILENAME = "input.txt"
ROBOT = "@"
EMPTY = "."
WALL = "#"
BOX = "O"
BOXL = "["
BOXR = "]"


def go_please(y0: int, x0: int, dy: int, dx: int, the_map: list[list[str]]) -> None:
    if the_map[y0][x0] == BOXR:
        x0 = x0 - 1
    if the_map[y0][x0] != BOXL:
        raise NotImplementedError
    if dx == 0:
        if the_map[y0 + dy][x0] == WALL or the_map[y0 + dy][x0 + 1] == WALL:
            raise NotImplementedError
        if the_map[y0 + dy][x0] == EMPTY and the_map[y0 + dy][x0 + 1] == EMPTY:
            the_map[y0 + dy][x0] = BOXL
            the_map[y0 + dy][x0 + 1] = BOXR
            the_map[y0][x0] = EMPTY
            the_map[y0][x0 + 1] = EMPTY
        elif the_map[y0 + dy][x0] == EMPTY:
            go_please(y0 + dy, x0 + 1, dy, dx, the_map)
            go_please(y0, x0, dy, dx, the_map)
        elif the_map[y0 + dy][x0 + 1] == EMPTY:
            go_please(y0 + dy, x0, dy, dx, the_map)
            go_please(y0, x0, dy, dx, the_map)
        elif the_map[y0 + dy][x0] == BOXL and the_map[y0 + dy][x0 + 1] == BOXR:
            go_please(y0 + dy, x0, dy, dx, the_map)
            go_please(y0, x0, dy, dx, the_map)
        elif the_map[y0 + dy][x0] == BOXR and the_map[y0 + dy][x0 + 1] == BOXL:
            go_please(y0 + dy, x0, dy, dx, the_map)
            go_please(y0 + dy, x0 + 1, dy, dx, the_map)
            go_please(y0, x0, dy, dx, the_map)
        else:
            raise NotImplementedError
    elif dx == 1:
        if the_map[y0][x0 + 2] != EMPTY:
            go_please(y0, x0 + 2, dy, dx, the_map)
        the_map[y0][x0 + 1] = BOXL
        the_map[y0][x0 + 2] = BOXR
        the_map[y0][x0] = EMPTY
    elif dx == -1:
        if the_map[y0][x0 - 1] != EMPTY:
            go_please(y0, x0 - 1, dy, dx, the_map)
        the_map[y0][x0 - 1] = BOXL
        the_map[y0][x0] = BOXR
        the_map[y0][x0 + 1] = EMPTY
    else:
        raise NotImplementedError


def can_go(y0: int, x0: int, dy: int, dx: int, the_map: list[list[str]]) -> bool:
    if the_map[y0][x0] == BOXR:
        x0 = x0 - 1
    if the_map[y0][x0] != BOXL:
        print(f"y0 = {y0} x0 = {x0} dy = {dy} dx = {dx} the_map[y0][x0] = {the_map[y0][x0]}")
        raise NotImplementedError
    if dx == 0:
        if the_map[y0 + dy][x0] == WALL or the_map[y0 + dy][x0 + 1] == WALL:
            return False
        if the_map[y0 + dy][x0] == EMPTY and the_map[y0 + dy][x0 + 1] == EMPTY:
            return True
        if the_map[y0 + dy][x0] == EMPTY:
            return can_go(y0 + dy, x0 + 1, dy, dx, the_map)
        if the_map[y0 + dy][x0 + 1] == EMPTY:
            return can_go(y0 + dy, x0, dy, dx, the_map)
        return can_go(y0 + dy, x0, dy, dx, the_map) and can_go(
            y0 + dy, x0 + 1, dy, dx, the_map
        )
    elif dx == 1:
        if the_map[y0][x0 + 2] == EMPTY:
            return True
        if the_map[y0][x0 + 2] == WALL:
            return False
        return can_go(y0, x0 + 2, dy, dx, the_map)
    elif dx == -1:
        if the_map[y0][x0 - 1] == EMPTY:
            return True
        if the_map[y0][x0 - 1] == WALL:
            return False
        return can_go(y0, x0 - 1, dy, dx, the_map)
    else:
        raise NotImplementedError


def main() -> None:
    the_map: list[list[str]] = []
    read_map = True
    instructions = ""
    start = None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            line = line.replace(WALL, WALL * 2)
            line = line.replace(BOX, BOXL + BOXR)
            line = line.replace(EMPTY, EMPTY * 2)
            line = line.replace(ROBOT, ROBOT + EMPTY)
            if not line:
                if not read_map:
                    raise NotImplementedError
                read_map = False
            if read_map:
                if ROBOT in line:
                    if start is not None:
                        raise NotImplementedError
                    start = len(the_map), line.index(ROBOT)
                the_map.append(list(line))
            else:
                instructions += line
    if start is None:
        raise NotImplementedError
    y0, x0 = start
    for symbol in instructions:
        if symbol == "<":
            dy, dx = 0, -1
        elif symbol == "^":
            dy, dx = -1, 0
        elif symbol == ">":
            dy, dx = 0, 1
        elif symbol == "v":
            dy, dx = 1, 0
        else:
            raise NotImplementedError
        if the_map[y0 + dy][x0 + dx] == EMPTY:
            the_map[y0][x0] = EMPTY
            y0, x0 = y0 + dy, x0 + dx
            the_map[y0][x0] = ROBOT
        elif the_map[y0 + dy][x0 + dx] == WALL:
            pass
        elif the_map[y0 + dy][x0 + dx] in [BOXL, BOXR]:
            if can_go(y0 + dy, x0 + dx, dy, dx, the_map):
                go_please(y0 + dy, x0 + dx, dy, dx, the_map)
                if the_map[y0+dy][x0+dx]!= EMPTY:
                    raise NotImplementedError
                the_map[y0][x0] = EMPTY
                y0, x0 = y0 + dy, x0 + dx
                the_map[y0][x0] = ROBOT
        else:
            print(f"the_map[y0 + dx][x0 + dx] = {the_map[y0 + dy][x0 + dx]}")
            raise NotImplementedError
    result = 0
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            if the_map[y][x] == BOXL:
                result += 100 * y + x
    print(result)


if __name__ == "__main__":
    main()
