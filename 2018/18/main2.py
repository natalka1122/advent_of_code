FILENAME = "input.txt"

OPEN = "."
TREE = "|"
LUMBERYARD = "#"
STEPS = 1000000000


def count_nei(y0: int, x0: int, the_map: list[list[str]]) -> dict[str, int]:
    result = {OPEN: 0, TREE: 0, LUMBERYARD: 0}
    for y in range(max(0, y0 - 1), min(len(the_map), y0 + 2)):
        for x in range(max(0, x0 - 1), min(len(the_map[0]), x0 + 2)):
            if y == y0 and x == x0:
                continue
            result[the_map[y][x]] += 1
    return result


def show_map(the_map: list[list[str]]) -> str:
    result = []
    for line in the_map:
        result.append("".join(line))
    return "\n".join(result)


def main() -> None:
    the_map: list[list[str]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(line.strip()))
    visited = {show_map(the_map): 0}
    i = 0
    while i < STEPS:
        i += 1
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
        map_str = show_map(the_map)
        if map_str in visited:
            period = i - visited[map_str]
            while i + period < STEPS:
                i += period
        else:
            visited[map_str] = i
    print(map_str.count(TREE) * map_str.count(LUMBERYARD))


if __name__ == "__main__":
    main()
