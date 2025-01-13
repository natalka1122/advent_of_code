FILENAME = "demo1.txt"  # expected 80
# FILENAME = "demo2.txt"  # expected 436
# FILENAME = "demo4.txt"  # expected 236
# FILENAME = "demo5.txt"  # expected 368
# FILENAME = "demo3.txt"  # expected 1206
# FILENAME = "input.txt"


def f(y0: int, x0: int, the_map: list[str]) -> tuple[int, set[tuple[int, int]]]:
    visited = {(y0, x0)}
    Q = {(y0, x0)}
    sides_y: dict[tuple[int, int], list[int]] = dict()
    sides_x: dict[tuple[int, int], list[int]] = dict()
    while len(Q) > 0:
        y1, x1 = Q.pop()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y = y1 + dy
            x = x1 + dx
            if (
                0 <= y < len(the_map)
                and 0 <= x < len(the_map[0])
                and the_map[y][x] == the_map[y1][x1]
            ):
                if (y, x) not in visited:
                    Q.add((y, x))
                    visited.add((y, x))
            else:
                if dy != 0:
                    if (y1, dy) not in sides_y:
                        sides_y[(y1, dy)] = list()
                    sides_y[(y1, dy)].append(x)
                elif dx != 0:
                    if (x1, dx) not in sides_x:
                        sides_x[(x1, dx)] = list()
                    sides_x[(x1, dx)].append(y)
    print(sides_y)
    sides_count = 0
    for side in sides_y.values():
        side.sort()
        sides_count += 1
        for index, value in enumerate(side):
            if index > 0:
                if value - side[index - 1] != 1:
                    sides_count += 1
    for side in sides_x.values():
        side.sort()
        sides_count += 1
        for index, value in enumerate(side):
            if index > 0:
                if value - side[index - 1] != 1:
                    sides_count += 1
    return sides_count * len(visited), visited


def main() -> None:
    the_map = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(line.strip())
    result = 0
    visited: set[tuple[int, int]] = set()
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            if (y, x) not in visited:
                price, current_visited = f(y, x, the_map)
                visited = visited.union(current_visited)
                result += price
    print(result)


if __name__ == "__main__":
    main()
