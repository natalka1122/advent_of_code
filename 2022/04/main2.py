import re

FILENAME = "demo.txt"  # expected 4
FILENAME = "input.txt"


def f(a1: int, b1: int, a2: int, b2: int) -> bool:
    return (a2 - b1) * (a1 - b2) >= 0


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            if f(
                int(line_match.group(1)),
                int(line_match.group(2)),
                int(line_match.group(3)),
                int(line_match.group(4)),
            ):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
