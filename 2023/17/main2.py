from __future__ import annotations
from typing import Optional


# FILENAME = "demo.txt"  # expected 94
# FILENAME = "demo2.txt"  # expected 71
FILENAME = "input.txt"
INFINITY = 100500
FOUR = 4
TEN = 10


class Distance:
    def __init__(self, y, x, the_map) -> None:
        self._data = {
            (0, 1): dict(),
            (0, -1): dict(),
            (1, 0): dict(),
            (-1, 0): dict(),
        }
        for key in self._data.keys():
            for count in range(FOUR, TEN + 1):
                self._data[key][count] = INFINITY
        self._min = INFINITY
        self._value = the_map[y][x]
        self._y = y
        self._x = x
        self._the_map = the_map

    def __repr__(self) -> str:
        result: dict[tuple[int, int], dict[int, int]] = dict()
        for key in self._data:
            result[key] = dict()
            for num in self._data[key]:
                if self._data[key][num] < INFINITY:
                    result[key][num] = self._data[key][num]
            if not result[key]:
                del result[key]
        return f"{self._value} {result}"

    def set(self, key: tuple[int, int, int], newvalue: int) -> bool:
        if (key[0], key[1]) not in self._data:
            print(f"key = {key}")
            raise NotImplementedError
        if INFINITY <= newvalue:
            return False
        if self._data[(key[0], key[1])][key[2]] <= newvalue:
            return False
        self._data[(key[0], key[1])][key[2]] = newvalue
        if newvalue < self._min:
            self._min = newvalue
        return True

    @property
    def min(self) -> int:
        return self._min

    def set_zero(self) -> None:
        self._is_start = True
        if not self.set((0, 1, FOUR), 0):
            raise NotImplementedError
        if not self.set((1, 0, FOUR), 0):
            raise NotImplementedError

    def go_here(self, dy0: int, dx0: int, count: int, source: Distance) -> bool:
        result = False
        # print(f"self = {self}")
        for dy, dx in source._data:
            if (dy, dx) == (dy0, dx0) or (dy, dx) == (-dy0, -dx0):
                continue
            else:
                # print(f"count = {count}")
                len_path = 0
                for c in range(1, count + 1):
                    len_path += source._the_map[source._y + c * dy0][
                        source._x + c * dx0
                    ]
                if self.set(
                    (dy0, dx0, count), min(source._data[(dy, dx)].values()) + len_path
                ):
                    result = True
        # print(f"self = {self} result = {result}")
        return result


def main() -> None:
    the_map: list[list[int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(map(int, line.strip())))
    # print(f"the_map = {the_map}")
    start = 0, 0
    end = len(the_map) - 1, len(the_map[0]) - 1
    dist: list[list[Distance]] = []
    for y in range(len(the_map)):
        dist.append([])
        for x in range(len(the_map[0])):
            dist[-1].append(Distance(y, x, the_map))

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
        # print(f"closest_index = {closest_index} closest_dist = {closest_dist}")
        if INFINITY <= closest_dist:
            raise NotImplementedError
        y0, x0 = Q.pop(closest_index)
        # print(f"y0 = {y0} x0 = {x0} closest_dist = {closest_dist}")
        for dy0, dx0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for count in range(FOUR, TEN + 1):
                y = y0 + dy0 * count
                x = x0 + dx0 * count
                if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
                    # print(f"Got good nei dy0 = {dy0} dx0 = {dx0} y = {y} x = {x}")
                    if dist[y][x].go_here(dy0, dx0, count, dist[y0][x0]):
                        # print(dist)
                        if (y, x) not in Q:
                            Q.append((y, x))
                            # print(f"found ({y}, {x}) dist[y][x] = {dist[y][x]}")
                else:
                    break
    print(dist[end[0]][end[1]])
    print(dist[end[0]][end[1]].min)


if __name__ == "__main__":
    main()
