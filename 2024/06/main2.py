from __future__ import annotations

# FILENAME = "demo.txt"
# FILENAME = "demo1.txt"
FILENAME = "input.txt"
START = "^"
ROCK = "#"
EMPTY = "."
TURN = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def find_a_cycle(the_map, y0, x0):
    visited = set()
    dy, dx = (-1, 0)
    while 0 <= y0 < len(the_map) and 0 <= x0 < len(the_map[0]):
        if (y0, x0, dy, dx) in visited:
            return True
        visited.add((y0, x0, dy, dx))
        while True:
            if not 0 <= y0 + dy < len(the_map) or not 0 <= x0 + dx < len(the_map[0]):
                return False
            if the_map[y0 + dy][x0 + dx] == ROCK:
                dy, dx = TURN[(dy, dx)]
            elif the_map[y0 + dy][x0 + dx] == EMPTY or the_map[y0 + dy][x0 + dx] == START:
                break
            else:
                raise NotImplementedError
        y0, x0 = y0 + dy, x0 + dx
    raise NotImplementedError


def main():
    the_map = []
    start = None
    with open(FILENAME, "r") as file:
        y = 0
        for line in file:
            if START in line:
                if start:
                    raise NotImplementedError
                start = (y, line.index(START))
            the_map.append(list(line.strip()))
            y += 1
    y0, x0 = start
    result = 0
    for y in range(len(the_map)):
        for x in range(len(the_map[y])):
            if the_map[y][x] == EMPTY:
                the_map[y][x] = ROCK
                if find_a_cycle(the_map, y0, x0):
                    print(f"y = {y} x = {x}")
                    result += 1
                the_map[y][x] = EMPTY
    print(result)


if __name__ == "__main__":
    main()
