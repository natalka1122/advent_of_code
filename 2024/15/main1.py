from __future__ import annotations

# FILENAME = "demo1.txt"  # expected 10092
# FILENAME = "demo2.txt"  # expected 2028
FILENAME = "input.txt"
ROBOT = "@"
EMPTY = "."
WALL = "#"
BOX = "O"


def main():
    the_map = []
    read_map = True
    instructions = ""
    start = None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
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
    print(the_map)
    print(instructions)
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
        elif the_map[y0 + dy][x0 + dx] == BOX:
            step = 2
            while the_map[y0 + step * dy][x0 + step * dx] == BOX:
                step += 1
            if the_map[y0 + step * dy][x0 + step * dx] == EMPTY:
                the_map[y0 + step * dy][x0 + step * dx] = BOX
                the_map[y0][x0] = EMPTY
                y0, x0 = y0 + dy, x0 + dx
                the_map[y0][x0] = ROBOT
        else:
            print(f"the_map[y0 + dx][x0 + dx] = {the_map[y0 + dy][x0 + dx]}")
            raise NotImplementedError
    for l in the_map:
        print("".join(l))
    result = 0
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            if the_map[y][x] == BOX:
                result += 100 * y + x
    print(result)


if __name__ == "__main__":
    main()
