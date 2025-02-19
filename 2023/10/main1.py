from __future__ import annotations

# FILENAME = "demo1_1.txt"
# FILENAME = "demo1_2.txt"
FILENAME = "input.txt"
S = "S"


class Cell:
    def __init__(self, symbol: str) -> None:
        self.dist = 100500
        self.is_start = False
        self.symbol = symbol
        self.valid = True
        if symbol == "|":
            self.nei = {(-1, 0), (1, 0)}
        elif symbol == "-":
            self.nei = {(0, -1), (0, 1)}
        elif symbol == "L":
            self.nei = {(-1, 0), (0, 1)}
        elif symbol == "J":
            self.nei = {(-1, 0), (0, -1)}
        elif symbol == "7":
            self.nei = {(1, 0), (0, -1)}
        elif symbol == "F":
            self.nei = {(1, 0), (0, 1)}
        elif symbol == S:
            self.nei = {(-1, 0), (1, 0), (0, 1), (0, -1)}
            self.dist = 0
            self.is_start = True
        else:
            self.nei = set()
            self.valid = False

    def __repr__(self) -> str:
        return self.symbol


def main() -> None:
    result = 0
    maze: list[list[Cell]] = []
    start = None
    with open(FILENAME, "r") as file:
        y = 0
        for line in file:
            if S in line:
                if start is not None:
                    raise NotImplementedError
                start = (y, line.index(S))
            maze.append(list(map(Cell, line.strip())))
            y += 1
    print(maze)
    if not start:
        raise NotImplementedError
    print(f"start = {start}")
    q = [start]
    step = 0
    while len(q) > 0:
        step += 1
        y0, x0 = q.pop(0)
        if not maze[y0][x0].valid:
            raise NotImplementedError
        if len(q) != 0 and len(q) != 1:
            print(
                f"step = {step} len(q) = {len(q)} q = {q} current = {(y0,x0, maze[y0][x0], maze[y0][x0].dist)}"
            )
            raise NotImplementedError
        # print(
        #     f"step = {step} len(q) = {len(q)} q = {q} current = {(y0,x0, maze[y0][x0], maze[y0][x0].dist)}"
        # )
        for dy, dx in maze[y0][x0].nei:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < len(maze) and 0 <= x < len(maze[y]) and maze[y][x].valid:
                if maze[y][x].dist > maze[y0][x0].dist + 1:
                    if (y0 - y, x0 - x) not in maze[y][x].nei:
                        continue
                    maze[y][x].dist = maze[y0][x0].dist + 1
                    q.append((y, x))

    print(maze[y0][x0].dist)


if __name__ == "__main__":
    main()
