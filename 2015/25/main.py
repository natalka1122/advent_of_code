import re

FILENAME = "demo.txt"  # expected 33071741
FILENAME = "input.txt"
FIRST = 20151125


def f(x: int) -> int:
    return (x * 252533) % 33554393


def main() -> None:
    y0, x0 = None, None
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            y0, x0 = map(int, line_match.groups())
    if y0 is None or x0 is None:
        raise NotImplementedError
    y, x = 1, 1
    number = FIRST
    while (y, x) != (y0, x0):
        if y == 1:
            y, x = x + 1, 1
        else:
            y, x = y - 1, x + 1
        number = f(number)
    print(number)


if __name__ == "__main__":
    main()
