from __future__ import annotations
from typing import Optional

# FILENAME = "demo1_2.txt"
# FILENAME = "demo2_1.txt"
# FILENAME = "demo2_2.txt"
# FILENAME = "demo2_3.txt"
# FILENAME = "demo2_4.txt"
FILENAME = "input.txt"
S = "S"
OUTSIDE = -1
INSIDE = 1
BORDER = 0
UNKNOWN = None


def state_to_line(state: int) -> str:
    if state == INSIDE:
        return "INSIDE"
    if state == OUTSIDE:
        return "OUTSIDE"
    if state == BORDER:
        return "BORDER"
    if state == UNKNOWN:
        return "UNKNOWN"
    raise NotImplementedError


class ConstDict:
    def __init__(
        self, nei: list[tuple[int, int]], is_regular: Optional[bool], is_start: bool
    ) -> None:
        self.nei = nei
        self.is_regular = is_regular
        self.is_start = is_start


LETTERS: dict[str, ConstDict] = {
    "|": ConstDict(nei=sorted({(-1, 0), (1, 0)}), is_regular=True, is_start=False),
    "-": ConstDict(nei=sorted({(0, -1), (0, 1)}), is_regular=True, is_start=False),
    "J": ConstDict(nei=sorted({(-1, 0), (0, -1)}), is_regular=True, is_start=False),
    "F": ConstDict(nei=sorted({(1, 0), (0, 1)}), is_regular=True, is_start=False),
    "L": ConstDict(nei=sorted({(-1, 0), (0, 1)}), is_regular=False, is_start=False),
    "7": ConstDict(nei=sorted({(1, 0), (0, -1)}), is_regular=False, is_start=False),
    "S": ConstDict(
        nei=sorted({(-1, 0), (1, 0), (0, 1), (0, -1)}),
        is_regular=None,
        is_start=True,
    ),
}


class Cell:
    def __init__(self, symbol: str) -> None:
        self.state: Optional[int] = UNKNOWN
        self._direction: Optional[int] = UNKNOWN
        self.dist: int = 100500
        self._symbol: str = symbol
        if self._symbol in LETTERS:
            self.nei: list[tuple[int, int]] = LETTERS[self._symbol].nei
            self.is_regular: Optional[bool] = LETTERS[self._symbol].is_regular
            self.is_start: bool = LETTERS[self._symbol].is_start
            self.is_valid: bool = True
            if self.is_start:
                self.dist = 0
                self.state = BORDER
        else:
            self.nei = []
            self.is_regular = True
            self.is_start = False
            self.is_valid = False

    def __repr__(self) -> str:
        result = {
            "state": state_to_line(self.state),
            "direction": state_to_line(self.direction),
            "dist": self.dist,
            "symbol": f"{self}({self._symbol})",
            "is_valid": self.is_valid,
            "is_regular": self.is_regular,
        }
        return str(result)

    def __str__(self) -> str:
        return self.letter

    @property
    def letter(self) -> str:
        if self.state == UNKNOWN:
            return "?"
        if self.state == BORDER:
            if self._direction == INSIDE:
                return "B"
            elif self._direction == OUTSIDE:
                return "b"
            elif self._direction is None:
                return "?"
            else:
                raise NotImplementedError
        if self.state == INSIDE:
            return "."
        if self.state == OUTSIDE:
            return "_"
        print(f"self.state = {self.state}")
        raise NotImplementedError

    def define_start(self, remove_from_nei: set[tuple[int, int]]) -> None:
        new_nei = sorted(set(self.nei) - remove_from_nei)
        if len(new_nei) != 2:
            raise NotImplementedError
        for symbol in LETTERS:
            if LETTERS[symbol].nei == new_nei:
                self.is_regular = LETTERS[symbol].is_regular
                self.nei = LETTERS[symbol].nei
                return
        print(f"new_nei = {new_nei}")
        raise NotImplementedError

    @property
    def direction(self) -> Optional[int]:
        if self._direction:
            return self._direction
        if self.state == OUTSIDE:
            self._direction = OUTSIDE
            return OUTSIDE
        if self.state == INSIDE:
            self._direction = INSIDE
            return INSIDE
        if self.state == BORDER:
            return UNKNOWN
        if self.state == UNKNOWN:
            return UNKNOWN
        print(self.__dict__)
        raise NotImplementedError

    @direction.setter
    def direction(self, value: int) -> None:
        if self._direction:
            raise NotImplementedError
        self._direction = value


def main() -> None:
    maze: list[list[Cell]] = []
    start = None
    with open(FILENAME, "r") as file:
        y = 0
        for line_ in file:
            line = line_.strip()
            maze.append([])
            for x in range(len(line)):
                maze[y].append(Cell(line[x]))
                if maze[y][x].is_start:
                    if start is not None:
                        raise NotImplementedError
                    start = (y, x)
            y += 1
    if not start:
        raise NotImplementedError
    print(f"start = {start}")
    q = [start]
    step = 0
    while len(q) > 0:
        step += 1
        y0, x0 = q.pop(0)
        if not maze[y0][x0].is_valid:
            raise NotImplementedError
        if len(q) != 0 and len(q) != 1:
            print(
                f"step = {step} len(q) = {len(q)} q = {q} x0 = {x0} y = {y0} maze[{y0}][{x0}] = {repr(maze[y0][x0])}"
            )
            raise NotImplementedError
        remove_from_nei = set()
        for dy, dx in maze[y0][x0].nei:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < len(maze) and 0 <= x < len(maze[y]) and maze[y][x].is_valid:
                if maze[y][x].dist > maze[y0][x0].dist + 1:
                    if (y0 - y, x0 - x) not in maze[y][x].nei:
                        remove_from_nei.add((dy, dx))
                        continue
                    maze[y][x].dist = maze[y0][x0].dist + 1
                    maze[y][x].state = BORDER
                    q.append((y, x))
            elif (y0, x0) == start:
                remove_from_nei.add((dy, dx))
            else:
                print(f"y0 = {y0} x0 = {x0} maze[y0][x0]={maze[y0][x0].__dict__}")
                raise NotImplementedError
        if remove_from_nei:
            if len(remove_from_nei) != 2:
                raise NotImplementedError
            maze[y0][x0].define_start(remove_from_nei)

    print("\n".join(map(lambda x: "".join(map(str, x)), maze)))

    result: int = 0
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            # print(f"y = {y} x = {x} maze[{y}][{x}] = {maze[y][x]}", repr(maze[y][x]))
            if maze[y][x].state == BORDER:
                if y == 0 or x == 0:
                    if maze[y][x].is_regular:
                        maze[y][x].direction = INSIDE
                    else:
                        maze[y][x].direction = OUTSIDE
                elif maze[y - 1][x - 1].state == BORDER:
                    if maze[y][x].is_regular:
                        maze[y][x].direction = -maze[y - 1][x - 1].direction
                    else:
                        maze[y][x].direction = maze[y - 1][x - 1].direction
                elif maze[y - 1][x - 1].state == OUTSIDE:
                    if maze[y][x].is_regular:
                        maze[y][x].direction = INSIDE
                    else:
                        maze[y][x].direction = OUTSIDE
                elif maze[y - 1][x - 1].state == INSIDE:
                    if maze[y][x].is_regular:
                        maze[y][x].direction = OUTSIDE
                    else:
                        maze[y][x].direction = INSIDE
                else:
                    raise NotImplementedError
            elif maze[y][x].state == UNKNOWN:
                if y == 0 or x == 0:
                    maze[y][x].state = OUTSIDE
                elif maze[y - 1][x - 1].state == BORDER:
                    maze[y][x].state = maze[y - 1][x - 1].direction
                elif maze[y - 1][x - 1].state in [INSIDE, OUTSIDE]:
                    maze[y][x].state = maze[y - 1][x - 1].state
                else:
                    raise NotImplementedError
            else:
                raise NotImplementedError
            if maze[y][x].state == INSIDE:
                result += 1

    print("\n".join(map(lambda x: "".join(map(str, x)), maze)))
    print(result)


if __name__ == "__main__":

    main()
