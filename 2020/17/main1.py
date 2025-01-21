FILENAME = "demo.txt"  # expected 112
FILENAME = "input.txt"

CYCLES_COUNT = 6
ACTIVE = "#"


def calc_nei(z0: int, y0: int, x0: int, the_map: set[tuple[int, int, int]]) -> int:
    result = 0
    for z in [z0 - 1, z0, z0 + 1]:
        for y in [y0 - 1, y0, y0 + 1]:
            for x in [x0 - 1, x0, x0 + 1]:
                if (z, y, x) == (z0, y0, x0):
                    continue
                if (z, y, x) in the_map:
                    result += 1
    return result


def f(the_map: set[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    result: set[tuple[int, int, int]] = set()
    visited: set[tuple[int, int, int]] = set()
    for z0, y0, x0 in the_map:
        for z in [z0 - 1, z0, z0 + 1]:
            for y in [y0 - 1, y0, y0 + 1]:
                for x in [x0 - 1, x0, x0 + 1]:
                    if (z, y, x) in visited:
                        continue
                    visited.add((z, y, x))
                    neis = calc_nei(z, y, x, the_map)
                    if (z, y, x) in the_map and neis in [2, 3]:
                        result.add((z, y, x))
                    elif (z, y, x) not in the_map and neis == 3:
                        result.add((z, y, x))
    return result


def main() -> None:
    the_map: set[tuple[int, int, int]] = set()
    y = 0
    with open(FILENAME, "r") as file:
        for line in file:
            for x in range(len(line)):
                if line[x] == ACTIVE:
                    the_map.add((0, y, x))
            y += 1
    print(the_map)
    for _ in range(CYCLES_COUNT):
        the_map = f(the_map)
        # print(sorted(the_map))
        # for z in range(-4, 4):
        #     print(f"z = {z}")
        #     for y in range(-4, 6):
        #         for x in range(-4, 6):
        #             if (z, y, x) in the_map:
        #                 print(ACTIVE, end="")
        #             else:
        #                 print(".", end="")
        #         print()
    print(len(the_map))


if __name__ == "__main__":
    main()
