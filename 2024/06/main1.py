from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
START = "^"
ROCK = "#"
TURN = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


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
            the_map.append(line.strip())
            y += 1
    visited = set()
    y0, x0 = start
    dy, dx = (-1, 0)
    while 0 <= y0 < len(the_map) and 0 <= x0 < len(the_map[0]):
        # print(f"y0 = {y0} x0 = {x0} dy = {dy} dx = {dx}")
        visited.add((y0, x0))
        if not 0 <= y0 + dy < len(the_map) or not 0 <= x0+dx < len(the_map[0]):
            break
        if the_map[y0 + dy][x0 + dx] == ROCK:
            dy, dx = TURN[(dy, dx)]
        y0, x0 = y0 + dy, x0 + dx
        # for y in range(len(the_map)):
        #     for x in range(len(the_map[y])):
        #         if (y,x) in visited:
        #             print("X",end="")
        #         else:
        #             print(the_map[y][x],end="")
        #     print()
        # print("*"*20)
    # for y in range(len(the_map)):
    #     for x in range(len(the_map[y])):
    #         if (y,x) in visited:
    #             print("X",end="")
    #         else:
    #             print(the_map[y][x],end="")
    #     print()
    print(len(visited))


if __name__ == "__main__":
    main()
