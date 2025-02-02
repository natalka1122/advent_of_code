import re

FILENAME = "demo.txt"  # expected 6032
FILENAME = "demo1.txt"  # expected 1041
FILENAME = "demo2.txt"  # expected 1045
FILENAME = "demo3.txt"  # expected 1045
FILENAME = "demo4.txt"  # expected 1043
FILENAME = "demo5.txt"  # expected 1047
FILENAME = "demo6.txt"  # expected 1036
FILENAME = "input.txt"


F = "F"
L = "L"
R = "R"
EMPTY = "."
WALL = "#"
NIL = " "
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class TheMap:
    def __init__(self, map_str: list[str]):
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
            self.direction = DIRECTIONS[
                (DIRECTIONS.index(self.direction) - 1) % len(DIRECTIONS)
            ]
        elif direction == R:
            self.direction = DIRECTIONS[
                (DIRECTIONS.index(self.direction) + 1) % len(DIRECTIONS)
            ]
        elif direction != F:
            raise NotImplementedError
        for _ in range(count):
            y = (self.y + self.direction[0]) % self.height
            x = (self.x + self.direction[1]) % self.width
            while self.map[y][x] != WALL and self.map[y][x] != EMPTY:
                y = (y + self.direction[0]) % self.height
                x = (x + self.direction[1]) % self.width
            if self.map[y][x] == WALL:
                break
            elif self.map[y][x] == EMPTY:
                self.y = y
                self.x = x
            else:
                raise NotImplementedError


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
                        map_str[index] = map_str[index] + NIL * (
                            max_len - len(map_str[index])
                        )
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
