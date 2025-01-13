import re

FILENAME, HEIGHT, WIDTH = "demo.txt", 3, 7  # expected 6
FILENAME, HEIGHT, WIDTH = "input.txt", 6, 50


def main() -> None:
    the_screen:list[list[bool]] = []
    for _ in range(HEIGHT):
        the_screen.append([])
        for _ in range(WIDTH):
            the_screen[-1].append(False)
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            line_match1 = re.match(r"rect (\d+)x(\d+)", line)
            if line_match1 is not None:
                for y in range(int(line_match1.group(2))):
                    for x in range(int(line_match1.group(1))):
                        the_screen[y][x] = True
                continue
            line_match2 = re.match(r"rotate column x=(\d+) by (\d+)", line)
            if line_match2 is not None:
                x0 = int(line_match2.group(1))
                dy = int(line_match2.group(2))
                backup: list[bool] = []
                for y in range(HEIGHT):
                    backup.append(the_screen[y][x0])
                for y in range(HEIGHT):
                    the_screen[y][x0] = backup[y - dy]
                continue
            line_match3 = re.match(r"rotate row y=(\d+) by (\d+)", line)
            if line_match3 is not None:
                y0 = int(line_match3.group(1))
                dx = int(line_match3.group(2))
                backup = []
                for x in range(WIDTH):
                    backup.append(the_screen[y0][x])
                for x in range(WIDTH):
                    the_screen[y0][x] = backup[x - dx]
                continue
            raise NotImplementedError
    result = 0
    for y in range(HEIGHT):
        result += the_screen[y].count(True)
    print(result)


if __name__ == "__main__":
    main()
