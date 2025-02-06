FILENAME = "demo.txt"  # expected 1147
FILENAME = "input.txt"

OPEN = "."
TREE = "|"
LUMBERYARD = "#"
STEPS = 10


def count_nei(y0: int, x0: int, the_map: list[list[str]]) -> dict[str, int]:
    result = {OPEN: 0, TREE: 0, LUMBERYARD: 0}
    for y in range(max(0, y0 - 1), min(len(the_map), y0 + 2)):
        for x in range(max(0, x0 - 1), min(len(the_map[0]), x0 + 2)):
            if y == y0 and x == x0:
                continue
            result[the_map[y][x]] += 1
    return result


def count_value(the_map: list[list[str]]) -> int:
    lumber = 0
    wood = 0
    for line in the_map:
        for symbol in line:
            if symbol == LUMBERYARD:
                lumber += 1
            elif symbol == TREE:
                wood += 1
    return lumber * wood


def show_map(the_map: list[list[str]]) -> None:
    for line in the_map:
        print("".join(line))


def main() -> None:
    the_map: list[list[str]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(line.strip()))
    # show_map(the_map)
    for i in range(STEPS):
        next_map: list[list[str]] = []
        for y in range(len(the_map)):
            next_map.append([])
            for x in range(len(the_map[y])):
                nei = count_nei(y, x, the_map)
                if the_map[y][x] == OPEN:
                    if nei[TREE] >= 3:
                        symbol = TREE
                    else:
                        symbol = OPEN
                elif the_map[y][x] == TREE:
                    if nei[LUMBERYARD] >= 3:
                        symbol = LUMBERYARD
                    else:
                        symbol = TREE
                elif the_map[y][x] == LUMBERYARD:
                    if nei[LUMBERYARD] >= 1 and nei[TREE] >= 1:
                        symbol = LUMBERYARD
                    else:
                        symbol = OPEN
                else:
                    raise NotImplementedError
                next_map[-1].append(symbol)
        the_map = next_map
        # print(i)
        # show_map(the_map)
    print(count_value(the_map))


if __name__ == "__main__":
    main()
