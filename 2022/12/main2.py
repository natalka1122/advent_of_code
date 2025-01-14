FILENAME = "demo.txt"  # expected 29
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
    start = []
    end = None
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append([])
            for symbol in line.strip():
                if symbol == START:
                    the_map[-1].append(get_elevation(A))
                elif symbol == END:
                    if end is not None:
                        raise NotImplementedError
                    the_map[-1].append(get_elevation(Z))
                    end = len(the_map) - 1, len(the_map[-1]) - 1
                elif "a" <= symbol <= "z":
                    the_map[-1].append(get_elevation(symbol))
                else:
                    raise NotImplementedError
                if the_map[-1][-1] == get_elevation(A):
                    start.append((len(the_map) - 1, len(the_map[-1]) - 1))

    if len(start) == 0 or end is None:
        raise NotImplementedError
    Q = start
    dist = {}
    for point in start:
        dist[point]= 0
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

    print(dist[end])


if __name__ == "__main__":
    main()
