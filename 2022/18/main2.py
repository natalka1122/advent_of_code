FILENAME = "demo2.txt"  # expected 58
FILENAME = "input.txt"

MAX = 100500
Point = tuple[int, int, int]


def main() -> None:
    cubes = set()
    limits = [[MAX, -MAX], [MAX, -MAX], [MAX, -MAX]]
    with open(FILENAME, "r") as file:
        for line in file:
            z, y, x = map(int, line.strip().split(","))
            cubes.add((z, y, x))
            limits[0][0] = min(limits[0][0], z)
            limits[0][1] = max(limits[0][1], z)
            limits[1][0] = min(limits[1][0], y)
            limits[1][1] = max(limits[1][1], y)
            limits[2][0] = min(limits[2][0], x)
            limits[2][1] = max(limits[2][1], x)
    print(limits)
    result = 0
    Q: set[Point] = {(limits[0][0] - 1, limits[1][0] - 1, limits[2][0] - 1)}
    visited = set()
    while len(Q) > 0:
        z, y, x = Q.pop()
        visited.add((z, y, x))
        for nei in [
            (z - 1, y, x),
            (z + 1, y, x),
            (z, y - 1, x),
            (z, y + 1, x),
            (z, y, x - 1),
            (z, y, x + 1),
        ]:
            if (
                limits[0][0] - 1 <= nei[0] <= limits[0][1] + 1
                and limits[1][0] - 1 <= nei[1] <= limits[1][1] + 1
                and limits[2][0] - 1 <= nei[2] <= limits[2][1] + 1
            ):
                if nei in cubes:
                    result += 1
                elif nei not in visited:
                    Q.add(nei)
    print(result)


if __name__ == "__main__":
    main()
