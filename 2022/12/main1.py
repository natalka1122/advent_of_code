# FILENAME = "demo.txt"  # expected 31
FILENAME = "input.txt"

A = "a"
Z = "z"
START = "S"
END = "E"
DIRECTIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def get_elevation(s: str) -> int:
    if A <= s <= Z:
        return ord(s) - ord(A)
    raise NotImplementedError


def main() -> None:
    the_map: list[list[int]] = []
    start = None
    end = None
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append([])
            for symbol in line.strip():
                if symbol == START:
                    the_map[-1].append(get_elevation(A))
                    start = len(the_map) - 1, len(the_map[-1]) - 1
                elif symbol == END:
                    the_map[-1].append(get_elevation(Z))
                    end = len(the_map) - 1, len(the_map[-1]) - 1
                elif "a" <= symbol <= "z":
                    the_map[-1].append(get_elevation(symbol))
    if start is None or end is None:
        raise NotImplementedError
    # print(start)
    # print(end)
    # print(the_map)
    Q = [start]
    dist = {start: 0}
    is_found = False
    while not is_found and len(Q) > 0:
        current = Q.pop(0)
        y0, x0 = current
        for dy, dx in DIRECTIONS:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
                if the_map[y][x] <= the_map[y0][x0] + 1:
                    if (y, x) not in dist or dist[y, x] > dist[y0, x0] + 1:
                        dist[y, x] = dist[y0, x0] + 1
                        Q.append((y, x))
                        if (y, x) == end:
                            is_found = True
                            break
    # for key in sorted(dist.keys()):
    #     print(key, dist[key])
    print(dist[end])


if __name__ == "__main__":
    main()
