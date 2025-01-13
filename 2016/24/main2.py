import itertools

FILENAME = "input.txt"
WALL = "#"
EMPTY = "."


def calc_dist(
    source: tuple[int, int],
    the_map: list[list[bool]],
    reverse_poi: dict[tuple[int, int], int],
) -> list[int]:
    Q = [(0, source)]
    visited = {source}
    result: list[int | None] = [None for _ in range(len(reverse_poi))]
    result[reverse_poi[source]] = 0
    while len(Q) > 0 and any(map(lambda x: x is None, result)):
        path, current = Q.pop(0)
        y0, x0 = current
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y = y0 + dy
            x = x0 + dx
            if the_map[y][x] and (y, x) not in visited:
                # print(f"current = {current} {y,x}")
                if (y, x) in reverse_poi:
                    index = reverse_poi[y, x]
                    if result[index] is None or result[index] > path + 1:
                        result[index] = path + 1
                visited.add((y, x))
                Q.append((path + 1, (y, x)))

    if any(map(lambda x: x is None, result)):
        print(f"Path not found, result = {result}")
        raise NotImplementedError
    return result


def main() -> None:
    the_map: list[list[bool]] = []
    poi: dict[int, tuple[int, int]] = dict()
    reverse_poi: dict[tuple[int, int], int] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append([])
            for letter in line.strip():
                if letter == WALL:
                    the_map[-1].append(False)
                else:
                    the_map[-1].append(True)
                    if letter.isdigit():
                        number = int(letter)
                        if number in poi:
                            raise NotImplementedError
                        poi[number] = (len(the_map) - 1, len(the_map[-1]) - 1)
                        reverse_poi[(len(the_map) - 1, len(the_map[-1]) - 1)] = number
                    elif letter != EMPTY:
                        raise NotImplementedError
    # print(f"the_map = {the_map}")
    print(f"poi = {poi}")
    print(f"reverse_poi = {reverse_poi}")
    dist: list[list[int]] = [[] for _ in range(len(poi))]
    for source in poi.keys():
        dist[source] = calc_dist(poi[source], the_map, reverse_poi)
    print(f"dist = {dist}")
    result = None
    for path_ in itertools.permutations(filter(lambda x: x != 0, poi.keys())):
        path = (0,) + path_ + (0,)
        current: int = 0
        for i in range(len(path) - 1):
            p1 = path[i]
            p2 = path[i + 1]
            current += dist[p1][p2]
            if result is not None and current >= result:
                break
        # print(path, current, result)
        if result is None or current < result:
            result = current
    print(result)


if __name__ == "__main__":
    main()
