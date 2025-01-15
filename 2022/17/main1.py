from __future__ import annotations

FILENAME = "demo.txt"  # expected 3068
FILENAME = "input.txt"

ROCKS_COUNT = 2022
WIDTH = 7
POSITION_X = 2
POSITION_Y = 3
EMPTY_STR = "."
ROCK_STR = "#"
LEFT = "<"
ROCKS = list(
    map(
        lambda x: list(map(lambda y: list(map(lambda z: z != EMPTY_STR, y)), x)),
        [
            ["####"],
            [".#.", "###", ".#."],
            ["###", "..#", "..#"],
            ["#", "#", "#", "#"],
            ["##", "##"],
        ],
    )
)


class IsOccupied(Exception):
    pass


class Chamber:
    def __init__(self) -> None:
        self.the_map: list[list[bool]] = []
        self.rock: tuple[int, int, int] | None = None

    def show(self) -> str:
        result: list[str] = []
        for y in range(len(self.the_map)):
            result.append("")
            for x in range(WIDTH):
                if self.the_map[y][x]:
                    result[-1] += ROCK_STR
                else:
                    result[-1] += EMPTY_STR
        return "\n".join(result[::-1])

    @property
    def height(self) -> int:
        return len(self.the_map)

    def throw_rock(self, rock_index: int) -> None:
        if self.rock is not None:
            raise NotImplementedError
        if rock_index < 0 or rock_index >= len(ROCKS):
            raise NotImplementedError
        self.rock = (POSITION_Y + len(self.the_map), POSITION_X, rock_index)

    def can_go(self, dy: int, dx: int) -> bool:
        if self.rock is None:
            raise NotImplementedError
        current_rock = ROCKS[self.rock[2]]
        for y0 in range(len(current_rock)):
            y = y0 + dy + self.rock[0]
            if y < 0:
                return False
            for x0 in range(len(current_rock[0])):
                if not current_rock[y0][x0]:
                    continue
                x = x0 + dx + self.rock[1]
                if x < 0 or x >= WIDTH:
                    return False
                if len(self.the_map) <= y:
                    continue
                if self.the_map[y][x]:
                    return False
        return True

    def move(self, dy: int, dx: int) -> None:
        if self.rock is None:
            raise NotImplementedError
        if not self.can_go(dy, dx):
            raise IsOccupied
        self.rock = (self.rock[0] + dy, self.rock[1] + dx, self.rock[2])

    def freeze_rock(self) -> None:
        if self.rock is None:
            raise NotImplementedError
        current_rock = ROCKS[self.rock[2]]
        for y0 in range(len(current_rock)):
            y = y0 + self.rock[0]
            if y < 0:
                raise NotImplementedError
            while y >= len(self.the_map):
                self.the_map.append([False for _ in range(WIDTH)])
            for x0 in range(len(current_rock[0])):
                x = x0 + self.rock[1]
                if x < 0 or x >= WIDTH:
                    raise NotImplementedError
                if current_rock[y0][x0]:
                    if self.the_map[y][x]:
                        raise NotImplementedError
                    self.the_map[y][x] = True
        self.rock = None

    def take_action(self, is_left: bool) -> bool:
        if self.rock is None:
            raise NotImplementedError
        if is_left:
            dx = -1
        else:
            dx = 1
        try:
            self.move(0, dx)
        except IsOccupied:
            pass
        try:
            self.move(-1, 0)
        except IsOccupied:
            self.freeze_rock()
            return True
        return False


def f(line: str) -> int:
    rock_index = 0
    chamber = Chamber()
    line_index = 0
    chamber.throw_rock(rock_index)
    while rock_index < ROCKS_COUNT:
        symbol = line[line_index]
        has_landed = chamber.take_action(symbol == LEFT)
        # print(f"chamber.rock = {chamber.rock} has_landed = {has_landed}")
        if has_landed:
            # print(chamber.show())
            rock_index += 1
            chamber.throw_rock(rock_index % len(ROCKS))
            # print(rock_index)
        line_index = (line_index + 1) % len(line)
    return chamber.height


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
