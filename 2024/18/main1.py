# FILENAME, SIZE, TIME = "demo.txt", 6, 12  # expected 22
FILENAME, SIZE, TIME = "input.txt", 70, 1024


def main():
    bad_bytes: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for _ in range(TIME):
            # for line in file:
            bad_bytes.add(tuple(map(int, file.readline().strip().split(","))))
    print(bad_bytes)
    start = (0, 0)
    end = (SIZE, SIZE)
    Q = [start]
    dist: dict[tuple[int, int], int] = dict()
    dist[(0, 0)] = 0
    while len(Q) > 0:
        y0, x0 = Q.pop(0)
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y <= SIZE and 0 <= x <= SIZE and (y, x) not in bad_bytes:
                if (y, x) not in dist or dist[(y, x)] > dist[(y0, x0)] + 1:
                    dist[(y, x)] = dist[(y0, x0)] + 1
                    Q.append((y, x))
    print(dist[end])


if __name__ == "__main__":
    main()
