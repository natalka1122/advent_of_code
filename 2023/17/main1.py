from __future__ import annotations
from typing import Optional


# FILENAME = "demo.txt"
# FILENAME = "demo1.txt"  # expected 25
FILENAME = "input.txt"
INFINITY = 100500
THREE = 3


class Distance:
    def __init__(self, value: int) -> None:
        self._data = {
            (0, 1): {1: INFINITY, 2: INFINITY, 3: INFINITY},
            (0, -1): {1: INFINITY, 2: INFINITY, 3: INFINITY},
            (1, 0): {1: INFINITY, 2: INFINITY, 3: INFINITY},
            (-1, 0): {1: INFINITY, 2: INFINITY, 3: INFINITY},
        }
        self._min = INFINITY
        self._value = value

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
        for count in range(key[2] + 1, THREE + 1):
            if self._data[(key[0], key[1])][count] <= newvalue:
                break
            self._data[(key[0], key[1])][count] = INFINITY
        if newvalue < self._min:
            self._min = newvalue
        return True

    @property
    def min(self) -> int:
        return self._min

    def set_zero(self) -> None:
        if not self.set((0, -1, 1), 0):
            raise NotImplementedError
        if not self.set((-1, 0, 1), 0):
            raise NotImplementedError

    def go_here(self, dy0: int, dx0: int, source: Distance) -> bool:
        result = False
        # print(f"self = {self}")
        for dy, dx in source._data:
            if (dy, dx) == (dy0, dx0):
                for count in range(1, THREE):
                    if self.set(
                        (dy0, dx0, count + 1),
                        source._data[(dy, dx)][count] + self._value,
                    ):
                        result = True
            elif (dy, dx) == (-dy0, -dx0):  # Cannot go back
                continue
            else:
                for count in range(1, THREE + 1):
                    if self.set(
                        (dy0, dx0, 1), source._data[(dy, dx)][count] + self._value
                    ):
                        result = True
                    pass
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
            dist[-1].append(Distance(the_map[y][x]))

    dist[start[0]][start[1]].set_zero()
    print(f"dist = {dist}")
    # processed: set[tuple[int, int]] = set()
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
        # if (y0, x0) == end:
        #     break
        # processed.add((y0, x0))
        print(f"y0 = {y0} x0 = {x0} closest_dist = {closest_dist}")
        for dy0, dx0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y = y0 + dy0
            x = x0 + dx0
            if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
                # if (y, x) in processed:
                #     continue
                # print(f"Got good nei dy0 = {dy0} dx0 = {dx0} y = {y} x = {x}")
                if dist[y][x].go_here(dy0, dx0, dist[y0][x0]):
                    # print(f"OKAY")
                    # print(dist)
                    if (y, x) not in Q:
                        Q.append((y, x))
                    # if (y, x) in processed:
                    #     raise NotImplementedError
    print(dist[end[0]][end[1]])
    # print("0,1", dist[end[0]][end[1] - 1])
    # print("1,0", dist[end[0] - 1][end[1]])
    for y in range(len(dist)):
        print(dist[y])
    print(dist[end[0]][end[1]].min)


if __name__ == "__main__":
    main()
