FILENAME, TARGET = "demo.txt", (4, 7)  # expected 11
FILENAME, TARGET = "input.txt", (39, 31)
START = 1, 1


def is_empty(y: int, x: int, n: int) -> bool:
    return bin(x * x + 3 * x + 2 * x * y + y + y * y + n)[2:].count("1") % 2 == 0


def f(n: int) -> int:
    the_map: list[list[bool]] = []
    for y in range(2 * TARGET[0]):
        the_map.append([])
        for x in range(2 * TARGET[1]):
            the_map[y].append(is_empty(y, x, n))
    visited = set()
    Q = [(0, START)]
    while len(Q) > 0:
        step, current = Q.pop(0)
        y0, x0 = current
        for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            y = y0 + dy
            x = x0 + dx
            if not 0 <= y < len(the_map) or not 0 <= x < len(the_map[0]):
                continue
            coord = (y, x)
            if the_map[y][x] and coord not in visited:
                if coord == TARGET:
                    return step+1
                visited.add(coord)
                Q.append((step + 1, coord))


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line)))


if __name__ == "__main__":
    main()
