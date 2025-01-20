FILENAME = "demo.txt"  # expected 336
FILENAME = "input.txt"

EMPTY = "."
DIRECTIONS = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]


def main() -> None:
    the_map = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(map(lambda x: x == EMPTY, line.strip())))
    width = len(the_map[0])
    result = 1
    for dy, dx in DIRECTIONS:
        current = 0
        self = (0, 0)
        while self[0] < len(the_map):
            if not the_map[self[0]][self[1] % width]:
                current += 1
            self = self[0] + dy, self[1] + dx
        result *= current
    print(result)


if __name__ == "__main__":
    main()
