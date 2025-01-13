from collections.abc import Iterator
import re

# FILENAME = "demo.txt"  # expected 5
# FILENAME = "demo1.txt"  # expected 3
# FILENAME = "demo2.txt"  # expected 2 AC
# FILENAME = "demo3.txt"  # expected 2 AD
# FILENAME = "demo4.txt"  # expected 3
# FILENAME = "demo5.txt"  # expected ?
FILENAME = "input.txt"
GROUND = 1, 0, 0


class Brick:
    def __init__(self, line: str) -> None:
        line_groups = re.match(r"^(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)$", line.strip())
        if line_groups is None:
            raise NotImplementedError
        if len(line_groups.group(1)) > 1:
            raise NotImplementedError
        if len(line_groups.group(2)) > 1:
            raise NotImplementedError
        if len(line_groups.group(3)) > 3:
            raise NotImplementedError
        x1, y1, z1, x2, y2, z2 = map(int, line_groups.groups())
        if (
            z1 < GROUND[0]
            or y1 < GROUND[1]
            or x1 < GROUND[2]
            or x1 > x2
            or y1 > y2
            or z1 > z2
        ):
            raise NotImplementedError
        self.items: tuple[tuple[int, int], tuple[int, int], tuple[int, int]] = (
            (z1 - GROUND[0], z2 - GROUND[0] + 1),
            (y1 - GROUND[1], y2 - GROUND[1] + 1),
            (x1 - GROUND[2], x2 - GROUND[2] + 1),
        )
        self.index = f"{line_groups.group(1):0>1}{line_groups.group(2):0>1}{line_groups.group(3):0>3}"

    def __repr__(self) -> str:
        return f"{self.index}: {self.items[2][0]},{self.items[1][0]},{self.items[0][0]}~{self.items[2][1]},{self.items[1][1]},{self.items[0][1]}"

    def __hash__(self) -> int:
        return hash(self.items)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Brick):
            return False
        return self.items == other.items


class Space:
    def __init__(self) -> None:
        self.bricks: set[Brick] = set()
        self.limits: tuple[int, int, int] = (1, 1, 1)
        self.field: list[list[list[Brick | None]]] = [[[None]]]

    def add_brick(self, brick: Brick) -> None:
        if brick in self.bricks:
            raise NotImplementedError
        self.bricks.add(brick)
        new_limits_list: list[int] = []
        for i in range(3):
            new_limits_list.append(max(self.limits[i], brick.items[i][1]))
        new_limits = tuple(new_limits_list)
        if len(new_limits) != 3:
            raise NotImplementedError
        if new_limits != self.limits:
            self.limits = new_limits
            for z in range(self.limits[0]):
                if len(self.field) == z:
                    self.field.append([])
                for y in range(self.limits[1]):
                    if len(self.field[z]) == y:
                        self.field[z].append([])
                    for x in range(self.limits[2]):
                        if len(self.field[z][y]) == x:
                            self.field[z][y].append(None)

        for z in range(brick.items[0][0], brick.items[0][1]):
            for y in range(brick.items[1][0], brick.items[1][1]):
                for x in range(brick.items[2][0], brick.items[2][1]):
                    self.field[z][y][x] = brick

    def drop_one(self) -> bool:
        for brick in self.bricks:
            if brick.items[0][0] == 0:
                continue
            is_target = True
            z1 = brick.items[0][0] - 1
            for y in range(brick.items[1][0], brick.items[1][1]):
                for x in range(brick.items[2][0], brick.items[2][1]):
                    if self.field[z1][y][x] is not None:
                        is_target = False
                        break
                if not is_target:
                    break
            if is_target:
                z2 = brick.items[0][1] - 1
                for y in range(brick.items[1][0], brick.items[1][1]):
                    for x in range(brick.items[2][0], brick.items[2][1]):
                        self.field[z1][y][x] = brick
                        self.field[z2][y][x] = None
                brick.items = (
                    (brick.items[0][0] - 1, brick.items[0][1] - 1),
                    brick.items[1],
                    brick.items[2],
                )
                return True
        return False

    def get_impossible_disintegrations(self) -> Iterator[Brick]:
        for brick in self.bricks:
            if brick.items[0][0] != 0:
                nei_from_below: set[Brick] = set()
                z1 = brick.items[0][0] - 1
                for y in range(brick.items[1][0], brick.items[1][1]):
                    for x in range(brick.items[2][0], brick.items[2][1]):
                        current = self.field[z1][y][x]
                        if current is not None:
                            nei_from_below.add(current)
                if len(nei_from_below) == 1:
                    yield nei_from_below.pop()


def main() -> None:
    space = Space()
    with open(FILENAME, "r") as file:
        for line in file:
            line_groups = re.match(
                r"^(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)$", line.strip()
            )
            if line_groups is None:
                raise NotImplementedError
            space.add_brick(Brick(line))
    is_changed = True
    while is_changed:
        is_changed = space.drop_one()
    print("Dropped")

    impossible_disintegrations: set[Brick] = set()
    for brick in space.get_impossible_disintegrations():
        impossible_disintegrations.add(brick)
    print(f"impossible_disintegrations = {len(impossible_disintegrations)}")
    print(len(space.bricks) - len(impossible_disintegrations))


if __name__ == "__main__":
    main()
