from __future__ import annotations
from typing import Optional

# FILENAME = "demo1.txt"  # expected 7036
# FILENAME = "demo2.txt"  # expected 11048
FILENAME = "input.txt"
START = "S"
END = "E"
EMPTY = "."
WALL = "#"
INFINITY = 100500
FORWARD = 1
ROTATE = 1000 + 1


class Distance:
    def __init__(self, value: str) -> None:
        self._data = {
            (0, 1): INFINITY,
            (0, -1): INFINITY,
            (1, 0): INFINITY,
            (-1, 0): INFINITY,
        }
        self._min = INFINITY
        self._value = value

    def __repr__(self) -> str:
        result: dict[tuple[int, int], int] = dict()
        for key in self._data:
            if self._data[key] < INFINITY:
                result[key] = self._data[key]
        return f"{self._value} {result}"

    def set(self, key: tuple[int, int], newvalue: int) -> bool:
        if (key[0], key[1]) not in self._data:
            print(f"key = {key}")
            raise NotImplementedError
        if INFINITY <= newvalue:
            return False
        if self._data[key] <= newvalue:
            return False
        self._data[(key[0], key[1])] = newvalue
        if newvalue < self._min:
            self._min = newvalue
        return True

    @property
    def min(self) -> int:
        return self._min

    def set_zero(self) -> None:
        # if not self.set((0, -1), 0):
        #     raise NotImplementedError
        if not self.set((0, 1), 0):
            raise NotImplementedError
        # if not self.set((-1, 0), 0):
        #     raise NotImplementedError
        # if not self.set((1, 0), 0):
        #     raise NotImplementedError

    def go_here(self, dy0: int, dx0: int, source: Distance) -> bool:
        result = False
        # print(f"self = {self}")
        for dy, dx in source._data:
            if (dy, dx) == (dy0, dx0):
                if self.set(
                    (dy0, dx0),
                    source._data[(dy, dx)] + FORWARD,
                ):
                    result = True
            elif (dy, dx) == (-dy0, -dx0):  # Cannot go back
                continue
            else:
                if self.set((dy0, dx0), source._data[(dy, dx)] + ROTATE):
                    result = True
                pass
        return result


def main() -> None:
    the_map = []
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
            the_map.append(line)
    if start is None or end is None:
        print(f"start = {start} end = {end}")
        raise NotImplementedError
    print(f"start = {start} end = {end}")
    print("\n".join(the_map))
    dist: list[list[Distance]] = []
    for y in range(len(the_map)):
        dist.append([])
        for x in range(len(the_map[0])):
            dist[-1].append(Distance(the_map[y][x]))
    dist[start[0]][start[1]].set_zero()
    print(f"dist = {dist}")
    Q = [start]
    while len(Q) > 0:
        closest_index: Optional[int] = None
        closest_dist: int = INFINITY
        for key, value in enumerate(Q):
            if closest_index:
                current_dist = dist[value[0]][value[1]].min
                if current_dist < closest_dist:
                    closest_index = key
                    closest_dist = current_dist
            else:
                closest_index = key
                closest_dist = dist[value[0]][value[1]].min
        if closest_index is None:
            raise NotImplementedError
        if INFINITY <= closest_dist:
            raise NotImplementedError
        y0, x0 = Q.pop(closest_index)
        # print(f"y0 = {y0} x0 = {x0} closest_dist = {closest_dist}")
        for dy0, dx0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y = y0 + dy0
            x = x0 + dx0
            if (
                0 <= y < len(the_map)
                and 0 <= x < len(the_map[0])
                and the_map[y][x] in [EMPTY, END]
            ):
                # print(f"Got good nei dy0 = {dy0} dx0 = {dx0} y = {y} x = {x}")
                if dist[y][x].go_here(dy0, dx0, dist[y0][x0]):
                    # print(f"OKAY")
                    # print(dist)
                    if (y, x) not in Q:
                        Q.append((y, x))
                #     # if (y, x) in processed:
                #     #     raise NotImplementedError
    # print(f"y0 = {y0} x0 = {x0} closest_dist = {closest_dist}")
    for y in range(len(dist)):
        print(f"{y}: {dist[y]}")
    print(dist[end[0]][end[1]])


if __name__ == "__main__":
    main()
