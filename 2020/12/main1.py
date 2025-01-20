FILENAME = "demo.txt"  # expected 25
FILENAME = "input.txt"

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main() -> None:
    y, x = 0, 0
    dy, dx = 0, 1
    with open(FILENAME, "r") as file:
        for line in file:
            dist = int(line[1:])
            if line[0] == "F":
                y = y + dy * dist
                x = x + dx * dist
            elif line[0] == "N":
                y = y - dist
            elif line[0] == "S":
                y = y + dist
            elif line[0] == "W":
                x = x - dist
            elif line[0] == "E":
                x = x + dist
            elif line[0] == "R":
                if dist == 90:
                    dy, dx = DIRECTIONS[(DIRECTIONS.index((dy, dx)) + 1) % len(DIRECTIONS)]
                elif dist == 180:
                    dy, dx = DIRECTIONS[(DIRECTIONS.index((dy, dx)) + 2) % len(DIRECTIONS)]
                elif dist == 270:
                    dy, dx = DIRECTIONS[(DIRECTIONS.index((dy, dx)) + 3) % len(DIRECTIONS)]
                else:
                    print(f"dist = {dist}")
                    raise NotImplementedError
            elif line[0] == "L":
                if dist == 90:
                    dy, dx = DIRECTIONS[(DIRECTIONS.index((dy, dx)) - 1) % len(DIRECTIONS)]
                elif dist == 180:
                    dy, dx = DIRECTIONS[(DIRECTIONS.index((dy, dx)) - 2) % len(DIRECTIONS)]
                elif dist == 270:
                    dy, dx = DIRECTIONS[(DIRECTIONS.index((dy, dx)) - 3) % len(DIRECTIONS)]
                else:
                    print(f"dist = {dist}")
                    raise NotImplementedError
            else:
                print(f"line[0] = {line[0]}")
                raise NotImplementedError
            # print(line[:-1], y, x)
    print(abs(y) + abs(x))


if __name__ == "__main__":
    main()
