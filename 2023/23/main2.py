from collections.abc import Iterator

FILENAME = "demo.txt"  # expected 154
FILENAME = "demo1.txt"  # expected 28
FILENAME = "demo2.txt"  # expected 424
FILENAME = "input.txt"

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
PATH = "."
FOREST = "#"
Point = tuple[int, int]
Path = tuple[Point, ...]
LPath = tuple[int, Path]


# def minN(a: int | None, b: int) -> int:
#     if a is None:
#         return b
#     return min(a, b)


# def maxN(a: int | None, b: int) -> int:
#     if a is None:
#         return b
#     return max(a, b)


def has_two_nei(p: Point, the_map: list[list[bool]]) -> bool:
    y0, x0 = p
    nei_count = 0
    for dy, dx in DIRECTIONS:
        y = y0 + dy
        x = x0 + dx
        if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
            if the_map[y][x]:
                nei_count += 1
    return nei_count == 2


def calc_direct_dist(p1: Point, p2: Point, the_map: list[list[bool]]) -> set[int]:
    if p1 >= p2:
        raise NotImplementedError
    result = set()
    Q = {(0, p1)}
    visited = {p1}
    while len(Q) > 0:
        path, current = Q.pop()
        y0, x0 = current
        for dy, dx in DIRECTIONS:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
                if the_map[y][x]:
                    point = (y, x)
                    if point == p1:
                        continue
                    if point == p2:
                        result.add(path + 1)
                    if has_two_nei(point, the_map):
                        if point not in visited:
                            visited.add(point)
                            Q.add((path + 1, point))
    return result


def gen_combination(
    dist: dict[Point, dict[Point, int]],
    num_vnodes: int,
    start: Point,
    end: Point,
    exclude: tuple[Point, ...] | None = None,
    add_len: int = 0,
) -> Iterator[tuple[int, Path]]:
    if num_vnodes <= 0:
        raise NotImplementedError
    if exclude is None:
        exclude = (start,)
    for next_node in dist[start]:
        if next_node not in exclude:
            if next_node == end:
                yield (add_len + dist[start][next_node], exclude + (next_node,))
                continue
            yield from gen_combination(
                dist,
                num_vnodes - 1,
                next_node,
                end,
                exclude + (next_node,),
                add_len + dist[start][next_node],
            )


def main() -> None:
    start: Point | None = None
    the_map: list[list[bool]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(map(lambda x: x != FOREST, line.strip())))
            if len(the_map) == 1:
                start = (0, the_map[0].index(True))
    if start is None:
        raise NotImplementedError
    end = (len(the_map) - 1, the_map[-1].index(True))
    print(f"start = {start} end = {end}")
    v_points: set[Point] = set()
    for y0 in range(len(the_map)):
        for x0 in range(len(the_map[0])):
            if not the_map[y0][x0]:
                continue
            nei_count = 0
            for dy, dx in DIRECTIONS:
                y = y0 + dy
                x = x0 + dx
                if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
                    if the_map[y][x]:
                        nei_count += 1
            if nei_count != 2:
                v_points.add((y0, x0))
    if start not in v_points:
        raise NotImplementedError
    if end not in v_points:
        raise NotImplementedError
    print(f"v_point = {sorted(v_points)}")
    dist: dict[Point, dict[Point, int]] = dict()
    for p1 in v_points:
        for p2 in v_points:
            if p1 < p2:
                current_distances = calc_direct_dist(p1, p2, the_map)
                if len(current_distances) == 1:
                    current_dist = current_distances.pop()
                    if p1 not in dist:
                        dist[p1] = dict()
                    if p2 not in dist:
                        dist[p2] = dict()
                    dist[p1][p2] = current_dist
                    dist[p2][p1] = current_dist
                elif len(current_distances) > 0:
                    raise NotImplementedError
    for key, value in sorted(dist.items()):
        print(f"{key}: {value}")
    best_result = 0
    best_path = None
    for result, exclude in gen_combination(dist, len(dist) - 1, start, end):
        # print(f"result = {result} exclude = {exclude}")
        if best_result is None or best_result < result:
            best_result = result
            best_path = exclude
    print(best_path)
    if best_path is None:
        raise NotImplementedError
    print(len(best_path))
    print(best_result)


if __name__ == "__main__":
    main()
