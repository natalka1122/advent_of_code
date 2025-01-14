FILENAME = "demo.txt"  # expected 24
FILENAME = "input.txt"

START = (500, 0)

Point = tuple[int, int]


def sign(a: int, b: int) -> int:
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def main() -> None:
    the_map: set[Point] = set()
    min_x = START[0]
    max_x = START[0]
    min_y = START[1]
    max_y = START[1]
    with open(FILENAME, "r") as file:
        for line in file:
            points: list[Point] = []
            for item in line.strip().split(" -> "):
                points.append((int(item.split(",")[0]), int(item.split(",")[1])))
            print(points)
            for point in points:
                min_x = min(min_x, point[0])
                max_x = max(max_x, point[0])
                min_y = min(min_y, point[1])
                max_y = max(max_y, point[1])
            for index in range(len(points) - 1):
                if (
                    points[index][0] == points[index + 1][0]
                    and points[index][1] != points[index + 1][1]
                ):
                    for x in range(
                        points[index][1],
                        points[index + 1][1],
                        sign(points[index + 1][1], points[index][1]),
                    ):
                        the_map.add((points[index][0], x))
                elif (
                    points[index][1] == points[index + 1][1]
                    and points[index][0] != points[index + 1][0]
                ):
                    for y in range(
                        points[index][0],
                        points[index + 1][0],
                        sign(points[index + 1][0], points[index][0]),
                    ):
                        the_map.add((y, points[index][1]))
                else:
                    raise NotImplementedError
                the_map.add(points[index + 1])
    print(f"the_map = {sorted(the_map)}")
    print(min_x, max_x, min_y, max_y)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == START:
                print("*", end="")
            elif (x, y) in the_map:
                print("#", end="")
            else:
                print(".", end="")
        print()
    step = 1
    is_full = False
    while not is_full:
        sand: Point = START
        while sand[1] <= max_y:
            if (sand[0], sand[1] + 1) not in the_map:
                sand = sand[0], sand[1] + 1
            elif (sand[0] - 1, sand[1] + 1) not in the_map:
                sand = sand[0] - 1, sand[1] + 1
            elif (sand[0] + 1, sand[1] + 1) not in the_map:
                sand = sand[0] + 1, sand[1] + 1
            else:
                break
        print("done", sand)
        the_map.add(sand)
        if sand[1] > max_y:
            is_full == True
            break
        step += 1
    print(step - 1)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == START:
                print("*", end="")
            elif (x, y) in the_map:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    main()
