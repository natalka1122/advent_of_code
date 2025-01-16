FILENAME = "demo1.txt"  # expected 10
FILENAME = "demo2.txt"  # expected 64
FILENAME = "input.txt"


def main() -> None:
    cubes = set()
    with open(FILENAME, "r") as file:
        for line in file:
            z, y, x = map(int, line.strip().split(","))
            cubes.add((z, y, x))
    result = 0
    for z, y, x in cubes:
        if (z - 1, y, x) not in cubes:
            result += 1
        if (z + 1, y, x) not in cubes:
            result += 1
        if (z, y - 1, x) not in cubes:
            result += 1
        if (z, y + 1, x) not in cubes:
            result += 1
        if (z, y, x - 1) not in cubes:
            result += 1
        if (z, y, x + 1) not in cubes:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
