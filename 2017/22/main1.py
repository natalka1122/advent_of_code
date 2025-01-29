FILENAME, COUNT = "demo.txt", 7  # expected 5
FILENAME, COUNT = "demo.txt", 70  # expected 41
FILENAME, COUNT = "demo.txt", 10000  # expected 5587
FILENAME, COUNT = "input.txt", 10000

CLEAN = "."
INFECTED = "#"
RIGHT = [(1, 0), (0, -1), (-1, 0), (0, 1)]
START_DIRECTION = (-1, 0)


def turn_right(dy: int, dx: int) -> tuple[int, int]:
    return RIGHT[(RIGHT.index((dy, dx)) + 1) % len(RIGHT)]


def turn_left(dy: int, dx: int) -> tuple[int, int]:
    return RIGHT[(RIGHT.index((dy, dx)) - 1) % len(RIGHT)]


def show_infected(y0: int, x0: int, infected: set[tuple[int, int]]) -> None:
    for y in range(0, 3):
        for x in range(0, 3):
            if (y, x) in infected:
                if y == y0 and x == x0:
                    print("@", end="")
                else:
                    print(INFECTED, end="")
            else:
                if y == y0 and x == x0:
                    print("O", end="")
                else:
                    print(CLEAN, end="")
        print()


def main() -> None:
    the_map = []
    infected: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(line.strip())
            for x, symbol in enumerate(line.strip()):
                if symbol == INFECTED:
                    infected.add((len(the_map) - 1, x))
    height = len(the_map)
    width = len(the_map[0])
    y, x = (height // 2, width // 2)
    # show_infected(y, x, infected)
    dy, dx = START_DIRECTION
    result = 0
    for _ in range(COUNT):
        if (y, x) in infected:
            dy, dx = turn_right(dy, dx)
            infected.remove((y, x))
        else:
            dy, dx = turn_left(dy, dx)
            infected.add((y, x))
            result += 1
        y += dy
        x += dx
        # show_infected(y, x, infected)
    print(result)


if __name__ == "__main__":
    main()
