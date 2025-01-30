FILENAME, LESS_THEN = "demo.txt", 32  # expected 16
FILENAME, LESS_THEN = "input.txt", 10000


def dist(y1: int, x1: int, y2: int, x2: int) -> int:
    return abs(y1 - y2) + abs(x1 - x2)


def main() -> None:
    nodes: list[tuple[int, int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_split = tuple(map(int, line.strip().split(", ")))
            if len(line_split) != 2:
                raise NotImplementedError
            nodes.append(line_split)
    print(nodes)
    min_y = min(map(lambda x: x[0], nodes))
    min_x = min(map(lambda x: x[1], nodes))
    max_y = max(map(lambda x: x[0], nodes))
    max_x = max(map(lambda x: x[1], nodes))
    max_dist = dist(min_y, min_x, max_y, max_x)
    counter = 0
    for y0 in range(min_y, max_y + 1):
        for x0 in range(min_x, max_x + 1):
            current_dist = 0
            for y, x in nodes:
                current_dist += dist(y0, x0, y, x)
                if current_dist >= LESS_THEN:
                    break
            if current_dist < LESS_THEN:
                counter += 1
    print(counter)


if __name__ == "__main__":
    main()
