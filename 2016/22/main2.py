import re

FILENAME = "demo.txt"  # expected 7
FILENAME = "input.txt"

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
SMALL_VS_BIG = 100


def main() -> None:
    nodes: list[list[tuple[int, int]]] = []
    big_nodes: set[tuple[int, int]] = set()
    small_nodes: set[tuple[int, int]] = set()
    empty_nodes: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.search(
                r"node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+\%", line
            )
            if line_match is None:
                print(f"skipped line: {line.strip()}")
            else:
                key = (int(line_match.group(1)), int(line_match.group(2)))
                if key[0] == len(nodes):
                    nodes.append([])
                if key[1] != len(nodes[-1]):
                    raise NotImplementedError
                nodes[-1].append((int(line_match.group(3)), int(line_match.group(4))))
                if nodes[-1][-1][0] == 0:
                    empty_nodes.add(key)
                if nodes[-1][-1][0] > SMALL_VS_BIG:
                    big_nodes.add(key)
                else:
                    small_nodes.add(key)
    target_node = (0, 0)
    source_node = (len(nodes) - 1, 0)
    print(f"source_node = {source_node}")
    print(f"target_node = {target_node}")
    print(f"empty_nodes = {empty_nodes}")
    print(f"big_nodes = {big_nodes}")
    # find max free space on big_nodes
    max_free_on_big = 0
    for x, y in big_nodes:
        max_free_on_big = max(max_free_on_big, nodes[x][y][1])
    # find max free space on small nodes
    # find max used space on small nodes
    max_free_on_small = 0
    min_used_on_small = None
    for x, y in small_nodes:
        if nodes[x][y][0] == 0:
            continue
        max_free_on_small = max(max_free_on_small, nodes[x][y][1])
        if min_used_on_small is None or min_used_on_small > nodes[x][y][0]:
            min_used_on_small = nodes[x][y][0]
    if min_used_on_small is None:
        raise NotImplementedError
    if max_free_on_big >= min_used_on_small:
        print(f"max_free_on_big = {max_free_on_big} >= {min_used_on_small}")
        raise NotImplementedError
    if max_free_on_small >= min_used_on_small:
        print(
            f"max_free_on_big = {max_free_on_small} >= {min_used_on_small} = min_used_on_small"
        )
        raise NotImplementedError
    if len(empty_nodes) != 1:
        raise NotImplementedError
    # verified limitations
    empty_node = empty_nodes.pop()
    Q = {
        (
            0,
            empty_node,
            source_node,
        )
    }
    paths: dict[
        tuple[tuple[int, int], tuple[int, int]],
        list[tuple[tuple[int, int], tuple[int, int]]],
    ] = {(empty_node, source_node): []}
    prev_steps = 0
    win_steps = 100500
    while len(Q) > 0:
        current = min(Q)
        Q.remove(current)
        steps, current_empty, current_source = current
        if current_source == target_node:
            print(paths[current_empty, current_source])
            break
        if steps != prev_steps:
            prev_steps = steps
            print(f"current = {current} len(Q) = {len(Q)}")
        if steps > win_steps:
            break
        for dx, dy in DIRECTIONS:
            x = current_empty[0] + dx
            y = current_empty[1] + dy
            new_empty = (x, y)
            if new_empty not in small_nodes:
                continue
            if new_empty == current_source:
                if current_empty == target_node:
                    print(f"Found it {steps+1}")
                    win_steps = steps + 1
                new_visited = (current_source, current_empty)
                if new_visited in paths:
                    continue
                paths[new_visited] = paths[current_empty, current_source] + [
                    ((x, y), (current_source))
                ]
                Q.add(
                    (
                        steps + 1,
                        current_source,
                        current_empty,
                    )
                )
            else:
                new_visited = (new_empty, current_source)
                if new_visited in paths:
                    continue
                paths[new_visited] = paths[current_empty, current_source] + [
                    ((x, y), (current_source))
                ]
                Q.add(
                    (
                        steps + 1,
                        new_empty,
                        current_source,
                    )
                )


if __name__ == "__main__":
    main()
