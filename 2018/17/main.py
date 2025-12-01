import re

FILENAME = "demo.txt"  # expected 57
# FILENAME = "input.txt"

Y = "y"
X = "x"
SAND = 0
CLAY = 1
WATER = 2
WAS_WATER = 3
START_POSITION = 0, 500


def show_map(the_map: list[list[int]]) -> None:
    for line in the_map:
        for symbol in line:
            if symbol == SAND:
                print(".", end="")
            elif symbol == CLAY:
                print("#", end="")
            elif symbol == WATER:
                print("~", end="")
            elif symbol == WAS_WATER:
                print("|", end="")
            else:
                raise NotImplementedError
        print()


def main() -> None:
    start_pos = START_POSITION
    clay_blocks: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"([xy])=(\d+), ([xy])=(\d+)\.\.(\d+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            a = int(line_match.group(2))
            b = int(line_match.group(4))
            c = int(line_match.group(5))
            if line_match.group(1) == Y and line_match.group(3) == X:
                clay_blocks.add(((a, a), (b, c)))
            elif line_match.group(1) == X and line_match.group(3) == Y:
                clay_blocks.add(((b, c), (a, a)))
            else:
                raise NotImplementedError
    print(clay_blocks)
    min_y = start_pos[0]
    max_y = start_pos[0]
    min_x = start_pos[1]
    max_x = start_pos[1]
    for y_coord, x_coord in clay_blocks:
        if y_coord[0] <= min_y:
            raise NotImplementedError
        max_y = max(max_y, y_coord[1])
        min_x = min(min_x, x_coord[0])
        max_x = max(max_x, x_coord[1])
    min_x -= 1
    max_x += 1
    print(f"min_y = {min_y}", f"max_y = {max_y}", f"min_x = {min_x}", f"max_x = {max_x}")
    the_map = []
    for y in range(max_y - min_y + 1):
        the_map.append([SAND for _ in range(max_x - min_x + 1)])
    for y_coord, x_coord in clay_blocks:
        for y in range(y_coord[0], y_coord[1] + 1):
            for x in range(x_coord[0], x_coord[1] + 1):
                the_map[y - min_y][x - min_x] = CLAY
    show_map(the_map)
    # while True:


if __name__ == "__main__":
    main()
