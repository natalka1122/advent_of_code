import re
import random

# FILENAME = "demo.txt"  # expected 5
# FILENAME = "demo1.txt"  # expected 3
# FILENAME = "demo2.txt"  # expected 2 AC
# FILENAME = "demo3.txt"  # expected 2 AD
# FILENAME = "demo4.txt"  # expected 3
FILENAME = "demo5.txt"  # expected ?
FILENAME = "input.txt"
GROUD = 1
INF = 100500
EMPTY = -1


class Brick:
    def __init__(self, line: str) -> None:
        line_groups = re.match(r"^(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)$", line.strip())
        if line_groups is None:
            raise NotImplementedError
        self.x1, self.y1, self.z1, self.x2, self.y2, self.z2 = map(
            int, line_groups.groups()
        )
        if len(str(self.x1)) > 1:
            raise NotImplementedError
        if len(str(self.y1)) > 2:
            raise NotImplementedError
        if len(str(self.z1)) > 3:
            raise NotImplementedError
        self.index = f"{self.x1:01}{self.y1:01}{self.z1:03}"
        if self.x1 > self.x2:
            raise NotImplementedError
        if self.y1 > self.y2:
            raise NotImplementedError
        if self.z1 > self.z2:
            raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.index}: {self.x1},{self.y1},{self.z1}~{self.x2},{self.y2},{self.z2}"


def can_fall_down(bricks: list[Brick], the_map: list[list[list[int]]]) -> bool:
    for brick in bricks:
        # print(f"index = {index} brick = {brick}")
        if brick.z1 == GROUD:
            continue
        can_fall_down_flag = True
        z = brick.z1 - 1
        while z >= 0:
            # print(f"z = {z}")
            for y in range(brick.y1, brick.y2 + 1):
                for x in range(brick.x1, brick.x2 + 1):
                    if the_map[z][y][x] != EMPTY:
                        can_fall_down_flag = False
                        break
                if not can_fall_down_flag:
                    break
            if not can_fall_down_flag:
                break
            z -= 1
        # print(f"fin: z = {z}")
        if z < brick.z1 - 1:
            return True
    return False


def add_brick(brick: Brick, the_map: list[list[list[int]]]) -> None:
    for z in range(brick.z1, brick.z2 + 1):
        for y in range(brick.y1, brick.y2 + 1):
            for x in range(brick.x1, brick.x2 + 1):
                if the_map[z][y][x] != EMPTY:
                    raise NotImplementedError
                the_map[z][y][x] = brick.index


def remove_brick(brick: Brick, the_map: list[list[list[int]]]) -> None:
    for z in range(brick.z1, brick.z2 + 1):
        for y in range(brick.y1, brick.y2 + 1):
            for x in range(brick.x1, brick.x2 + 1):
                if the_map[z][y][x] != brick.index:
                    raise NotImplementedError
                the_map[z][y][x] = EMPTY


def fall_one(brick: Brick, new_z: int, the_map: list[list[list[int]]]) -> None:
    remove_brick(brick, the_map)
    brick.z1, brick.z2 = new_z, brick.z2 - brick.z1 + new_z
    print(f"brick = {brick} new_z = {new_z}")
    add_brick(brick, the_map)


def fall_all(bricks: list[Brick], the_map: list[list[list[int]]]) -> None:
    for index, brick in enumerate(bricks):
        print(f"index = {index} brick = {brick}")
        if brick.z1 == GROUD:
            continue
        can_fall_down_flag = True
        z = brick.z1 - 1
        while z >= 0:
            # print(f"z = {z}")
            for y in range(brick.y1, brick.y2 + 1):
                for x in range(brick.x1, brick.x2 + 1):
                    if the_map[z][y][x] != EMPTY:
                        can_fall_down_flag = False
                        break
                if not can_fall_down_flag:
                    break
            if not can_fall_down_flag:
                break
            z -= 1
        print(f"fin: z = {z}")
        if z < brick.z1 - 1:
            print(f"Can fall down")
            fall_one(brick, z + 1, the_map)
        else:
            print(f"Can not fall down")
    return


def main() -> None:
    bricks: list[Brick] = list()
    min_x = INF
    max_x = GROUD
    min_y = INF
    max_y = GROUD
    min_z = INF
    max_z = GROUD
    with open(FILENAME, "r") as file:
        for line in file:
            line_groups = re.match(
                r"^(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)$", line.strip()
            )
            if line_groups is None:
                raise NotImplementedError
            bricks.append(Brick(line))
            min_x = min(min_x, bricks[-1].x1)
            max_x = max(max_x, bricks[-1].x2)
            min_y = min(min_y, bricks[-1].y1)
            max_y = max(max_y, bricks[-1].y2)
            min_z = min(min_z, bricks[-1].z1)
            max_z = max(max_z, bricks[-1].z2)
    bricks.sort(key=lambda x: x.z1)
    the_map: list[list[list[int]]] = []
    for _ in range(max_z + 1):
        the_map.append([])
        for _ in range(max_y + 1):
            the_map[-1].append([])
            for _ in range(max_x + 1):
                the_map[-1][-1].append(EMPTY)
    for brick in bricks:
        add_brick(brick, the_map)
    print(the_map)
    print("\n".join(map(str, bricks)))
    print(min_z, max_z, min_y, max_y, min_x, max_x)
    # print(can_fall_down(bricks, the_map))
    fall_all(bricks, the_map)
    print("\n".join(map(str, bricks)))
    if can_fall_down(bricks, the_map):
        raise NotImplementedError
    result = 0
    print(the_map)
    for brick in bricks:
        remove_brick(brick, the_map)
        if not can_fall_down(bricks, the_map):
            print(f"brick {brick} can get disintegrated")
            result += 1
        else:
            print(f"brick {brick} can not get disintegrated")
        add_brick(brick, the_map)
    print(result)


if __name__ == "__main__":
    main()
