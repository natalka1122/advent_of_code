# FILENAME = "demo1.txt"  # expected 140
# FILENAME = "demo2.txt"  # expected 772
# FILENAME = "demo3.txt"  # expected 1930
FILENAME = "input.txt"


def f(y0: int, x0: int, the_map: list[str]) -> tuple[int, set[tuple[int, int]]]:
    perimeter = 0
    visited = {(y0, x0)}
    Q = {(y0, x0)}
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
                perimeter += 1
    print(f"perimeter = {perimeter}")
    return perimeter * len(visited), visited


def main() -> None:
    the_map = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(line.strip())
    print(the_map)
    result = 0
    visited: set[tuple[int, int]] = set()
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            if (y, x) not in visited:
                price, current_visited = f(y, x, the_map)
                print(
                    f"y = {y} x = {x} symbol = {the_map[y][x]} price = {price} current_visited = {current_visited}"
                )
                visited = visited.union(current_visited)
                result += price
    print(result)


if __name__ == "__main__":
    main()
