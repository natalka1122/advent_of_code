from __future__ import annotations
from typing import Optional

# FILENAME = "demo1.txt"  # expected 45
# FILENAME = "demo2.txt"  # expected 64
FILENAME = "input.txt"
START = "S"
END = "E"
EMPTY = "."
WALL = "#"
INFINITY = 100500
FORWARD = 1
ROTATE = 1000 + 1
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Cell:
    def __init__(self, value: str, y: int, x: int, cell_map: list[list[Cell]]) -> None:
        self._data: dict[tuple[int, int], tuple[int, set[Cell]]] = {
            (0, 1): (INFINITY, set()),
            (0, -1): (INFINITY, set()),
            (1, 0): (INFINITY, set()),
            (-1, 0): (INFINITY, set()),
        }
        self._min = INFINITY
        self.x = x
        self.y = y
        self._value = value
        self._cell_map = cell_map

    def __repr__(self) -> str:
        result: dict[tuple[int, int], str] = dict()
        for key in self._data:
            if self._data[key][0] < INFINITY:
                result[key] = f"{self._data[key][0]} {len(self._data[key][1])}"
        return f"{self._value} ({self.y},{self.x}) {result}"

    def set(self, key: tuple[int, int], newvalue: int, newpath: set[Cell]) -> bool:
        if key not in self._data:
            print(f"key = {key}")
            raise NotImplementedError
        source = self._cell_map[self.y - key[0]][self.x - key[1]]
        if self.y != source.y + key[0] or self.x != source.x + key[1]:
            raise NotImplementedError
        if newvalue >= INFINITY:
            return False
        if self._data[key][0] > newvalue:
            self._data[key] = (newvalue, newpath)
            if newvalue < self._min:
                self._min = newvalue
        elif self._data[key][0] == newvalue:
            joined_path = self._data[key][1].union(newpath)
            if len(self._data[key][1]) == len(joined_path):
                return False
            elif len(self._data[key][1]) < len(joined_path):
                self._data[key] = (self._data[key][0], joined_path)
            else:
                raise NotImplementedError
        elif self._data[key][0] < newvalue:
            return False
        else:
            raise NotImplementedError
        return True

    @property
    def min(self) -> int:
        return self._min

    def set_zero(self) -> None:
        if not self.set((0, 1), 0, {self}):
            raise NotImplementedError

    def go_here(self, dy0: int, dx0: int) -> bool:
        source = self._cell_map[self.y - dy0][self.x - dx0]
        if self.y != source.y + dy0 or self.x != source.x + dx0:
            raise NotImplementedError
        result = False
        for dy, dx in source._data:
            if (dy, dx) == (-dy0, -dx0):  # Cannot go back
                continue
            if self in source._data[(dy, dx)][1]:
                continue
            newpath = source._data[(dy, dx)][1].union({self})
            if (dy, dx) == (dy0, dx0):
                if self.set((dy0, dx0), source._data[(dy, dx)][0] + FORWARD, newpath):
                    result = True
            elif self.set((dy0, dx0), source._data[(dy, dx)][0] + ROTATE, newpath):
                result = True
        return result


def main() -> None:
    char_map = []
    start = None
    end = None
    with open(FILENAME, "r") as file:
        y = 0
        for line_ in file:
            line = line_.strip()
            if START in line:
                if start is not None:
                    raise NotImplementedError
                start = y, line.index(START)
            if END in line:
                if end is not None:
                    raise NotImplementedError
                end = y, line.index(END)
            y += 1
            char_map.append(line)
    if start is None or end is None:
        print(f"start = {start} end = {end}")
        raise NotImplementedError
    height = len(char_map)
    width = len(char_map[0])
    # print(f"start = {start} end = {end}")
    # print("\n".join(char_map))
    cell_map: list[list[Cell]] = []
    for y in range(height):
        cell_map.append([])
        for x in range(width):
            cell_map[-1].append(Cell(value=char_map[y][x], y=y, x=x, cell_map=cell_map))
    cell_map[start[0]][start[1]].set_zero()
    # for y in range(height):
    #     print(f"{y}: {cell_map[y]}")
    Q: list[Cell] = [cell_map[start[0]][start[1]]]
    while len(Q) > 0:
        closest_index: Optional[int] = None
        closest_dist: int = INFINITY
        for key, value in enumerate(Q):
            if closest_index is None or closest_dist > value.min:
                closest_dist = value.min
                closest_index = key
        if closest_index is None:
            raise NotImplementedError
        if INFINITY <= closest_dist:
            raise NotImplementedError
        cell: Cell = Q.pop(closest_index)
        # print(f"y0 = {cell.y} x0 = {cell.x} cell = {cell}")
        for dy0, dx0 in DIRECTIONS:
            y = cell.y + dy0
            x = cell.x + dx0
            if 0 <= y < height and 0 <= x < width and char_map[y][x] in [EMPTY, END]:
                if cell_map[y][x].go_here(dy0, dx0):
                    if cell_map[y][x] not in Q:
                        Q.append(cell_map[y][x])
    # for y in range(height):
    #     print(f"{y}: {cell_map[y]}")
    print(cell_map[end[0]][end[1]])


if __name__ == "__main__":
    main()
