import re

FILENAME = "demo2.txt"  # expected 2000001
FILENAME = "input.txt"
THOUSAND = 1000


def main() -> None:
    the_grid = [[0 for _ in range(THOUSAND)] for _ in range(THOUSAND)]
    with open(FILENAME, "r") as file:
        for line in file:
            turn_on_match = re.match(
                r"turn on (\d+),(\d+) through (\d+),(\d+)", line.strip()
            )
            if turn_on_match is not None:
                x1, y1, x2, y2 = map(int, turn_on_match.groups())
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        the_grid[x][y] += 1
                continue
            turn_off_match = re.match(
                r"turn off (\d+),(\d+) through (\d+),(\d+)", line.strip()
            )
            if turn_off_match is not None:
                x1, y1, x2, y2 = map(int, turn_off_match.groups())
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        the_grid[x][y] = max(0, the_grid[x][y] - 1)
                continue
            toggle_match = re.match(
                r"toggle (\d+),(\d+) through (\d+),(\d+)", line.strip()
            )
            if toggle_match is not None:
                x1, y1, x2, y2 = map(int, toggle_match.groups())
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        the_grid[x][y] += 2
                continue
            raise NotImplementedError
    result = 0
    for y in range(THOUSAND):
        for x in range(THOUSAND):
            result += the_grid[x][y]
    print(result)


if __name__ == "__main__":
    main()
