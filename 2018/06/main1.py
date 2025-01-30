FILENAME = "demo.txt"  # expected 17
FILENAME = "input.txt"


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
    counter = dict()
    for y0 in range(min_y, max_y + 1):
        for x0 in range(min_x, max_x + 1):
            best_dist = max_dist
            best_node_index = None
            for index, node in enumerate(nodes):
                current_dist = dist(y0, x0, node[0], node[1])
                if current_dist < best_dist:
                    best_dist = current_dist
                    best_node_index = index
                elif current_dist == best_dist:
                    best_node_index = None
            if (
                best_node_index is not None
                and nodes[best_node_index][0] not in [min_y, max_y]
                and nodes[best_node_index][1] not in [min_x, max_x]
            ):
                if best_node_index not in counter:
                    counter[best_node_index] = 0
                counter[best_node_index] += 1
    print(counter)
    print(max(counter.values()))


if __name__ == "__main__":
    main()
