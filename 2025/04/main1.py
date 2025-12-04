# FILENAME = "demo.txt"  # expected 13
FILENAME = "input.txt"


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        rolls: list[list[bool]] = []
        for line in file:
            rolls.append(list(map(lambda x: x == "@", line.strip())))
    height = len(rolls)
    width = len(rolls[0])
    for y0 in range(height):
        for x0 in range(width):
            if rolls[y0][x0]:
                count = 0
                for y in range(max(0, y0 - 1), min(height, y0 + 2)):
                    for x in range(max(0, x0 - 1), min(width, x0 + 2)):
                        if rolls[y][x]:
                            count += 1
                if count <= 4:
                    result += 1
    print(result)


if __name__ == "__main__":
    main()
