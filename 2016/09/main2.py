import re

FILENAME = "demo2.txt"
FILENAME = "input.txt"


def f(line: str) -> int:
    line_match = re.search(r"\((\d+)x(\d+)\)", line)
    if line_match is None:
        return len(line)
    return (
        len(line[: line_match.start(0)])
        + f(line[line_match.end(0) : line_match.end(0) + int(line_match.group(1))])
        * int(line_match.group(2))
        + f(line[line_match.end(0) + int(line_match.group(1)) :])
    )


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
