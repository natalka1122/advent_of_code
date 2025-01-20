FILENAME = "demo.txt"  # expected 7
FILENAME = "input.txt"

EMPTY = "."
DIRECTION = (1, 3)


def main() -> None:
    the_map = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(map(lambda x: x == EMPTY, line.strip())))
    width = len(the_map[0])
    print(the_map)
    self = (0, 0)
    result = 0
    while self[0] < len(the_map):
        if not the_map[self[0]][self[1] % width]:
            result += 1
        self = self[0] + DIRECTION[0], self[1] + DIRECTION[1]
    print(result)


if __name__ == "__main__":
    main()
