# FILENAME, SIZE = "demo.txt", 6  # expected 6,1
FILENAME, SIZE = "input.txt", 70


def find_exit(bad_bytes: list[tuple[int, int]]) -> bool:
    start = (0, 0)
    end = (SIZE, SIZE)
    Q = [start]
    dist: dict[tuple[int, int], int] = dict()
    dist[(0, 0)] = 0
    while len(Q) > 0:
        y0, x0 = Q.pop(0)
        if (y0, x0) == end:
            return True
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y <= SIZE and 0 <= x <= SIZE and (y, x) not in bad_bytes:
                if (y, x) not in dist or dist[(y, x)] > dist[(y0, x0)] + 1:
                    dist[(y, x)] = dist[(y0, x0)] + 1
                    Q.append((y, x))
    return False


def main() -> None:
    bad_bytes: list[tuple[int, int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            bad_bytes.append(tuple(map(int, line.strip().split(","))))
    for i in range(1, len(bad_bytes)):
        if not find_exit(bad_bytes[:i]):
            print(f"{bad_bytes[i-1][0]},{bad_bytes[i-1][1]}")
            break
        else:
            print(f"i = {i}")


if __name__ == "__main__":
    main()
