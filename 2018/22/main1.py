FILENAME = "demo.txt"  # expected 114
FILENAME = "input.txt"

ROCKY = 0
WET = 1
NARROW = 2
BIG_NUMBER = 20183
X_NUMBER = 48271
Y_NUMBER = 16807


def main() -> None:
    depth = None
    target = None
    with open(FILENAME, "r") as file:
        for line in file:
            if line.startswith("depth"):
                depth = int(line.split(" ")[1])
            elif line.startswith("target"):
                line_split = line.split(" ")[1].split(",")
                target = int(line_split[0]), int(line_split[1])
            else:
                raise NotImplementedError
    if depth is None or target is None:
        raise NotImplementedError
    print(depth, target)
    result = 0
    the_map: list[list[int]] = []
    for y in range(target[0] + 1):
        the_map.append([])
        for x in range(target[1] + 1):
            if y == 0:
                if x == 0:
                    value = 0
                else:
                    value = x * X_NUMBER
            elif x == 0:
                value = y * Y_NUMBER
            elif (y, x) == target:
                value = 0
            else:
                value = the_map[y - 1][x] * the_map[y][x - 1]
            the_map[y].append((value + depth) % BIG_NUMBER)
            result += the_map[y][x] % 3
        # print(the_map[y])
    print(result)


if __name__ == "__main__":
    main()
