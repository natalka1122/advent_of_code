from __future__ import annotations
import re

# FILENAME = "demo.txt"  # expected 5031
FILENAME = "input.txt"


F = "F"
L = "L"
R = "R"
EMPTY = "."
WALL = "#"
NIL = " "
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Side(tuple[str, int]):
    def __init__(self, *_: object):
        self.is_defined = len(self) == 2

    def go_down(self) -> Side:
        if self == ("F", 1):
            return Side(("D", 1))
        if self == ("D", 1):
            return Side(("B", 1))
        if self == ("R", 3):
            return Side(("D", 2))
        print(f"self = {self}")
        raise NotImplementedError

    def go_up(self) -> Side:
        print(f"self = {self}")
        raise NotImplementedError

    def go_left(self) -> Side:
        if self == ("F", 1):
            return Side(("L", 1))
        if self == ("B", 1):
            return Side(("L", 4))
        print(f"self = {self}")
        raise NotImplementedError

    def go_right(self) -> Side:
        if self == ("D", 1):
            return Side(("R", 3))
        if self == ("R", 3):
            return Side(("U", 4))
        if self == ("B", 1):
            return Side(("R", 3))
        print(f"self = {self}")
        raise NotImplementedError


def gen_transform(
    map_str: list[str],
) -> dict[tuple[tuple[int, int], tuple[int, int]], tuple[tuple[int, int], tuple[int, int]]]:
    side = 50
    transform: dict[
        tuple[tuple[int, int], tuple[int, int]], tuple[tuple[int, int], tuple[int, int]]
    ] = dict()
    for y in range(side):
        # 1
        transform[(y, side - 1), (0, -1)] = (3 * side - y - 1, 0), (0, 1)
        transform[(3 * side - y - 1, -1), (0, -1)] = (y, side), (0, 1)
        # 2
        transform[(2 * side - 1, y), (-1, 0)] = (side + y, side), (0, 1)
        transform[(side + y, side - 1), (0, -1)] = (2 * side, y), (1, 0)
        # 3
        transform[(side + y, 2 * side), (0, 1)] = (side - 1, 2 * side + y), (-1, 0)
        transform[(side, 2 * side + y), (1, 0)] = (side + y, 2 * side - 1), (0, -1)
        # 4
        transform[(-1, 2 * side + y), (-1, 0)] = (4 * side - 1, y), (-1, 0)
        transform[(4 * side, y), (1, 0)] = (0, 2 * side + y), (1, 0)
        # 5
        transform[(3 * side + y, -1), (0, -1)] = (0, side + y), (1, 0)
        transform[(-1, side + y), (-1, 0)] = (3 * side + y, 0), (0, 1)
        # 6
        transform[(2 * side + y, 2 * side), (0, 1)] = (side - y - 1, 3 * side - 1), (0, -1)
        transform[(side - y - 1, 3 * side), (0, 1)] = (2 * side + y, 2 * side - 1), (0, -1)
        # 7
        transform[(3 * side, side + y), (1, 0)] = (3 * side + y, side - 1), (0, -1)
        transform[(3 * side + y, side), (0, 1)] = (3 * side - 1, side + y), (-1, 0)
    print(f"{transform}")
    # raise NotImplementedError
    return transform


class TheMap:
    def __init__(self, map_str: list[str]):
        self.transform = gen_transform(map_str)
        self.map = map_str
        self.direction = (0, 1)
        self.y = 0
        self.x = map_str[0].index(EMPTY)
        self.height = len(self.map)
        self.width = len(self.map[0])

    @property
    def password(self) -> int:
        return (self.y + 1) * 1000 + (self.x + 1) * 4 + DIRECTIONS.index(self.direction)

    def move(self, step: tuple[str, int]) -> None:
        direction, count = step
        if direction == L:
            self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) - 1) % len(DIRECTIONS)]
        elif direction == R:
            self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) + 1) % len(DIRECTIONS)]
        elif direction != F:
            raise NotImplementedError
        # is_complex = False
        # steps = []
        # start = (self.y, self.x)
        for _ in range(count):
            y = self.y + self.direction[0]
            x = self.x + self.direction[1]
            new_direction = self.direction
            if (
                y < 0
                or y >= self.height
                or x < 0
                or x >= self.width
                or self.map[y][x] not in [WALL, EMPTY]
            ):
                print(
                    f"self.y = {self.y}",
                    f"self.x = {self.x}",
                    f"self.direction = {self.direction}",
                    f"y = {y}",
                    f"x = {x}",
                )
                is_complex = True
                (y, x), new_direction = self.transform[(y, x), self.direction]
                if (
                    y < 0
                    or y > self.height
                    or x < 0
                    or x > self.width
                    or self.map[y][x] not in [WALL, EMPTY]
                ):
                    print(
                        f"self.y = {self.y}",
                        f"self.x = {self.x}",
                        f"self.direction = {self.direction}",
                        f"y = {y}",
                        f"x = {x}",
                    )
                    raise NotImplementedError
            if self.map[y][x] == WALL:
                break
            elif self.map[y][x] == EMPTY:
                self.y = y
                self.x = x
                self.direction = new_direction
            else:
                raise NotImplementedError
            # steps.append((y, x))
        # if is_complex:
        #     print(f"steps = {steps}")
        #     for y in range(self.height):
        #         for x in range(self.width):
        #             if (y, x) == start:
        #                 symbol = "s"
        #             elif (y, x) == (self.y, self.x):
        #                 symbol = "e"
        #             elif (y, x) in steps:
        #                 symbol = "*"
        #             else:
        #                 symbol = self.map[y][x]
        #             print(symbol, end="")
        #         print()


def main() -> None:
    map_str: list[str] = []
    is_path = False
    max_len = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if is_path:
                path = list(
                    map(
                        lambda x: (str(x[0]), int(x[1])),
                        re.findall(r"([FRL])(\d+)", F + line.strip()),
                    )
                )

            elif len(line) == 1:
                if is_path:
                    raise NotImplementedError
                is_path = True
            else:
                line = line[:-1]
                if len(line) > max_len:
                    max_len = len(line)
                    for index in range(len(map_str)):
                        map_str[index] = map_str[index] + NIL * (max_len - len(map_str[index]))
                elif len(line) - 1 < max_len:
                    line = line + NIL * (max_len - len(line))
                map_str.append(line)
    # for l in map_str:
    #     print(l)
    the_map = TheMap(map_str)
    # print(the_map)
    for step in path:
        the_map.move(step)
        print(
            f"step = {step}",
            f"y = {the_map.y}",
            f"x = {the_map.x}",
            f"direction = {the_map.direction}",
        )
    print(the_map.password)


if __name__ == "__main__":
    main()
